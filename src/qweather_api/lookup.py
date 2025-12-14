import re
from typing import Iterable

import Levenshtein
import pandas as pd

from qweather_api.dataframes import (
    china_city_list,
    location_name_en,
    location_name_en_list,
    location_name_zh,
    location_name_zh_list,
)
from qweather_api.schema import City, GeoCoordinate


def series_to_city(series: pd.Series) -> City:
    return City(
        location_id=series["Location_ID"],
        location_name_en=series["Location_Name_EN"],
        location_name_zh=series["Location_Name_ZH"],
        iso3166_alpha2=series["ISO_3166_1"],
        country_region_en=series["Country_Region_EN"],
        country_region_zh=series["Country_Region_ZH"],
        adm1_name_en=series["Adm1_Name_EN"],
        adm1_name_zh=series["Adm1_Name_ZH"],
        adm2_name_en=series["Adm2_Name_EN"],
        adm2_name_zh=series["Adm2_Name_ZH"],
        timezone=series["Timezone"],
        geo_coordinate=GeoCoordinate(
            latitude=series["Latitude"],
            longitude=series["Longitude"],
        ),
        ad_code=series["AD_code"],
    )


def deduplicate_cities(cities: Iterable[City]) -> list[City]:
    return list(
        (
            {(c.geo_coordinate.latitude, c.geo_coordinate.longitude): c for c in cities}
        ).values()
    )


def lookup_location_name_en(location: str, editdistance: int = 1) -> list[City]:
    candidates: list[tuple[int, City]] = []
    for c in location_name_en_list:
        distance = Levenshtein.distance(location.lower(), c.lower(), weights=(1, 1, 2))
        if distance <= editdistance:
            series = china_city_list[location_name_en == c].iloc[0]
            candidates.append((distance, series_to_city(series)))
    candidates.sort(key=lambda c: c[0])
    return [c[1] for c in candidates]


def lookup_location_name_zh(location: str, editdistance: int = 1) -> list[City]:
    candidates: list[tuple[int, City]] = []
    for c in location_name_zh_list:
        distance = Levenshtein.distance(location.lower(), c.lower(), weights=(1, 1, 2))
        if distance <= editdistance:
            series = china_city_list[location_name_zh == c].iloc[0]
            candidates.append((distance, series_to_city(series)))
    candidates.sort(key=lambda c: c[0])
    return [c[1] for c in candidates]


def lookup_location_name(location: str) -> list[City]:
    match = re.compile(r"[\sa-zA-Z]*").fullmatch(location)
    if match:
        return lookup_location_name_en(location)
    return lookup_location_name_zh(location)
