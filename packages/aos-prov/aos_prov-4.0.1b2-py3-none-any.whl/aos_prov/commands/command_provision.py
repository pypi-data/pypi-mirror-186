#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#
"""Provision unit."""

import time

from colorama import Fore, Style
from aos_prov.communication.cloud.cloud_api import CloudAPI
from aos_prov.communication.unit.v0.unit_communication import UnitCommunication
from aos_prov.communication.unit.v1.unit_communication_v1 import UnitCommunicationV1
from aos_prov.communication.unit.v2.unit_communication_v2 import UnitCommunicationV2
from aos_prov.communication.unit.v4.unit_communication_v4 import UnitCommunicationV4
from aos_prov.utils.config import Config
from aos_prov.utils.errors import GrpcUnimplemented, BoardError
from aos_prov.utils.common import generate_random_password, console

COMMAND_TO_DECRYPT = 'diskencryption'


def run_provision(unit_address: str, cloud_api: CloudAPI, reconnect_times: int = 1):
    """
    Provision Unit. This function will try to provision starting from the newest to the oldest.

    Args:
         unit_address (str): Address of the Unit
         cloud_api (CloudAPI): URL to download
         reconnect_times (int): URL to download

    Raises:
        AosProvError: If provision fails.
    """
    config = Config()
    uc = UnitCommunicationV4(unit_address)
    model_name = ''
    for retry in range(reconnect_times):
        try:
            console.print('Starting provisioning using protocol v4')
            config.system_id, model_name = uc.get_system_info()
            config.protocol_version = uc.get_protocol_version()
            break
        except GrpcUnimplemented:
            try:
                console.print('v4 is not supported. Starting provisioning using protocol v2')
                uc = UnitCommunicationV2(unit_address)
                if uc.get_protocol_version() == 3:
                    uc.need_set_users = False
                config.system_id, model_name = uc.get_system_info()
                config.protocol_version = uc.get_protocol_version()
                break
            except GrpcUnimplemented:
                try:
                    print('v2 is not supported. Using protocol v1')
                    uc = UnitCommunicationV1(unit_address)
                    config.system_id, model_name = uc.get_system_info()
                    config.protocol_version = uc.get_protocol_version()
                    break
                except GrpcUnimplemented:
                    print('v1 is not supported. Using protocol v0')
                    uc = UnitCommunication(unit_address)
                    config.system_id, model_name = uc.get_system_info()
                    config.protocol_version = uc.get_protocol_version()
                    break
        except BoardError as be:
            if retry + 1 < reconnect_times:
                time.sleep(5)
            else:
                raise be

    if config.system_id is None:
        raise BoardError('Cannot read system_id')

    config.set_model(model_name)
    cloud_api.check_unit_is_not_provisioned(config.system_id)
    if config.protocol_version >= 4:  # support of multi domains
        config.node_ids = uc.get_all_node_ids()
        for node_id in config.node_ids:
            config.supported_cert_types = uc.get_cert_types(node_id)

            password = generate_random_password()

            for cert_type in config.supported_cert_types:
                uc.clear(cert_type, node_id)

            for cert_type in config.supported_cert_types:
                uc.set_cert_owner(cert_type, password, node_id)

            if COMMAND_TO_DECRYPT in config.supported_cert_types:
                config.supported_cert_types.remove(COMMAND_TO_DECRYPT)
                uc.encrypt_disk(password, node_id)
                uc.wait_for_connection()

            for cert_type in config.supported_cert_types:
                config.unit_certificates.append(uc.create_keys(cert_type, password, node_id))
    else:
        config.supported_cert_types = uc.get_cert_types()

        password = generate_random_password()

        for cert_type in config.supported_cert_types:
            uc.clear(cert_type)

        for cert_type in config.supported_cert_types:
            uc.set_cert_owner(cert_type, password)

        if COMMAND_TO_DECRYPT in config.supported_cert_types:
            config.supported_cert_types.remove(COMMAND_TO_DECRYPT)
            uc.encrypt_disk(password)
            uc.wait_for_connection()

        for cert_type in config.supported_cert_types:
            config.unit_certificates.append(uc.create_keys(cert_type, password))

    register_payload = {
        'hardware_id': config.system_id,
        'system_uid': config.system_id,
        'board_model_name': config.model_name,
        'board_model_version': config.model_version,
        'provisioning_software': "aos-provisioning:{version}".format(version=3.1),
        'additional_csrs': []
    }

    if cloud_api.use_model_name_param():
        register_payload['model_name'] = config.model_name
        register_payload['model_version'] = config.model_version
    else:
        register_payload['board_model_name'] = config.model_name
        register_payload['board_model_version'] = config.model_version

    for cert in config.unit_certificates:
        if cert.cert_type == 'online':
            register_payload['online_public_csr'] = cert.csr
            if cert.node_id:
                register_payload['online_public_node_id'] = cert.node_id
        elif cert.cert_type == 'offline':
            register_payload['offline_public_csr'] = cert.csr
            if cert.node_id:
                register_payload['offline_public_node_id'] = cert.node_id
        else:
            register_payload['additional_csrs'].append({
                'cert_type': cert.cert_type,
                'csr': cert.csr,
                'node_id': cert.node_id,
            })

    response = cloud_api.register_device(register_payload)
    system_uid = response.get('system_uid')
    additional_certs = response.get('additional_certs', [])
    for cert in config.unit_certificates:
        if cert.cert_type == 'online':
            cert.certificate = response.get('online_certificate')
        elif cert.cert_type == 'offline':
            cert.certificate = response.get('offline_certificate')
        else:
            for ac in additional_certs:
                if ac['cert_type'] == cert.cert_type:
                    if ac.get('node_id'):
                        if ac.get('node_id') == cert.node_id:
                            cert.certificate = ac['cert']
                            break
                    else:
                        cert.certificate = ac['cert']
                        cert.node_id = ac.get('node_id')
                        break

    for cert in config.unit_certificates:
        uc.apply_certificate(cert)

    claims = response.get('claim')

    if claims:
        if not hasattr(uc, 'need_set_users'):
            uc.set_users([claims])
        elif uc.need_set_users:
            uc.set_users([claims])

    uc.finish_provisioning()

    print(f'{Fore.GREEN}Finished successfully!{Style.RESET_ALL}')
    link = cloud_api.get_unit_link_by_system_uid(system_uid)
    if link:
        print(f'You may find your unit on the cloud here: {Fore.GREEN}{link}{Style.RESET_ALL}')
