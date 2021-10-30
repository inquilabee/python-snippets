from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self): pass

    @abstractmethod
    def on_click(self, f): pass

    @abstractmethod
    def click(self): pass


class WindowsButton(Button):
    def __init__(self):
        self.on_click_function = None

    def render(self):
        return "Windows Button"

    def on_click(self, f):
        self.on_click_function = f

    def click(self):
        self.on_click_function()


class HTMLButton(Button):
    def __init__(self):
        self.on_click_function = None

    def render(self):
        return "HTML Button"

    def on_click(self, f):
        self.on_click_function = f

    def click(self):
        self.on_click_function()
