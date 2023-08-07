from pathlib import Path


def count_file_versions(three_version_root_directory: Path):
    paths = three_version_root_directory.glob('**/*.gz')
    dot_phot_count = 0
    dot_phot_dot_all_count = 0
    dot_phot_dot_cor_count = 0
    for path in paths:
        if path.name.endswith('.phot.all.gz'):
            dot_phot_dot_all_count += 1
        if path.name.endswith('.phot.gz'):
            dot_phot_count += 1
        if path.name.endswith('.phot.cor.gz'):
            dot_phot_dot_cor_count += 1
    print(f'.phot.all.gz count: {dot_phot_dot_all_count}')
    print(f'.phot.gz count: {dot_phot_count}')
    print(f'.phot.cor.gz count: {dot_phot_dot_cor_count}')


if __name__ == '__main__':
    three_version_root_directory_ = Path('MOA2dia')
    count_file_versions(three_version_root_directory_)
