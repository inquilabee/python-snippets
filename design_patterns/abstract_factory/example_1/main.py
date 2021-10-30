from application import Application
from gui_factory import WinFactory, MacFactory

if __name__ == '__main__':
    config = {
        "os": "Mac"
    }

    if config["os"] == "Mac":
        factory = MacFactory()
    elif config["os"] == "Win":
        factory = WinFactory()
    else:
        raise ValueError("Unsupported Platform")

    app = Application(factory)
    app.create_ui()
    print(app.paint())
