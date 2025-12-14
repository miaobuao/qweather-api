from typing import Literal, Optional

from pydantic import AnyHttpUrl, BaseModel, Field


class QWeatherApiConfig(BaseModel):
    """
    Configuration model for accessing the QWeather API using JWT authentication.

    This model encapsulates all required parameters to authenticate requests
    against the QWeather API. QWeather uses a developer-specific API Host and
    standard JWT (JSON Web Token) signing with the EdDSA algorithm.

    The configuration values are used as follows:

    - ``api_host``:
      A developer-specific API endpoint that replaces the public QWeather API host.
      It is part of the authentication mechanism and must be correct for all requests.

    - ``project_id``:
      The Project ID associated with the QWeather credential.
      This value is used as the ``sub`` (subject) claim in the JWT payload.

    - ``kid``:
      The Credential ID that identifies the signing key.
      This value is included as the ``kid`` field in the JWT header.

    - ``alg``:
      The JWT signing algorithm. QWeather requires the EdDSA algorithm.

    - ``private_key``:
      The EdDSA private key used to sign the JWT.
      The PEM header and footer will be stripped automatically during initialization.

    All values related to the Project ID and Credential ID can be obtained from
    the QWeather Console under Project Management:
    https://console.qweather.com/project
    """

    api_host: AnyHttpUrl | str = Field(
        ...,
        description=(
            "Developer-specific API host provided by QWeather. "
            "This host is unique per account and replaces the public API endpoint. "
            "It is part of the authentication mechanism: requests will be rejected "
            "even with valid credentials if the API Host is incorrect. "
            "You can find your API Host in the QWeather Console under Settings. "
            "Example: https://abc1234xyz.def.qweatherapi.com"
        ),
    )

    project_id: str = Field(
        ...,
        description=(
            "Project ID of the QWeather credential. "
            "This value is used as the `sub` (subject) claim in the JWT payload. "
            "You can find the Project ID in the QWeather Console under Project Management: "
            "https://console.qweather.com/project"
        ),
    )

    kid: str = Field(
        ...,
        description=(
            "Credential ID used to identify the signing key. "
            "This value is set as the `kid` field in the JWT header. "
            "You can find the Credential ID in the QWeather Console under Project Management: "
            "https://console.qweather.com/project"
        ),
    )

    alg: Optional[Literal["EdDSA"]] = Field(
        "EdDSA",
        description=("JWT signing algorithm. QWeather requires the EdDSA algorithm."),
    )

    private_key: str = Field(
        ...,
        description=(
            "EdDSA private key in PEM format used to sign the JWT. "
            "Header and footer markers will be stripped automatically."
        ),
    )
