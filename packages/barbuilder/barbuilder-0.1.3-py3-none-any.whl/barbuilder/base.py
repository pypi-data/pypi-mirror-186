from __future__ import annotations

import os
from collections.abc import MutableSequence
from pathlib import Path
from shlex import quote
from typing import Any, Iterable, Iterator, overload

PLUGIN_PATH = Path(os.environ.get('SWIFTBAR_PLUGIN_PATH', '.'))

ItemParams = str | int | bool
ItemParamsDict = dict[str, ItemParams]


class Item:
    title: str = ''

    def __str__(self):
        return self.title


class ConfigurableItem(Item):

    def __init__(self, title: str, **params: ItemParams) -> None:
        super().__init__()
        self.title = title
        self._alternate: Item | None = None
        self.params = params

    def __setattr__(self, name: str, value: Any) -> None:
        excluded_names = ['params', *dir(self)]
        if 'params' in self.__dict__ and name not in excluded_names:
            self.params[name] = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name: str) -> Any:
        if 'params' in self.__dict__ and name in self.params:
            return self.params[name]
        try:
            return self.__dict__[name]
        except KeyError as exc:
            raise NameError(f'name {name} is not defined.') from exc

    def __str__(self) -> str:
        if not self.params:
            return self.title
        title = self.title.replace(chr(124), chr(9474)) # melonamin is a smartass
        params = ' '.join([f'{k}={quote(str(v))}' for k,v in self.params.items()])
        return f'{title} | {params}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.title}")'

    def set_alternate(self, title: str, **params: ItemParams) -> Item:
        cls = self.__class__
        params['alternate'] = True
        self._alternate = cls(title, **params)
        return self._alternate


class ItemContainer(MutableSequence[Item]):

    def __init__(self) -> None:
        self._children: list[Item] = []

    @overload
    def __getitem__(self, index: int) -> Item:
        ...
    @overload
    def __getitem__(self, index: slice) -> list[Item]:
        ...
    def __getitem__(self, index: int | slice) -> Item | list[Item]:
        return self._children[index]

    @overload
    def __setitem__(self, index: int, item: Item) -> None:
        ...
    @overload
    def __setitem__(self, index: slice, item: Iterable[Item]) -> None:
        ...
    def __setitem__(self, index: int | slice, item: Item | Iterable[Item]) -> None:
        if isinstance(index, int) and not isinstance(item, Iterable):
            self._children[index] = item
        elif isinstance(index, slice) and isinstance(item, Iterable):
            self._children[index] = item
        else:
            raise TypeError(f"{index}/{item} Invalid index/item type.")

    def __delitem__(self, index: int | slice) -> None:
        del self._children[index]

    def __len__(self) -> int:
        return len(self._children)

    def __iter__(self) -> Iterator[Item]:
        return iter(self._children)

    def __bool__(self) -> bool:
        return bool(self._children)

    def __repr__(self) -> str:
        children = ", ".join(repr(i) for i in self)
        return f'{self.__class__.__name__}({children})'

    def append(self, value: Item) -> None:
        self._children.append(value)

    def insert(self, index: int, value: Item) -> None:
        self._children.insert(index, value)

    def _item_factory(self, cls: type[Item], title: str | None = None,
                      **params: ItemParams) -> Item:
        if not issubclass(cls, ConfigurableItem):
            item = cls()
        elif title is None:
            raise TypeError(f'Type "{cls}" requires a title')
        else:
            item = cls(title, **params)
        self.append(item)
        return item
