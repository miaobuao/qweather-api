from typing import List, Optional

from pydantic import BaseModel, Field


class DailyWeather(BaseModel):
    fxDate: str = Field(..., description="Forecast date")
    sunrise: Optional[str] = Field(
        None, description="Sunrise time, may be empty in high latitude regions"
    )
    sunset: Optional[str] = Field(
        None, description="Sunset time, may be empty in high latitude regions"
    )
    moonrise: Optional[str] = Field(None, description="Moonrise time, may be empty")
    moonset: Optional[str] = Field(None, description="Moonset time, may be empty")
    moonPhase: str = Field(..., description="Name of the moon phase")
    moonPhaseIcon: str = Field(..., description="Icon code of the moon phase")
    tempMax: str = Field(..., description="Maximum temperature of the day")
    tempMin: str = Field(..., description="Minimum temperature of the day")
    iconDay: str = Field(..., description="Daytime weather icon code")
    textDay: str = Field(..., description="Daytime weather description")
    iconNight: str = Field(..., description="Nighttime weather icon code")
    textNight: str = Field(..., description="Nighttime weather description")
    wind360Day: str = Field(..., description="Daytime wind direction in degrees")
    windDirDay: str = Field(..., description="Daytime wind direction")
    windScaleDay: str = Field(..., description="Daytime wind scale")
    windSpeedDay: str = Field(..., description="Daytime wind speed (km/h)")
    wind360Night: str = Field(..., description="Nighttime wind direction in degrees")
    windDirNight: str = Field(..., description="Nighttime wind direction")
    windScaleNight: str = Field(..., description="Nighttime wind scale")
    windSpeedNight: str = Field(..., description="Nighttime wind speed (km/h)")
    humidity: str = Field(..., description="Relative humidity (%)")
    precip: str = Field(..., description="Total precipitation of the day (mm)")
    pressure: str = Field(..., description="Atmospheric pressure (hPa)")
    vis: str = Field(..., description="Visibility (km)")
    cloud: Optional[str] = Field(None, description="Cloud cover (%), may be empty")
    uvIndex: str = Field(..., description="UV index")


class Refer(BaseModel):
    sources: Optional[List[str]] = Field(None, description="Data sources, may be empty")
    license: Optional[List[str]] = Field(
        None, description="Data license or copyright, may be empty"
    )


class DailyWeatherResponse(BaseModel):
    code: str = Field(..., description="Status code")
    updateTime: str = Field(..., description="Latest API update time")
    fxLink: str = Field(..., description="Responsive page link for embedding")
    daily: List[DailyWeather] = Field(..., description="Daily weather forecast")
    refer: Refer = Field(..., description="Data sources and license information")
