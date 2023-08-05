from typing import Iterator

from .base import BaseItem, BaseItemContainer, ItemParams
from .items import HeaderItem, HeaderItemContainer, MenuItem


class Menu(BaseItemContainer[MenuItem]):
    def __init__(self, title: str | None = None, streamable: bool = False,
                 **params: ItemParams) -> None:
        super().__init__()
        self.streamable = streamable
        self._headers = HeaderItemContainer()
        if title:
            self.add_header(title, **params)

    def add_header(self, title: str, **params: ItemParams) -> HeaderItem:
        return self._headers._item_factory(HeaderItem, title, **params)

    def add_item(self, title: str, **params: ItemParams) -> MenuItem:
        return self._item_factory(MenuItem, title, **params)

    def add_divider(self):
        return self.add_item('---')

    def __str__(self) -> str:
        lines = []
        for header in self._headers:
            lines.append(str(header))
        if self:
            lines.append('---')
        for item in self:
            lines.append(str(item))
        return '\n'.join(lines)

    @property
    def header(self) -> HeaderItem | None:
        if self._headers:
            return self._headers[0]
        return None
