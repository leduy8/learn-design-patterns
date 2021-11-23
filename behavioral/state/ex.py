from abc import ABC, abstractmethod


class Mode(ABC):
    @abstractmethod
    def get_ETA(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass


class BicyclingMode(Mode):
    def get_ETA(self):
        print('ETA: 22m10s...')

    def get_direction(self):
        print('Go straight...')

    def __str__(self) -> str:
        return 'Bicycling Mode'


class WalkingMode(Mode):
    def get_ETA(self):
        print('ETA: 1h46m10s...')

    def get_direction(self):
        print('Go straight and turn left...')

    def __str__(self) -> str:
        return 'Walking Mode'


class DrivingMode(Mode):
    def get_ETA(self):
        print('ETA: 10m...')

    def get_direction(self):
        print('Go straight and turn right...')

    def __str__(self) -> str:
        return 'Driving Mode'


class DirectionService():
    def __init__(self) -> None:
        self.travel_mode = None

    def get_ETA(self):
        self.travel_mode.get_ETA()
    
    def get_direction(self):
        self.travel_mode.get_direction()

    def get_travel_mode(self):
        return self.travel_mode

    def set_travel_mode(self, mode):
        self.travel_mode = mode


ds = DirectionService()
ds.set_travel_mode(WalkingMode())
print(ds.get_travel_mode())
ds.get_ETA()
ds.get_direction()
ds.set_travel_mode(DrivingMode())
print(ds.get_travel_mode())
ds.get_ETA()
ds.get_direction()