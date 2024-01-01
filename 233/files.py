from datetime import datetime
import os
from pathlib import Path
from zipfile import ZipFile

TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: Path = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
    pass