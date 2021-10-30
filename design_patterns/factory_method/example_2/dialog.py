from abc import ABC, abstractmethod
from button import Button, WindowsButton, HTMLButton


class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        ok_button = self.create_button()
        ok_button.on_click(lambda: print(f"{ok_button.__class__.__name__} Button was clicked"))
        print(ok_button.render())
        ok_button.click()


class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()
