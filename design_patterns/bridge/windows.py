class Window:
    def __init(self):
        print("Window Super is running")
        self.imp = WindowImp()

    def draw_text(self):
        self.imp.draw_text()

    def draw_rect(self):
        self.imp.draw_line()
        self.imp.draw_line()
        self.imp.draw_line()
        self.imp.draw_line()


class WindowImp(Window):
    def __init__(self):
        print("WindowImp Super is running")
        self.super()

    def draw_line(self):
        pass

    def draw_text(self):
        pass


class XWindowImp(WindowImp):
    def __init(self):
        print("XWindowImp Super is running")
        self.super()

    def draw_text(self):
        print("XWindowImp draw text")

    def draw_line(self):
        print("XWindowImp draw line")


class PMWindowImp(WindowImp):
    def __init(self):
        print("PMWindowImp Super is running")
        self.super()

    def draw_text(self):
        print("PMWindowImp draw text")

    def draw_line(self):
        print("PMWindowImp draw line")


class IconWindow(Window):
    def __init(self):
        print("IconWindow Super is running")
        self.super()

    def draw_border(self):
        self.draw_rect()
        self.draw_text()


class TransientWindow(Window):
    def __init(self):
        print("TransientWindow Super is running")
        self.super()


    def draw_cloase_box(self):
        self.draw_rect()


if __name__ == "__main__":
    myIconWin = IconWindow()
    # myIconWin.draw_border()

    # myTransWin = TransientWindow()
    # myTransWin.draw_cloase_box()



