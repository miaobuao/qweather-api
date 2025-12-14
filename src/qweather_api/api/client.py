import time
from typing import Literal

import httpx
import jwt

from qweather_api.api.config import QWeatherApiConfig
from qweather_api.api.model.daily_weather import DailyWeatherResponse
from qweather_api.api.model.hourly_weather import HourlyWeatherResponse
from qweather_api.api.model.now_weather import NowWeatherResponse
from qweather_api.api.types import LangCodeType, UnitType
from qweather_api.schema.geo_coordinate import GeoCoordinate


class QWeatherApiClient:
    def __init__(
        self,
        config: QWeatherApiConfig,
        client: httpx.Client | None = None,
        async_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.config = config
        self._client = client
        self._async_client = async_client

    def get_jwt(self) -> str:
        headers = {
            "alg": self.config.alg,
            "kid": self.config.kid,
        }
        payload = {
            "sub": self.config.project_id,
            "iat": int(time.time()) - 30,
            "exp": int(time.time()) + 900,
        }
        encoded_jwt = jwt.encode(
            payload,
            self.config.private_key.get_secret_value(),
            algorithm=self.config.alg,
            headers=headers,
        )
        return encoded_jwt

    def get_client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(
                base_url=str(self.config.api_host),
                headers={"Authorization": f"Bearer {self.get_jwt()}"},
            )
        return self._client

    def get_async_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=str(self.config.api_host),
                headers={"Authorization": f"Bearer {self.get_jwt()}"},
            )
        return self._async_client

    def get_now_weather(
        self,
        location: str | GeoCoordinate,
        lang: LangCodeType = "zh",
        unit: UnitType = "m",
    ):
        client = self.get_client()
        response = client.get(
            "/v7/weather/now",
            params={
                "location": location if isinstance(location, str) else location.text,
                "lang": lang,
                "unit": unit,
            },
        )
        return NowWeatherResponse(**response.json())

    async def aget_now_weather(
        self,
        location: str | GeoCoordinate,
        lang: LangCodeType = "zh",
        unit: UnitType = "m",
    ):
        client = self.get_async_client()
        response = await client.get(
            "/v7/weather/now",
            params={
                "location": location if isinstance(location, str) else location.text,
                "lang": lang,
                "unit": unit,
            },
        )
        return NowWeatherResponse(**response.json())

    def get_daily_weather(
        self,
        days: Literal["3d", "7d", "10d", "15d", "30d"],
        location: str | GeoCoordinate,
        lang: LangCodeType = "zh",
        unit: UnitType = "m",
    ):
        client = self.get_client()
        response = client.get(
            f"/v7/weather/{days}",
            params={
                "location": location if isinstance(location, str) else location.text,
                "lang": lang,
                "unit": unit,
            },
        )
        return DailyWeatherResponse(**response.json())

    async def aget_daily_weather(
        self,
        days: Literal["3d", "7d", "10d", "15d", "30d"],
        location: str | GeoCoordinate,
        lang: LangCodeType = "zh",
        unit: UnitType = "m",
    ):
        client = self.get_async_client()
        response = await client.get(
            f"/v7/weather/{days}",
            params={
                "location": location if isinstance(location, str) else location.text,
                "lang": lang,
                "unit": unit,
            },
        )
        return DailyWeatherResponse(**response.json())

    def get_hourly_weather(
        self,
        hours: Literal["24h", "72h", "168h"],
        location: str | GeoCoordinate,
        lang: LangCodeType = "zh",
        unit: UnitType = "m",
    ):
        client = self.get_client()
        response = client.get(
            f"/v7/weather/{hours}",
            params={
                "location": location if isinstance(location, str) else location.text,
                "lang": lang,
                "unit": unit,
            },
        )
        return HourlyWeatherResponse(**response.json())

    async def aget_hourly_weather(
        self,
        hours: Literal["24h", "72h", "168h"],
        location: str | GeoCoordinate,
        lang: LangCodeType = "zh",
        unit: UnitType = "m",
    ):
        client = self.get_async_client()
        response = await client.get(
            f"/v7/weather/{hours}",
            params={
                "location": location if isinstance(location, str) else location.text,
                "lang": lang,
                "unit": unit,
            },
        )
        return HourlyWeatherResponse(**response.json())
