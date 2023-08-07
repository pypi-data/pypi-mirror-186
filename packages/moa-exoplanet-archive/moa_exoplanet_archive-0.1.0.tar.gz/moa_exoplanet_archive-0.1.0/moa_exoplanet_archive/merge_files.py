import getpass
import gzip
import io
import multiprocessing
from functools import partial
from pathlib import Path
from typing import Optional

import astropy.io.ascii
import numpy as np
import pandas as pd
import pysftp as pysftp
from astropy.table import Table
from tabulate import tabulate

from moa_exoplanet_archive.column_name import phot_all_column_names, phot_cor_column_names, ColumnName, \
    merged_column_names, merged_column_formats


def merge_split_version_files_into_single_file(dot_phot_dot_all_path: Path, destination_merged_path: Path):
    containing_directory_path = dot_phot_dot_all_path.parent
    dot_phot_name = dot_phot_dot_all_path.name.replace('.phot.all', '.phot')
    dot_phot_path = containing_directory_path.joinpath(dot_phot_name)
    dot_phot_dot_cor_name = dot_phot_dot_all_path.name.replace('.phot.all', '.phot.cor')
    dot_phot_dot_cor_path = containing_directory_path.joinpath(dot_phot_dot_cor_name)
    dot_phot_dot_all_data_frame = pd.read_csv(dot_phot_dot_all_path, comment='#', names=phot_all_column_names,
                                              delim_whitespace=True, skipinitialspace=True)
    dot_phot_data_frame = pd.read_csv(dot_phot_path, comment='#', names=phot_all_column_names,
                                      delim_whitespace=True, skipinitialspace=True)
    without_cor_data_frame = pd.merge(dot_phot_dot_all_data_frame,
                                      dot_phot_data_frame[[ColumnName.HJD,]],
                                      on=ColumnName.HJD, how='outer', indicator=True)
    without_cor_data_frame[ColumnName.INCLUDED] = without_cor_data_frame['_merge'] == 'both'
    without_cor_data_frame.drop(columns='_merge', inplace=True)
    missing_columns = list(set(phot_cor_column_names) - set(phot_all_column_names))
    if dot_phot_dot_cor_path.exists():
        dot_phot_dot_cor_data_frame = pd.read_csv(dot_phot_dot_cor_path, comment='#', names=phot_cor_column_names,
                                                  delim_whitespace=True, skipinitialspace=True)
        columns_to_merge_in = missing_columns + [ColumnName.HJD]
        unordered_merged_data_frame = pd.merge(without_cor_data_frame,
                                               dot_phot_dot_cor_data_frame[columns_to_merge_in], on=ColumnName.HJD,
                                               how='outer')
        if unordered_merged_data_frame[ColumnName.AIRMASS_1].isna().all():
            unordered_merged_data_frame[ColumnName.COR_FLUX] = np.nan
    else:
        for missing_column in missing_columns:
            without_cor_data_frame[missing_column] = np.nan
        unordered_merged_data_frame = without_cor_data_frame
    merged_data_frame = unordered_merged_data_frame[merged_column_names]
    save_data_frame_to_compressed_ipac_file(merged_data_frame, destination_merged_path)


def save_data_frame_to_traditional_format_text_file(data_frame, output_path):
    table_string = tabulate(data_frame, headers=merged_column_names, tablefmt='plain', missingval='na',
                            floatfmt=tuple(merged_column_formats.values()), showindex=False, numalign='right')
    table_string = table_string.replace('nan', ' na')
    with gzip.open(output_path, 'wt') as merged_file:
        merged_file.write(table_string)


def save_data_frame_to_compressed_ipac_file(data_frame: pd.DataFrame, output_path: Path):
    data_table: Table = Table.from_pandas(data_frame)
    string_io = io.StringIO()
    astropy.io.ascii.write(data_table, output=string_io, format='ipac')
    with gzip.open(output_path, 'wt') as merged_file:
        merged_file.write(string_io.getvalue())


def merge_three_version_directory(phot_all_path, three_version_directory, merged_version_directory):
    merged_sub_path = phot_all_path.relative_to(three_version_directory)
    merged_path = merged_version_directory.joinpath(merged_sub_path)
    merged_path = merged_path.parent.joinpath(merged_path.name.replace('.phot.all', '.ipac.gz'))
    merged_path.parent.mkdir(parents=True, exist_ok=True)
    merge_split_version_files_into_single_file(phot_all_path, merged_path)


