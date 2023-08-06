import subprocess
from urllib.parse import urlencode

from .base import PLUGIN_PATH


def open_callback_url(scheme: str, path: str, **params: str | int | None) -> None:
    clean_params = urlencode({k:v for k,v in params.items() if v is not None})
    url = f'{scheme}://{path}?{clean_params}'
    cmd = ['open', '-g', url]
    subprocess.run(cmd, capture_output=True, check=True)


def refreshplugin() -> None:
    open_callback_url('swiftbar', 'refreshplugin', name=PLUGIN_PATH.name)


def refreshallplugins() -> None:
    open_callback_url('swiftbar', 'refreshallplugins')


def enableplugin() -> None:
    open_callback_url('swiftbar', 'enableplugin', name=PLUGIN_PATH.name)


def disableplugin() -> None:
    open_callback_url('swiftbar', 'disableplugin', name=PLUGIN_PATH.name)


def toggleplugin() -> None:
    open_callback_url('swiftbar', 'toggleplugin', name=PLUGIN_PATH.name)


def notify(**params: str | int | None) -> None:
    open_callback_url('swiftbar', 'notify', name=PLUGIN_PATH.name, **params)
