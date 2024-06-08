# Lift floor selection class
class LiftFloorSelection:
    def __init__(self, elevator):
        self.elevator = elevator  # Reference to the associated elevator

    # Method to handle button press events
    def request_button_pressed(self, floor):
        self.elevator.go_to_floor(floor)  # Directs the elevator to the requested floor