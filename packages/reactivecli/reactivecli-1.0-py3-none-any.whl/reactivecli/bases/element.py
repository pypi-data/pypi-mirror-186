from reactivecli.components import Menu


class Element:

    def __init__(self, default_state="", style={}):

        self.__type__ = type

        self.style = style

        self._state = default_state

        self._private_on_change = lambda: ()
        self._private_format_renderer = self._private_default_formatter

        self._private_id = None
        self.parent = Menu(lambda: [], False)
        self._private_action = None
        self._private_action_index = None
        self.__private_renderer = default_state

    def _private_default_formatter(self):
        self._private_renderer = self._state

    @property
    def _private_renderer(self):
        return self.__private_renderer

    @_private_renderer.setter
    def _private_renderer(self, value):
        self.__private_renderer = value
        if self.parent != None:
            self.parent.__render__(True)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self.updated = True
        self._state = value
        self._private_format_renderer()
        self._private_on_change()

    @property
    def on_change(self):
        return self._private_on_change

    @on_change.setter
    def on_change(self, value):
        self._private_on_change = value
        if self.parent != None:
            self.parent.__render__(True)
