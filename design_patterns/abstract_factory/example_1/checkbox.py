from abc import ABC, abstractmethod


class CheckBox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WinCheckBox(CheckBox):
    def paint(self):
        return "Windows CheckBox"


class MacCheckBox(CheckBox):
    def paint(self):
        return "Mac CheckBox"
