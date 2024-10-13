class SingletonClass(object):
    def __init__(self, data=None):
        if data:
            self._data = data

    def __new__(cls, data=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

    def init(self, data):
        self._data = data

    def __str__(self):
        return f"Data: {self._data}"


if __name__ == "__main__":
    x = SingletonClass(20)
    y = SingletonClass()

    if x is y:
        print("Same object")

    print(x)
    print(y)
