#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#

import random
import string
from pathlib import Path

from rich.console import Console

CONTENT_ENCRYPTION_ALGORITHM = 'aes256_cbc'
DOWNLOADS_PATH = Path.home() / '.aos' / 'downloads'
AOS_DISK_PATH = DOWNLOADS_PATH / 'aos-disk.vmdk'
VBOX_SDK_PATH = DOWNLOADS_PATH / 'vbox-sdk.zip'

DISK_IMAGE_DOWNLOAD_URL = 'https://aos-prod-cdn-endpoint.azureedge.net/vm/aos-image-vm-genericx86-64_3.0.1.wic.vmdk' \
                          '.gz?0b4230d66ef2f41ec6b9bbc796ff2b938d5a317b9009c6a2474fb2c24e86a127a05b5d535a0d115bcd729' \
                          '79c3c78413c9ef5176e48a41361eacf458d20e071d696cd048e072025192f256428051c6d526c2fe6d55c34' \
                          'd46a130945cb73813a'
VIRTUAL_BOX_DOWNLOAD_URL = 'https://download.virtualbox.org/virtualbox/6.1.32/VirtualBoxSDK-6.1.32-149290.zip'

console = Console()


def generate_random_password() -> str:
    """
    Generate random password from letters and digits.

    Returns:
        str: Random string password
    """
    dictionary = string.ascii_letters + string.digits
    password_length = random.randint(10, 15)
    return ''.join(random.choice(dictionary) for _ in range(password_length))
