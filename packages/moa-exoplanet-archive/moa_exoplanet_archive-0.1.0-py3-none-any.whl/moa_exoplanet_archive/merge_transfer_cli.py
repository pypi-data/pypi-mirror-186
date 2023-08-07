
import getpass

from moa_exoplanet_archive.merge_files import copy_and_merge_from_remote


def merge_transfer():
    remote_hostname = input('Remote hostname: ')
    remote_username = input('User hostname: ')
    remote_password = getpass.getpass(prompt='Remote password: ')
    remote_private_key = None
    if remote_password == '':
        remote_password = None
        remote_private_key = input('Remote private key path: ')
    copy_and_merge_from_remote(remote_hostname, remote_username, remote_password=remote_password,
                               remote_private_key=remote_private_key)
