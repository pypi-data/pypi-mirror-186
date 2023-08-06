from typing import Iterator

from .base import BaseItemContainer, ItemParams, ItemParamsDict
from .items import HeaderItem, HeaderItemContainer, MenuItem


class Menu(BaseItemContainer[MenuItem | HeaderItem]):
    def __init__(self, title: str | None = None, streamable: bool = False,
                 **params: ItemParams) -> None:
        super().__init__()
        self.streamable = streamable
        self._headers = HeaderItemContainer()

        if title:
            self.add_header(title, **params)

    def __iter__(self) -> Iterator[MenuItem | HeaderItem]:
        yield from self._headers
        if self:
            yield MenuItem('---')
        yield from self._children

    def __str__(self) -> str:
        lines = []
        if self.streamable:
            lines.append('~~~')
        for item in self:
            lines.append(str(item))
        return '\n'.join(lines)

    @property
    def header(self) -> HeaderItem | None:
        if not self._headers:
            return None
        return self._headers[0]

    @property
    def title(self) -> str | None:
        if not self.header:
            return None
        return self.header.title

    @property
    def params(self) -> ItemParamsDict | None:
        if not self.header:
            return None
        return self.header.params

    def add_header(self, title: str, **params: ItemParams) -> HeaderItem:
        return self._headers.add_item(title, **params)

    def add_divider(self) -> MenuItem | HeaderItem:
        return self.add_item('---')
