from pydantic import SecretStr

from qweather_api import QWeatherApiClient, QWeatherApiConfig, lookup_location_name

# Lookup Location
cities = lookup_location_name("Beijing")


client = QWeatherApiClient(
    config=QWeatherApiConfig(
        api_host="https://xxx.re.qweatherapi.com",
        project_id="xxx",
        kid="xxx",
        private_key=SecretStr("..."),
        alg="EdDSA",
    )
)

now_weather = client.get_now_weather(cities[0].location_id, "zh")
print(now_weather)
