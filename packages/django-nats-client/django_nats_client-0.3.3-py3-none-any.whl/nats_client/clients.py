import asyncio
import json

from django.conf import settings
from nats.aio.client import Client

from .types import ResponseType
from .utils import parse_arguments


async def request_async(subject_name: str, method_name: str, *args, **kwargs) -> ResponseType:
    payload = parse_arguments(method_name, args, kwargs)

    nc = Client()
    await nc.connect(**settings.NATS_OPTIONS)

    try:
        response = await nc.request(subject_name, payload)
    finally:
        await nc.close()

    data = response.data.decode()
    return json.loads(data)['result']


async def send_async(subject_name: str, method_name: str, *args, **kwargs) -> None:
    payload = parse_arguments(method_name, args, kwargs)

    nc = Client()
    await nc.connect(**settings.NATS_OPTIONS)

    try:
        await nc.publish(subject_name, payload)
    finally:
        await nc.close()


def request(*args, **kwargs):
    return asyncio.run(request_async(*args, **kwargs))


def send(*args, **kwargs):
    return asyncio.run(send_async(*args, **kwargs))
