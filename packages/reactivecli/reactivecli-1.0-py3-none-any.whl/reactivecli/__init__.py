from reactivecli.elements import (Option, Text, Title, Input, Link)
from reactivecli.bases import Element
from reactivecli.components import Menu
from reactivecli.utils import (color, background, decoration)


def create_root(callback, dev=False):
    menu = Menu(callback, dev)
    menu.render()


__all__ = [
    'Menu',
    'Option',
    'Text',
    'Title',
    'Input',
    'Link',
    'Element',
    'color',
    'background',
    'create_root'
]
