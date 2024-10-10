class Window:
    def on_click(self):
        print("On Click")


class PMWindow(Window):
    def create_scrollbar(self):
        print("PM Scrollbar created")

    def create_window(self):
        print("PM Window created")


class MotifWindow(Window):
    def create_scrollbar(self):
        print("Motif Scrollbar created")

    def create_window(self):
        print("Motif window created")


class Scrollbar:
    pass


class PMScrollBar(Scrollbar):
    pass


class MotifScrollBar(Scrollbar):
    pass


class WidgetFactory:
    def create_scrollbar(self):
        self.create_scrollbar()

    def create_window(self):
        self.create_window()


class MotifWidgetFactory(WidgetFactory):
    def __init__(self):
        self._window = MotifWindow()

    def create_window(self):
        self._window.create_window()

    def create_scrollbar(self):
        self._window.create_window()

    def on_click(self):
        self._window.on_click()


class PMWidgetSFactory(WidgetFactory):
    def __init__(self):
        self._window = PMWindow()

    def create_window(self):
        self._window.create_window()

    def create_scrollbar(self):
        self._window.create_scrollbar()

    def on_click(self):
        self._window.on_click()


def client(window):
    _window = window.create_window()
    _scrollbar = window.create_scrollbar()
    window.on_click()


if __name__ == "__main__":
    pmWindow = PMWidgetSFactory()
    client(pmWindow)

    motifWindow = MotifWidgetFactory()
    client(motifWindow)