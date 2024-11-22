import os
from settings import CURRENT_DIR


def get_names_in_folder(folder_path: str) -> set[str]:
    files = os.listdir(folder_path)
    return {file.removesuffix('.pgn') for file in files}


def main() -> None:
    converted_datasets = get_names_in_folder(os.path.join(CURRENT_DIR, 'Datasets'))
    raw_datasets = get_names_in_folder(os.path.join(CURRENT_DIR, 'Raw datasets'))

    datasets_to_convert = raw_datasets - converted_datasets

    for dataset in datasets_to_convert:
        with open(os.path.join(CURRENT_DIR, 'Datasets', f'{dataset}.txt'), 'w') as file_to_write:
            with open(os.path.join(CURRENT_DIR, 'Raw datasets', f'{dataset}.pgn'), 'r') as file_to_read:
                for line in file_to_read:
                    if line.startswith('[') or line == '\n': continue
                    file_to_write.write(line)

        print('Converted:', dataset)

    input('Program finished. Press enter to exit...')

if __name__ == '__main__':
    main()
