from dataclasses import dataclass


@dataclass
class UserContext:
    location: str


@dataclass
class ResponseFormat:
    summary: str
    temperature_celcius: str
    humidity: str
    wind: str