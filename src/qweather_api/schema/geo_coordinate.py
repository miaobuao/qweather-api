from pydantic import BaseModel


class GeoCoordinate(BaseModel):
    latitude: float
    longitude: float

    @property
    def text(self):
        return f"{self.longitude},{self.latitude}"
