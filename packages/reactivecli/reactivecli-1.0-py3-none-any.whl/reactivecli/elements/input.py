from reactivecli.bases import Element
from sshkeyboard import listen_keyboard, stop_listening
import ctypes
import re
import os


class Input(Element):

    def __init__(self, type="text", state="", style={}):

        self._private_type = type

        default_style = {
            "text_symbol": ".",
            "state_symbol": ":",
            "minus_symbol": "-",
            "plus_symbol": "+",
            "fill_symbol": "█",
            "empty_symbol": "░",
        }

        for key in style:
            try:
                default_style[key] = style[key]
            except:
                pass

        super().__init__(state, default_style)

        self._private_format_renderer = self._private_formatter
        self._private_action = self._private_edit
        self._private_renderer = f"> {self.state}"
        self._private_editing = False
        self._private_final_part = ""
        self._private_text_edit_index = 0

        self.capslock = self._private_check_capslock()

    def _private_check_capslock(self):
        if os.name == "posix":
            pass
        elif os.name == "windows":
            self.capslock = bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14))

    def _private_formatter(self):
        print(self.state)
        if self._private_editing:
            self._private_renderer = "> " + self.state + "█" + self._private_final_part
        else:
            self._private_renderer = "> " + self.state

    def _private_edit(self):
        self._private_editing = True
        self._private_formatter()
        self._private_text_edit_index = len(self._private_renderer) - 1
        while self._private_editing:
            listen_keyboard(on_press=self.set_key)
            self.handle_key()

    def set_key(self, key):
        self._private_check_capslock()
        self._private_key = key
        stop_listening()

    def handle_key(self):
        if self._private_key == 'left' and self._private_text_edit_index > 2:
            self._private_left()
        elif self._private_key == 'right' and self._private_text_edit_index < len(
                self._private_renderer) - 1:
            self._private_right()
        elif self._private_key == 'backspace' and self._private_text_edit_index > 2:
            self._private_backspace()
        elif self._private_key == 'enter':
            self._private_save()
        elif self._private_type == "value" and re.search("^[0-9.]$",
                                                         self._private_key):
            self._private_append_state(self._private_key)
        elif self._private_type == "text" and re.search(
                "^[a-zA-Z0-9\"'!@#$%&*()_+=[°:;.,?/\\|{\}ª\-\]]$", self._private_key):
            self._private_append_state(self._private_key)
        elif self._private_type == "text" and self._private_key == "space":
            self._private_append_state(" ")

    def _private_left(self):
        self._private_text_edit_index -= 1
        self._private_final_part = self.state[-1] + self._private_final_part
        self.state = self.state[:-1]

    def _private_right(self):
        self._private_text_edit_index += 1
        first_final_part_char = self._private_final_part[0]
        self._private_final_part = self._private_final_part[
            1:len(self._private_final_part)]
        self.state = self.state + first_final_part_char

    def _private_backspace(self):
        self.state = self.state[:-1]
        self._private_text_edit_index -= 1

    def _private_save(self):
        self._private_editing = False
        self.state = self.state + self._private_final_part
        self._private_text_edit_index = 0
        self._private_final_part = ''

    def _private_append_state(self, value):
        if self.capslock:
            value = value.upper()
        self.state = self.state + value
        self._private_text_edit_index += 1
