from __future__ import annotations

from textwrap import indent

from .base import ConfigurableItem, Item, ItemContainer, ItemParams


class Divider(Item):
    title = '---'


class Reset(Item):
    title = '~~~'


class HeaderItem(ConfigurableItem):
    pass


class HeaderItemContainer(ItemContainer):

    def add_item(self, title: str, **params: ItemParams) -> Item:
        return self._item_factory(HeaderItem, title, **params)


class MenuItem(ConfigurableItem, ItemContainer):

    def __str__(self) -> str:
        lines = [super().__str__()]
        for item in self:
            lines.append(indent(str(item), '--'))
        if self._alternate is not None:
            lines.append(str(self._alternate))
        return '\n'.join(lines)

    def __repr__(self) -> str:
        children = ", ".join(repr(i) for i in self)
        return f'{self.__class__.__name__}("{self.title}", [{children}])'

    def add_item(self, title: str, **params: ItemParams) -> Item:
        return self._item_factory(MenuItem, title, **params)

    def add_divider(self) -> Item:
        return self._item_factory(Divider)
