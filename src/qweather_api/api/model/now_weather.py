from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class NowWeather(BaseModel):
    obsTime: Optional[datetime] = Field(
        None, description="Observation time of the weather data"
    )
    temp: Optional[int] = Field(None, description="Temperature in Celsius")
    feelsLike: Optional[int] = Field(
        None, description="Feels-like temperature in Celsius"
    )
    icon: Optional[str] = Field(
        None, description="Weather condition icon code (see official icon set)"
    )
    text: Optional[str] = Field(
        None,
        description="Text description of the weather condition, e.g., sunny, cloudy, rain, snow",
    )
    wind360: Optional[int] = Field(
        None, description="Wind direction in degrees (0-360)"
    )
    windDir: Optional[str] = Field(None, description="Wind direction as text")
    windScale: Optional[int] = Field(None, description="Wind scale level")
    windSpeed: Optional[int] = Field(None, description="Wind speed in km/h")
    humidity: Optional[int] = Field(None, description="Relative humidity in percentage")
    precip: Optional[float] = Field(
        None, description="Precipitation in the past 1 hour, in millimeters"
    )
    pressure: Optional[int] = Field(None, description="Atmospheric pressure in hPa")
    vis: Optional[int] = Field(None, description="Visibility in kilometers")
    cloud: Optional[int] = Field(
        None, description="Cloud cover in percentage. May be null"
    )
    dew: Optional[int] = Field(None, description="Dew point temperature. May be null")


class Refer(BaseModel):
    sources: Optional[List[str]] = Field(
        None, description="Original data sources. May be null or empty"
    )
    license: Optional[List[str]] = Field(
        None, description="Data license or copyright statement. May be null or empty"
    )


class NowWeatherResponse(BaseModel):
    code: str = Field(
        ..., description="API status code. See official status code reference"
    )
    updateTime: Optional[datetime] = Field(
        None, description="The latest update time of this API response"
    )
    fxLink: Optional[str] = Field(
        None,
        description="Responsive page link for the current weather data, suitable for embedding",
    )
    now: NowWeather = Field(..., description="Current real-time weather data")
    refer: Optional[Refer] = Field(
        None, description="Data sources and licensing information"
    )
