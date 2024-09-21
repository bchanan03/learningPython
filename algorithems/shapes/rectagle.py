class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width must be positive")
        self._width = width

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height must be positive")
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __repr__(self):
        return f"Rectagle with width {self._width} and height {self._height}"

    def __str__(self):
        return f"Rectagle with width {self._width} and height {self._height}"

    def __eq__(self, other):
        return self._width == other.width and self._height == other.height

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False


