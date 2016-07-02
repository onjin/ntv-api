import morepath


class App(morepath.App):
    pass


def make_app():
    morepath.autoscan()
    App.commit()
    return App()