def convert_directory_to_merged_version(three_version_directory: Path, merged_version_directory: Path):
    merge_three_version_with_roots = partial(merge_three_version_directory,
                                             three_version_directory=three_version_directory,
                                             merged_version_directory=merged_version_directory)
    paths = three_version_directory.glob('**/*.phot.all')
    with multiprocessing.get_context('spawn').Pool(processes=20, maxtasksperchild=200) as pool:
        for _ in pool.imap_unordered(merge_three_version_with_roots, paths):
            pass


def copy_and_merge_from_remote(remote_hostname: str, remote_username: str, remote_password: Optional[str] = None,
                               remote_private_key: Optional[str] = None):
    with pysftp.Connection(remote_hostname, username=remote_username, private_key=remote_private_key,
                           password=remote_password) as sftp:
        remote_three_version_root_directory = Path('/root/moa/MOA2dia')
        local_merged_root_directory = Path('check0')
        count = 0

        def remote_to_local_merge_split_version_files_into_single_file(remote_dot_phot_dot_all_path_str: str):
            if remote_dot_phot_dot_all_path_str.endswith('.phot.all'):
                remote_dot_phot_dot_all_path = Path(remote_dot_phot_dot_all_path_str)
                nonlocal count
                print(f'{count}: {remote_dot_phot_dot_all_path}')
                count += 1
                dot_phot_dot_all_name = remote_dot_phot_dot_all_path.name
                remote_containing_directory_path = remote_dot_phot_dot_all_path.parent
                dot_phot_name = remote_dot_phot_dot_all_path.name.replace('.phot.all', '.phot')
                remote_dot_phot_path = remote_containing_directory_path.joinpath(dot_phot_name)
                dot_phot_dot_cor_name = remote_dot_phot_dot_all_path.name.replace('.phot.all', '.phot.cor')
                remote_dot_phot_dot_cor_path = remote_containing_directory_path.joinpath(dot_phot_dot_cor_name)
                relative_parent_path = remote_dot_phot_dot_all_path.parent.relative_to(remote_three_version_root_directory)
                local_parent_path = local_merged_root_directory.joinpath(relative_parent_path)
                local_parent_path.mkdir(exist_ok=True, parents=True)
                local_dot_phot_dot_all_path = local_parent_path.joinpath(dot_phot_dot_all_name)
                local_dot_phot_path = local_parent_path.joinpath(dot_phot_name)
                local_dot_phot_dot_cor_path = local_parent_path.joinpath(dot_phot_dot_cor_name)
                sftp.get(str(remote_dot_phot_dot_all_path), str(local_dot_phot_dot_all_path))
                sftp.get(str(remote_dot_phot_path), str(local_dot_phot_path))
                if sftp.exists(str(remote_dot_phot_dot_cor_path)):
                    sftp.get(str(remote_dot_phot_dot_cor_path), str(local_dot_phot_dot_cor_path))
                merged_path = local_dot_phot_dot_all_path.parent.joinpath(
                    local_dot_phot_dot_all_path.name.replace('.phot.all', '.ipac.gz'))
                merge_split_version_files_into_single_file(local_dot_phot_dot_all_path, merged_path)
                local_dot_phot_dot_all_path.unlink()
                local_dot_phot_path.unlink()
                local_dot_phot_dot_cor_path.unlink(missing_ok=True)

        def pass_function(_):
            pass

        sftp.walktree(remotepath=str(remote_three_version_root_directory),
                      fcallback=remote_to_local_merge_split_version_files_into_single_file,
                      dcallback=pass_function, ucallback=pass_function)


if __name__ == '__main__':
    remote_hostname_ = input('Remote hostname: ')
    remote_username_ = input('User hostname: ')
    remote_password_ = getpass.getpass(prompt='Remote password: ')
    remote_private_key_ = None
    if remote_password_ == '':
        remote_password_ = None
        remote_private_key_ = input('Remote private key path: ')
    copy_and_merge_from_remote(remote_hostname_, remote_username_, remote_password=remote_password_,
                               remote_private_key=remote_private_key_)
