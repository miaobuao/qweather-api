from pathlib import Path

import pandas as pd

LOCATION_LIST_ROOT_PATH = Path(__file__).parent / "LocationList"
CHINA_CITY_LIST_CSV_PATH = LOCATION_LIST_ROOT_PATH / "China-City-List-latest.csv"

china_city_list = pd.read_csv(CHINA_CITY_LIST_CSV_PATH, header=1)

location_name_zh = china_city_list["Location_Name_ZH"]
location_name_en = china_city_list["Location_Name_EN"]
location_name_en_list: list[str] = list(location_name_en)
location_name_zh_list: list[str] = list(location_name_zh)
