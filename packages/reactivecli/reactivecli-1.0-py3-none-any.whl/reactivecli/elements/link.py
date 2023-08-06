from reactivecli.bases import Element
from reactivecli.components import Menu


class Link(Element):

    def __init__(self, state, action, style={}):
        super().__init__(state, style)
        self._private_renderer = f" - {state} "
        self._private_format_renderer = self._private_formatter
        self._private_action = lambda: self._private_create_menu(action)

    def _private_create_menu(self, action):
        menu = Menu(action, self.parent.dev)
        menu.render()

    def _private_formatter(self):
        self._private_renderer = f" - {self.state} "
