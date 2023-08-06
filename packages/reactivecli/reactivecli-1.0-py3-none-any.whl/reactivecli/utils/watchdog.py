import os
import time
import traceback
import threading
from importlib import reload, import_module

from reactivecli.utils.text_formatter import error


class Watcher:

    def __init__(self, target, on_change):
        self._private_target_name = target.__name__

        try:
            self._private_target_module = import_module(target.__module__)
            self.target_callback = self._private_target_module.__getattribute__(
                self._private_target_name)
        except Exception as e:
            error_label = str(e).replace(
                f"{self._private_target_file_name}, ", f"{self._private_target_path}, ")
            print(error(error_label))

        module_dirs = target.__module__.split(".")
        self.target_module_path = f"./{'/'.join(module_dirs)}"

        if module_dirs.__contains__(self._private_target_name):
            self._private_target_file_name = f"{self._private_target_name}.py"
            self._private_target_path = f"./{'/'.join(module_dirs)}.py"
        else:
            self._private_target_path = f"./{'/'.join(module_dirs)}/__init__.py"
            self._private_target_file_name = "__init__.py"

        self._private_target_file = os.path.getmtime(self._private_target_path)
        self._private_watching = True

        self.on_change = on_change

    def _private_module_reload(self):
        try:
            self._private_target_module = reload(self._private_target_module)
            self.target_callback = self._private_target_module.__getattribute__(
                self._private_target_name)
            self.on_change()
        except Exception as e:
            error_label = str(e).replace(
                f"{self._private_target_file_name}, ", f"{self._private_target_path}, ")
            print(error(error_label))

    def start(self):
        t = threading.Thread(
            target=self._private_wait_changes, args=(), daemon=True)
        t.start()

    def stop(self):
        self._private_watching = False

    def _private_wait_changes(self):
        try:
            while self._private_watching:
                time.sleep(0.5)
                current_file = os.path.getmtime(self._private_target_path)
                if current_file != self._private_target_file:
                    self._private_target_file = current_file
                    self._private_module_reload()
        except:
            print(traceback.format_exc())
