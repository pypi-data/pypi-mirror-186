from __future__ import annotations

import os
from collections.abc import MutableSequence
from pathlib import Path
from shlex import quote
from typing import Any, Iterable, Iterator, TypeVar, get_args, overload

PLUGIN_PATH = Path(os.environ.get('SWIFTBAR_PLUGIN_PATH', '.'))

ItemParams = str | int | bool
ItemParamsDict = dict[str, ItemParams]


class BaseItem:

    def __init__(self, title: str, **params: ItemParams) -> None:
        super().__init__()
        self.title = title
        self._alternate: BaseItem | None = None
        self._params = params

    def __setattr__(self, name: str, value: Any) -> None:
        excluded_names = ['_params', *dir(self)]
        if '_params' in self.__dict__ and name not in excluded_names:
            self._params[name] = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name: str) -> Any:
        if '_params' in self.__dict__ and name in self._params:
            return self._params[name]
        try:
            return self.__dict__[name]
        except KeyError as exc:
            raise NameError(f'name {name} is not defined.') from exc

    def __str__(self) -> str:
        if not self._params:
            return self.title
        title = self.title.replace(chr(124), chr(9474)) # melonamin is a smartass
        params = ' '.join([f'{k}={quote(str(v))}' for k,v in self._params.items()])
        return f'{title} | {params}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.title}")'

    @property
    def params(self) -> ItemParamsDict:
        return self._params

    def set_alternate(self, title: str, **params: ItemParams) -> BaseItem:
        cls = self.__class__
        params['alternate'] = True
        self._alternate = cls(title, **params)
        return self._alternate


T = TypeVar('T', bound=BaseItem)

class BaseItemContainer(MutableSequence[T]):

    def __init__(self) -> None:
        self._children: list[T] = []

    @overload
    def __getitem__(self, index: int) -> T:
        ...
    @overload
    def __getitem__(self, index: slice) -> list[T]:
        ...
    def __getitem__(self, index: int | slice) -> T | list[T]:
        return self._children[index]

    @overload
    def __setitem__(self, index: int, item: T) -> None:
        ...
    @overload
    def __setitem__(self, index: slice, item: Iterable[T]) -> None:
        ...
    def __setitem__(self, index: int | slice, item: T | Iterable[T]) -> None:
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

    def __iter__(self) -> Iterator[T]:
        return iter(self._children)

    def __bool__(self) -> bool:
        return bool(self._children)

    def __repr__(self) -> str:
        children = ", ".join(repr(i) for i in self)
        return f'{self.__class__.__name__}({children})'

    def append(self, value: T) -> None:
        self._children.append(value)

    def insert(self, index: int, value: T) -> None:
        self._children.insert(index, value)

    def add_item(self, title: str, **params: ItemParams) -> T:
        bases = getattr(self.__class__, '__orig_bases__')
        cls = None
        for base in bases:
            args = get_args(base)
            while args:
                if isinstance(args[0], str):
                    break
                cls = args[0]
                args = get_args(cls)
            if cls:
                break
        else:
            cls = self.__class__
        item = cls(title, **params)
        self.append(item)
        return item
