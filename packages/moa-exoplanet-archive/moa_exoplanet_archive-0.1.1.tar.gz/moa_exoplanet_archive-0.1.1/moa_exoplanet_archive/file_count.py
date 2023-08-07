from pathlib import Path

merged_version_directory = Path('merged_MOA2dia')
paths = merged_version_directory.glob('**/*.txt.gz')
print(f'Merged: {len(list(paths))}')

merged_version_directory = Path('MOA2dia')
paths = merged_version_directory.glob('**/*.gz')
print(f'Unmerged: {len(list(paths))}')
