from pydantic import BaseModel

from qweather_api.schema.geo_coordinate import GeoCoordinate


class City(BaseModel):
    location_id: str
    location_name_en: str
    location_name_zh: str
    iso3166_alpha2: str
    country_region_en: str
    country_region_zh: str
    adm1_name_en: str
    adm1_name_zh: str
    adm2_name_en: str
    adm2_name_zh: str
    timezone: str
    geo_coordinate: GeoCoordinate
    ad_code: str
