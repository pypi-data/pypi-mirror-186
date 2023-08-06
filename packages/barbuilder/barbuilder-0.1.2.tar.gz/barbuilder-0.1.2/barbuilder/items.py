from __future__ import annotations

from textwrap import indent

from .base import BaseItem, BaseItemContainer


class HeaderItem(BaseItem):
    pass

class HeaderItemContainer(BaseItemContainer[HeaderItem]):
    pass

class MenuItem(BaseItem, BaseItemContainer['MenuItem']):

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

    def add_divider(self) -> MenuItem:
        return self.add_item('---')
