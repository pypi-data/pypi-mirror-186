import pytest

from barbuilder import Menu


def test_render():
    m = Menu()
    m.add_item('option 1')
    m.add_header('title')
    i = m.add_item('option 2', color='green')
    i.add_item('suboption1', sfimage='calendar')
    i.set_alternate('alt')
    out = str(m)
    assert out == """\
title
---
option 1
option 2 | color="green"
--suboption1 | sfimage="calendar"
alt | alternate="True"
""".strip()

