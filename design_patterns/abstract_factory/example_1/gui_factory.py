from abc import ABC, abstractmethod
from button import Button, WinButton, MacButton
from checkbox import CheckBox, WinCheckBox, MacCheckBox


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox: pass


class WinFactory(GUIFactory):

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckBox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckBox()
