import os
from datetime import date
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    pass


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    pass


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    pass