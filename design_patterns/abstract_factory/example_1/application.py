from gui_factory import GUIFactory
from button import Button
from checkbox import CheckBox


class Application:
    def __init__(self, factory: GUIFactory):
        self.__factory = factory
        self.button: Button = None
        self.checkbox: CheckBox = None

    def create_ui(self):
        self.button = self.__factory.create_button()
        self.checkbox = self.__factory.create_checkbox()

    def paint(self):
        return self.button.paint(), self.checkbox.paint()
