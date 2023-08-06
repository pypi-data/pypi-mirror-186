import os
from reactivecli.utils import Watcher, color, background, error
from sshkeyboard import listen_keyboard, stop_listening


class Menu:

    def __init__(self, menu, dev):

        if dev:
            self.watcher = Watcher(menu, lambda: self._private_menu_reload())
            self.watcher.start()
            self.menu = self.watcher.target_callback
        else:
            self.menu = menu

        self.dev = dev

        self._private_actions_index = {}
        self._private_elements = {}
        self._private_hover_index = 0
        self._private_error = ""
        self._private_leave = False
        self._private_paused = False
        self._private_key = None

    def _private_menu_reload(self):
        self.menu = self.watcher.target_callback
        self._private_update()

    def set_key(self, key):
        self._private_key = key
        stop_listening()

    def render(self):
        for index, element in enumerate(self.menu()):
            element._private_id = index
            self._private_elements[index] = element
            element.parent = self
            if element._private_action != None:
                count = len(self._private_actions_index.keys())
                self._private_actions_index[count] = {'id': index}
                element._private_action_index = count
            self.__render__(False)
        while not self._private_leave:
            listen_keyboard(on_press=self.set_key)
            self._private_handle_key()
            while self._private_paused:
                pass
            self.__render__(False)

    def _private_update(self, keep_hover=False):
        self._private_actions_index = {}
        self._private_elements = {}
        if not keep_hover:
            self._private_hover_index = 0

        for index, element in enumerate(self.menu()):
            element._private_id = index
            self._private_elements[index] = element
            element.parent = self
            if element._private_action != None:
                count = len(self._private_actions_index.keys())
                self._private_actions_index[count] = {'id': index}
                element._private_action_index = count

        self.__render__(False)

    def __render__(self, force):
        if not self._private_paused and not self._private_leave or force:
            os.system('clear' if os.name == 'posix' else 'cls')
            for key in self._private_elements.keys():
                if self._private_elements[
                        key]._private_action_index == self._private_hover_index:
                    if os.name == 'posix':
                        linux_terminal = os.popen('ls -l /proc/$$/exe').read()
                        text = ""
                    else:
                        text = background(
                            color(self._private_elements[key]._private_renderer, 'black'), "white")
                    print(text)
                else:
                    print(self._private_elements[key]._private_renderer)

            print(background(color("\n Press E to Exit ", 'white'), 'blue'))
            print(f"\n{error(self._private_error)}")

    def _private_handle_key(self):

        if self._private_key == 'up':
            self._private_up()
        elif self._private_key == 'down':
            self._private_down()
        elif self._private_key == 'enter':
            self._private_call_action()
        elif self._private_key == 'e':
            self.exit()

    def _private_up(self):
        if self._private_hover_index > 0:
            self._private_hover_index -= 1
        self._private_key = None

    def _private_down(self):
        if self._private_hover_index < len(self._private_actions_index.keys()) - 1:
            self._private_hover_index += 1
        self._private_key = None

    def _private_call_action(self):
        self._private_paused = True
        stop_listening()
        try:
            element_id = self._private_actions_index[self._private_hover_index]['id']
            self._private_elements[element_id]._private_action()
            self._private_error = ""
            self._private_update(True)
        except Exception as e:
            if str(e) == "0":
                self._private_error = ""
            else:
                self._private_error = "Error on callback: " + str(e)
        self._private_paused = False
        self._private_key = None

    def exit(self):
        self.watcher.stop()
        self._private_leave = True
        stop_listening()
