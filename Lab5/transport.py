import abc


class Transport:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._cost = 0
        self._velocity = 0.0
        self._year_of_production = 0
        self._coordinateX = 0.0
        self._coordinateY = 0.0

    @property
    def coordinateX(self):
        return self._coordinateX

    @property
    def coordinateY(self):
        return self._coordinateY

    @property
    def cost(self):
        return self._cost

    @property
    def velocity(self):
        return self._velocity

    @property
    def year_of_production(self):
        return self._year_of_production

    @coordinateX.setter
    def coordinateX(self, x):
        self._coordinateX_setter(x)

    @abc.abstractmethod
    def _coordinateX_setter(self, val):
        self._coordinateX = val

    @coordinateY.setter
    def coordinateY(self, x):
        self._coordinateY_setter(x)

    @abc.abstractmethod
    def _coordinateY_setter(self, val):
        self._coordinateY = val

    @cost.setter
    def cost(self, x):
        self._cost_setter(x)

    @abc.abstractmethod
    def _cost_setter(self, val):
        self._cost = val

    @velocity.setter
    def velocity(self, x):
        self._velocity_setter(x)

    @abc.abstractmethod
    def _velocity_setter(self, val):
        self._velocity = val

    @year_of_production.setter
    def year_of_production(self, x):
        self._year_of_production_setter(x)

    @abc.abstractmethod
    def _year_of_production_setter(self, val):
        self._year_of_production = val

    def __str__(self) -> str:
        return f"Cost: {self._cost} Velocity: {self._velocity} Year: {self._year_of_production} Coordinate x: {self._coordinateX} Coordinate y: {self._coordinateY}"


class Car(Transport):

    def _cost_setter(self, val):
        self._cost = val

    def _velocity_setter(self, val):
        self._velocity = val

    def _year_of_production_setter(self, val):
        self._year_of_production = val

    def _coordinateX_setter(self, y):
        self._coordinateY = y

    def _coordinateY_setter(self, x):
        self._coordinateX = x


class Plane(Transport):

    def __init__(self):
        super().__init__()
        self._height = 0
        self._amount_of_passengers = 0

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val

    @property
    def amount_of_passengers(self):
        return self._amount_of_passengers

    @amount_of_passengers.setter
    def amount_of_passengers(self, val):
        self._amount_of_passengers = val

    def __str__(self) -> str:
        return super().__str__() + f" Height: {self.height} Amount of passengers: {self.amount_of_passengers}"


class Ship(Transport):

    def __init__(self):
        super().__init__()
        self._port_id = 0
        self._amount_of_passengers = 0

    @property
    def port_id(self):
        return self._port_id

    @port_id.setter
    def port_id(self, val):
        self._port_id = val

    @property
    def amount_of_passengers(self):
        return self._amount_of_passengers

    @amount_of_passengers.setter
    def amount_of_passengers(self, val):
        self._amount_of_passengers = val

    def __str__(self) -> str:
        return super().__str__() + f" Port Id: {self.port_id} Amount of passengers: {self.amount_of_passengers}"


car = Car()

car.cost = 1000
car.velocity = 200
car.year_of_production = 1992
car.coordinateX = 33.4
car.coordinateY = 38.4

print(car)

plane = Plane()

plane.cost = 10000000
plane.velocity = 2000
plane.year_of_production = 1982
plane.coordinateX = 12.4
plane.coordinateY = 55.4
plane.amount_of_passengers = 300
plane.height = 448

print(plane)

ship = Ship()

ship.cost = 2500000
ship.velocity = 800
ship.year_of_production = 2016
ship.coordinateX = 44.4
ship.coordinateY = 87.4
ship.port_id = 123
ship.amount_of_passengers = 899

print(ship)
