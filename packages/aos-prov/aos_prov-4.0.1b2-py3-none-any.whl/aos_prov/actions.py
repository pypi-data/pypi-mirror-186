#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#
import os
import platform
import subprocess
import time
import zipfile
from pathlib import Path

from aos_prov.commands.command_provision import run_provision
from aos_prov.commands.download import download_and_save_file, download_and_save_multinode
from aos_prov.communication.cloud.cloud_api import CloudAPI
from aos_prov.utils.common import DOWNLOADS_PATH, AOS_DISK_PATH, AOS_DISKS_PATH
from aos_prov.utils.user_credentials import UserCredentials


def create_new_unit(vm_name: str, uc: UserCredentials, disk_location: str, do_provision=False):
    cloud_api = CloudAPI(uc)
    # cloud_api.check_cloud_access()
    if platform.system() == 'Linux':
        from aos_prov.commands.command_vm_multi_node import new_vm, start_vms
        vm_port = new_vm(vm_name, disk_location)
        start_vms([f'/AosUnits/{vm_name}'])
    elif platform.system() == 'Darwin':
        from aos_prov.commands.command_vm_multi_node import new_vm, start_vms
        vm_port = new_vm(vm_name, disk_location)
        start_vms([f'/AosUnits/{vm_name}'])
    elif platform.system() == 'Windows':
        from aos_prov.commands.command_vm_multi_node import new_vm, start_vms
        vm_port = new_vm(vm_name, disk_location)
        start_vms([f'/AosUnits/{vm_name}'])
    if do_provision:
        time.sleep(10)
        run_provision(f'127.0.0.1:{vm_port}', cloud_api, reconnect_times=20)


def download_image(download_url: str, force: bool = False):
    download_and_save_multinode(download_url, DOWNLOADS_PATH, force)
    print('Download finished. You may find Unit images in: ' + str(DOWNLOADS_PATH.resolve()))


def install_vbox_sdk():
    file = download_vbox_sdk()

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(DOWNLOADS_PATH)

    envs = os.environ.copy()
    if platform.system() == 'Windows':
        command = ['python', 'vboxapisetup.py', 'install', '--user']
    elif platform.system() == 'Linux':
        'VBOX_INSTALL_PATH=$(which virtualbox)'
        command = ['python3', 'vboxapisetup.py', 'install', '--user', '--prefix=']
    elif platform.system() == 'Darwin':
        'VBOX_INSTALL_PATH=/Applications/VirtualBox.app/Contents/MacOS'
        command = ['python3', 'vboxapisetup.py', 'install', '--user', '--prefix=']
    else:
        command = 'VBOX_INSTALL_PATH=$(which virtualbox) python3 vboxapisetup.py install --user --prefix='
    return_code = subprocess.run(command, shell=True, env=envs, cwd=str(Path(DOWNLOADS_PATH / 'sdk' / 'installer')))
    if return_code.returncode == 0:
        return
    else:
        print('Error installing VirtualBox SDK')
