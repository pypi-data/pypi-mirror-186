import asyncio
import datetime
import http
import logging
import typing
from contextlib import asynccontextmanager
from http.client import HTTPException

import aiohttp
import munch
from pypasser import reCaptchaV3

from tami4edge_api_client import model

BASE_URL = 'https://swelcustomers.strauss-water.com'
GENERATE_OTP = f'{BASE_URL}/public/phone/generateOTP'
SUBMIT_OTP = f'{BASE_URL}/public/phone/submitOTP'
API_V1_URL = f'{BASE_URL}/api/v1'
TOKEN_REFRESH_URL = f'{BASE_URL}/public/token/refresh'
GET_DEVICES_URL = f'{API_V1_URL}/device'
ANCHOR_URL = "https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lf-jYgUAAAAAEQiRRXezC9dfIQoxofIhqBnGisq&co=aHR0cHM6Ly93d3cudGFtaTQuY28uaWw6NDQz&hl=en&v=gWN_U6xTIPevg0vuq7g1hct0&size=invisible&cb=ji0lh9higcza"

_LOGGER = logging.getLogger(__name__)


class Tami4Client:
    def __init__(self, token: str = ''):
        """
        :param token: the permanent token obtained through the out-of-band authentication (phone/OTP)
        """
        # The permanent token is initially used as a refresh token
        self.token_info = model.TokenInfo(
            access_token='',
            refresh_token=token,
            expires_in=0,
        )

        self.token_expiration = datetime.datetime.now() + datetime.timedelta(seconds=self.token_info.expires_in)

        self.session = None
        self.devices: typing.Dict[str, model.Device] = dict()

    async def _authenticate(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    TOKEN_REFRESH_URL,
                    headers={'Content-Type': 'application/json'},
                    json=dict(token=self.token_info.refresh_token),
            ) as resp:
                if resp.status != http.HTTPStatus.OK:
                    text = await resp.text()
                    raise HTTPException(text)
                self.token_info = model.TokenInfo(**(await resp.json()))
                self.token_expiration = datetime.datetime.now() + datetime.timedelta(seconds=self.token_info.expires_in)
                _LOGGER.warning(f'Token refreshed; valid until {self.token_expiration}')

    @asynccontextmanager
    async def get_session(self):
        if self.token_expiration <= datetime.datetime.now():
            # If we know token is expired, try to refresh it
            await self._authenticate()

        # Create a session with the fresh access token
        session = aiohttp.ClientSession(headers={'Authorization': f'Bearer {self.token_info.access_token}'})
        try:
            yield session
        finally:
            await session.close()

    async def get_devices(self):
        async with self.get_session() as session:
            async with session.get(GET_DEVICES_URL) as resp:
                if resp.status == http.HTTPStatus.OK:
                    data = munch.munchify(await resp.json())
                    self.devices = {device.id: model.Device(**device)
                                    for device in data}
                else:
                    _LOGGER.warning(f'get_devices failed: {resp.status}')

    async def get_configuration(self, device_id: str):
        async with self.get_session() as session:
            async with session.get(f'{GET_DEVICES_URL}/{device_id}/configuration') as resp:
                data = await resp.json()
                device = self.devices.get(device_id)
                device.configuration = model.DeviceConfiguration(**data)

    async def get_drinks(self, device_id: str):
        async with self.get_session() as session:
            async with session.get(f'{GET_DEVICES_URL}/{device_id}/drink') as resp:
                data = munch.munchify(await resp.json())
                device = self.devices.get(device_id)
                device.drinks = [model.Drink(**row) for row in data.drinks]

    async def get_filter_info(self, device_id: str):
        async with self.get_session() as session:
            async with session.get(f'{GET_DEVICES_URL}/{device_id}/filter') as resp:
                data = await resp.json()
                device = self.devices.get(device_id)
                device.filter_info = model.FilterInfo(**data)

    async def get_uv_info(self, device_id: str):
        async with self.get_session() as session:
            async with session.get(f'{GET_DEVICES_URL}/{device_id}/uv') as resp:
                data = await resp.json()
                device = self.devices.get(device_id)
                device.uv_info = model.UVInfo(**data)

    async def start_boiling(self, device_id: str):
        async with self.get_session() as session:
            async with session.post(f'{GET_DEVICES_URL}/{device_id}/startBoiling') as resp:
                if resp.status == http.HTTPStatus.BAD_GATEWAY:
                    _LOGGER.debug('Already boiling!')
                elif resp.status != http.HTTPStatus.OK:
                    text = await resp.text()
                    _LOGGER.warning(text)
                    raise HTTPException(text)
                else:
                    pass

    async def set_configuration(
        self,
        device_id: str,
        device_configuration: model.DeviceConfiguration,
    ):
        config = device_configuration.dict(
            exclude_none=True,
            by_alias=True,
        )
        _LOGGER.debug(f'Configuring {device_id}: {config}')
        async with self.get_session() as session:
            async with session.post(f'{GET_DEVICES_URL}/{device_id}/configuration', json=config) as resp:
                if resp.status != http.HTTPStatus.OK:
                    text = await resp.text()
                    raise HTTPException(text)
                else:
                    _LOGGER.debug(f'{device_id} configured successfully ')

    @staticmethod
    def _get_recaptcha_token() -> reCaptchaV3:
        return reCaptchaV3(ANCHOR_URL)

    @staticmethod
    def async_add_executor_job(target: typing.Callable, *args: typing.Any) -> asyncio.Future:
        """Add an executor job from within the event loop."""
        loop = asyncio.get_running_loop()
        task = loop.run_in_executor(None, target, *args)

        return task

    async def request_one_time_password(self, phone_number: str) -> None:
        token = await self.async_add_executor_job(self._get_recaptcha_token)
        form = model.OneTimePasswordForm(phoneNumber=phone_number, reCaptchaToken=token)

        # This is pre-auth, so we don't want the authenticated session
        async with aiohttp.ClientSession() as session:
            async with session.post(GENERATE_OTP, json=form.dict(exclude_none=True)) as resp:
                if resp.status != http.HTTPStatus.OK:
                    _LOGGER.warning(f'Could not generate OTP for {phone_number}: {resp.status}')
                    raise HTTPException()
                else:
                    _LOGGER.debug(f'OTP generated successfully ')

    async def submit_one_time_password(self, phone_number: str, otp: int) -> str:
        token = await self.async_add_executor_job(self._get_recaptcha_token)
        form = model.OneTimePasswordForm(phoneNumber=phone_number, reCaptchaToken=token, code=otp)

        # This is pre-auth, so we don't want the authenticated session
        async with aiohttp.ClientSession() as session:
            async with session.post(SUBMIT_OTP, json=form.dict(exclude_none=True)) as resp:
                if resp.status != http.HTTPStatus.OK:
                    _LOGGER.warning(f'Could not submit OTP for {phone_number}: {resp.status}')
                    raise HTTPException()

                json = await resp.json()
                return json['refresh_token']
