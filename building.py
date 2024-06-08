from elevator import Elevator
from lift_floor_selection import LiftFloorSelection

# This class represents a building with 2 elevators.

class Building:
    def __init__(self):
        self.elevator1 = Elevator(name="Lift 1")  # Create first elevator
        self.elevator2 = Elevator(name="Lift 2")  # Create second elevator
        self.lift_console1 = LiftFloorSelection(self.elevator1)  # Create panel for first elevator
        self.lift_console2 = LiftFloorSelection(self.elevator2)  # Create panel for second elevator

    # Method to handle elevator requests
    def request_elevator(self, floor):
        #Load balancing based on the number of pending stops
        if len(self.elevator1.floors_to_visit) <= len(self.elevator2.floors_to_visit):
            self.lift_console1.request_button_pressed(floor)  # Direct request to first elevator
        else:
            self.lift_console2.request_button_pressed(floor)  # Direct request to second elevator


