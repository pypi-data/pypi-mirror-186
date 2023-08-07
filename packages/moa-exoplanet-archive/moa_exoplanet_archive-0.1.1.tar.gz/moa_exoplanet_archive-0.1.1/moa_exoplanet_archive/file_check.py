import random
import shutil
from pathlib import Path

unmerged_version_directory = Path('MOA2dia')
merged_version_directory = Path('merged_MOA2dia')
paths = unmerged_version_directory.glob('**/*.phot.all.gz')
paths = map(Path, paths)
paths = list(paths)
random.shuffle(paths)
spot_check_directory = Path('merge_spot_check')
spot_check_directory.mkdir(exist_ok=True, parents=True)
for index in range(3):
    spot_check_phot_all_path = paths[index]
    spot_check_phot_path = spot_check_phot_all_path.parent.joinpath(
        spot_check_phot_all_path.name.replace('.phot.all.gz', '.phot.gz'))
    spot_check_phot_cor_path = spot_check_phot_all_path.parent.joinpath(
        spot_check_phot_all_path.name.replace('.phot.all.gz', '.phot.cor.gz'))
    spot_check_merged_path = Path(f'merged_{spot_check_phot_all_path.parent}').joinpath(
        spot_check_phot_all_path.name.replace('.phot.all.gz', '.txt.gz'))
    shutil.copy(spot_check_phot_all_path, spot_check_directory.joinpath(spot_check_phot_all_path.name))
    shutil.copy(spot_check_phot_path, spot_check_directory.joinpath(spot_check_phot_path.name))
    shutil.copy(spot_check_phot_cor_path, spot_check_directory.joinpath(spot_check_phot_cor_path.name))
    shutil.copy(spot_check_merged_path, spot_check_directory.joinpath(spot_check_merged_path.name))
