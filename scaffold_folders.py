

from pathlib import Path
import shutil


NEEDED_FOLDERS = [
    './data/mart',
    './data/ml_models',
    './data/ml',
    './data/raw',
    './data/staging',
    './data/staging/lookups'
]

def create_folders():
    for folder in NEEDED_FOLDERS:
        Path(folder).mkdir(parents=True, exist_ok=True)

def copy_files():
    shutil.copyfile('./important_committee_lookup.csv', './data/staging/lookups/important_committee_lookup.csv')
    

if __name__ == "__main__":
    create_folders()
    copy_files()