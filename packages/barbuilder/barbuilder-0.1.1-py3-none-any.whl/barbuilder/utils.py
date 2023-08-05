import subprocess
from urllib.parse import urlencode

from .base import PLUGIN_PATH


def open_callback_url(action: str, **params: str | int | None) -> None:
    scheme = 'swiftbar://'
    clean_params = urlencode({k:v for k,v in params.items() if v is not None})
    url = f'swiftbar://{action}?{clean_params}'
    print(action, params, url)
    cmd = ['open', '-g', url]
    subprocess.run(cmd, capture_output=True, check=True)


def refreshplugin() -> None:
    open_callback_url('refreshplugin', name=PLUGIN_PATH.name)


def refreshallplugins() -> None:
    open_callback_url('refreshallplugins')


def enableplugin() -> None:
    open_callback_url('enableplugin', name=PLUGIN_PATH.name)


def disableplugin() -> None:
    open_callback_url('disableplugin', name=PLUGIN_PATH.name)


def toggleplugin() -> None:
    open_callback_url('toggleplugin', name=PLUGIN_PATH.name)


def notify(**params: str | int | None) -> None:
    open_callback_url('notify', name=PLUGIN_PATH.name, **params)