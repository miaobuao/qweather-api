from typing import List, Optional

from pydantic import BaseModel, Field


class HourlyWeather(BaseModel):
    fxTime: str = Field(..., description="Forecast time in ISO format")
    temp: str = Field(..., description="Temperature (°C)")
    icon: str = Field(..., description="Weather icon code")
    text: str = Field(..., description="Weather description")
    wind360: str = Field(..., description="Wind direction in degrees")
    windDir: str = Field(..., description="Wind direction")
    windScale: str = Field(..., description="Wind scale")
    windSpeed: str = Field(..., description="Wind speed (km/h)")
    humidity: str = Field(..., description="Relative humidity (%)")
    precip: str = Field(..., description="Hourly precipitation (mm)")
    pop: Optional[str] = Field(
        None, description="Hourly probability of precipitation (%)"
    )
    pressure: str = Field(..., description="Atmospheric pressure (hPa)")
    cloud: Optional[str] = Field(None, description="Cloud cover (%), may be empty")
    dew: Optional[str] = Field(None, description="Dew point temperature, may be empty")


class Refer(BaseModel):
    sources: Optional[List[str]] = Field(None, description="Data sources, may be empty")
    license: Optional[List[str]] = Field(
        None, description="Data license or copyright, may be empty"
    )


class HourlyWeatherResponse(BaseModel):
    code: str = Field(..., description="Status code")
    updateTime: str = Field(..., description="Latest API update time")
    fxLink: str = Field(..., description="Responsive page link for embedding")
    hourly: List[HourlyWeather] = Field(..., description="Hourly weather forecast")
    refer: Refer = Field(..., description="Data sources and license information")
