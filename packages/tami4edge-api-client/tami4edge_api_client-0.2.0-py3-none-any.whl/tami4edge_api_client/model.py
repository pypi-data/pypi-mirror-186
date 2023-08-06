import typing

import pydantic
from humps.main import camelize


def to_camel(string: str) -> str:
    return camelize(string)


class BaseModel(pydantic.BaseModel):
    class Config:
        alias_generator = to_camel


class TokenInfo(pydantic.BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int


class DeviceConfigurationProperties(BaseModel):
    wifi_name: typing.Optional[str]
    connectivity_enabled: typing.Optional[bool]
    boiling_temp: typing.Optional[float]
    child_lock: typing.Optional[bool]
    buttons_sound: typing.Optional[bool]
    energy_save_mode: typing.Optional[bool]


class DeviceConfiguration(BaseModel):
    id: str
    configuration_properties: DeviceConfigurationProperties
    configuration_time: typing.Optional[int]


class FilterInfo(BaseModel):
    last_replacement: int
    upcoming_replacement: int
    status: str  # seen values: "replacementDateAsPassed",
    milli_litters_passed: int


class UVInfo(BaseModel):
    last_replacement: int
    upcoming_replacement: int
    status: str


class WaterQuality(BaseModel):
    filter_info: FilterInfo
    uv_info: UVInfo


class DrinkSettings(BaseModel):
    volume: int
    temperature: int
    carbonization_level: int


class Drink(BaseModel):
    id: str
    name: str
    settings: DrinkSettings
    vessel: str
    include_in_customer_statistics: bool
    default_drink: bool


class Device(BaseModel):
    id: str
    name: str
    connected: bool
    last_heartbeat: int
    psn: str
    type: str
    device_firmware: str

    configuration: typing.Optional[DeviceConfiguration] = None
    filter_info: typing.Optional[FilterInfo] = None
    uv_info: typing.Optional[UVInfo] = None
    drinks: typing.List[Drink] = None


class OneTimePasswordForm(pydantic.BaseModel):
    """Class for submitting the OTP"""
    phoneNumber: str
    reCaptchaToken: str
    code: typing.Optional[str] = None
