from reactivecli.bases import Element


class Option(Element):

    def __init__(self, state, action, style={}):
        super().__init__(state, style)
        self._private_renderer = f" - {state} "
        self._private_format_renderer = self._private_formatter
        self._private_action = action

    def _private_formatter(self):
        self._private_renderer = f" - {self.state} "
