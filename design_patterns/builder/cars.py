class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_body()
        self._builder.build_engine()
        self._builder.build_tires()

    def get_car(self):
        return self._builder.get_car()


class CarBuilder:
    def __init__(self):
        self._car = None

    def build_body(self):
        pass

    def build_engine(self):
        pass

    def build_tires(self):
        pass

    def get_car(self):
        return self._car


class Car:
    def __init__(self, car_type):
        self.car_type = car_type
        self.body = None
        self.engine = None
        self.tires = None

    def __str__(self):
        return f"{self.car_type} | Body: {self.body} | Engine: {self.engine} | Tires: {self.tires}"


class SedanBuilder(CarBuilder):
    def __init__(self):
        super().__init__()
        self._car = Car('Sedan')

    def build_body(self):
        self._car.body = 'Sedan body'

    def build_engine(self):
        self._car.engine = 'Sedan engine'

    def build_tires(self):
        self._car.tires = 'Sedan tires'


class PorscheBuilder(CarBuilder):
    def __init__(self):
        super().__init__()
        self._car = Car('Porsche')

    def build_body(self):
        self._car.body = 'Porsche body'

    def build_engine(self):
        self._car.engine = 'Porsche engine'

    def build_tires(self):
        self._car.tires = 'Porsche tires'


if __name__ == "__main__":
    sedan_builder = SedanBuilder()
    director = Director(sedan_builder)
    director.construct()
    sedaan_car = director.get_car()

    Porsche_builder = PorscheBuilder()
    director = Director(Porsche_builder)
    director.construct()
    porsche_car = director.get_car()

    print(sedaan_car)
    print(porsche_car)

