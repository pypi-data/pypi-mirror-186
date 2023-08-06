from reactivecli.bases import Element


class Title(Element):

    def __init__(self, state, style={}):
        super().__init__(state, style)
        self._private_renderer = "####$$$####\n####@@@####\n####$$$####\n".replace(
            '@@@', f" {state} ").replace('$$$', "#" * (len(state) + 2))
        self._private_format_renderer = self._private_formatter

    def _private_formatter(self):
        self._private_renderer = "####$$$####\n####@@@####\n####$$$####\n".replace(
            '@@@', f" {self.state} ").replace('$$$', "#" * (len(self.state) + 2))
