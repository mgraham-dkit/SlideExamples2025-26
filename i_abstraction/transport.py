from abc import ABC, abstractmethod


'''
Example of defining an interface to standardise common abilities, 
plus two classes that implement it
'''
class Drivable(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass

    @abstractmethod
    def stop_engine(self) -> str:
        pass


class Car(Drivable):
    def start_engine(self) -> str:
        return "Car engine started"

    def stop_engine(self) -> str:
        return "Car engine stopped"


class MotorBike(Drivable):
    def start_engine(self) -> str:
        return "Bike engine started"

    def stop_engine(self) -> str:
        return "Bike engine stopped"


if __name__ == "__main__":
    # Create objects - these are their own type (but can be treated as the interface type
    # as they inherit from that type)
    car = Car()
    bike = MotorBike()

    # Can define the list as holding drivable things
    # this will mean the only requirement is that all objects inside it
    # must implement the Drivable interface
    # i.e. inherit from that abstract class and provide code for its methods
    garage: list[Drivable] = [car, bike]
    print("Start your engines!")
    for brum_brum in garage:
        print(f"Starting engine: {brum_brum.start_engine()}")

    print()
    print("Race over - engine shutdown required.")
    for brum_brum in garage:
        print(f"Stopping engine: {brum_brum.stop_engine()}")