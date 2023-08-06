from typing import Iterator

from .base import Item, ItemContainer, ItemParams, ItemParamsDict
from .items import HeaderItem, HeaderItemContainer, MenuItem


class Menu(ItemContainer):
    def __init__(self, title: str | None = None, streamable: bool = False,
                 **params: ItemParams) -> None:
        super().__init__()
        self.streamable = streamable
        self._headers = HeaderItemContainer()

        if title:
            self.add_header(title, **params)

    def __iter__(self) -> Iterator[Item]:
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
    def header(self) -> Item | None:
        if not self._headers:
            return None
        return self._headers[0]

    @property
    def title(self) -> str | None:
        if self.header is None:
            return None
        return self.header.title

    @title.setter
    def title(self, value) -> None:
        if self.header is None:
            self.add_header(value)
        else:
            self.header.title = value

    @property
    def params(self) -> ItemParamsDict | None:
        if not isinstance(self.header, HeaderItem):
            return None
        return self.header.params

    def add_header(self, title: str, **params: ItemParams) -> Item:
        return self._headers.add_item(title, **params)

    def add_item(self, title: str, **params: ItemParams) -> Item:
        return self._item_factory(MenuItem, title, **params)

    def add_divider(self) -> Item:
        return self.add_item('---')
