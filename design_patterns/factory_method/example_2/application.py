import sys
from dialog import Dialog, WindowsDialog, WebDialog


class Application:
    dialog: Dialog

    def __init__(self):
        if sys.platform.lower().startswith("win"):
            self.__class__.dialog = WindowsDialog()
        elif sys.platform.lower().startswith("dar"):
            self.__class__.dialog = WebDialog()
        else:
            raise Exception("Platform not supported")

    def start(self):
        self.dialog.render()
