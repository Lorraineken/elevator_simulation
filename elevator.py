import time
from threading import Thread

# Elevator class
class Elevator:
    def __init__(self, name):
        self.name = name  
        self.current_floor = 1  
        self.moving_up = True  # Initial direction is up
        self.eventlog = []  # Log of events for the elevator
        self.floors_to_visit = set()  # Set of floors to visit
        self.current_no_passengers = 0 #Initial number of passengers
        self.passenger_max = 8 #Maximum capacity of passengers


    # Method to add a floor to the list of stops and start moving
    def go_to_floor(self, floor):
        self.log(f"Request to stop on floor {floor}")  
        self.floors_to_visit.add(floor)  # Add floor to the set of floors to visit
        self.keep_it_moving()  # Start moving the elevator

    # Method to decide the next move of the elevator
    def next_move(self):
        if self.floors_to_visit:
            if self.current_floor in self.floors_to_visit and len(self.floors_to_visit) == 1:
                self.stay_on_floor()  # Stay if the only floor to visit is the current one
            elif self.moving_up:
                if max(self.floors_to_visit) > self.current_floor:
                    self.move_floors(1)  # Go up if there are higher floors to visit
                else:
                    self.moving_up = False  # Change direction to go down
                    self.move_floors(-1)
            else:
                if min(self.floors_to_visit) < self.current_floor:
                    self.move_floors(-1)  # Move down if there are lower floors to visit
                else:
                    self.moving_up = True  # Change direction to up
                    self.move_floors(1)


    # Method to keep the elevator moving while there are floors to visit
    def keep_it_moving(self):
        while self.floors_to_visit:
            self.next_move()  # Determine the next move
            time.sleep(5)  # Simulate time delay for moving between floors


    # Method to handle staying on the current floor
    def stay_on_floor(self):
        self.floors_to_visit.remove(self.current_floor)  # Remove current floor from visit list
        

    # Method to move the elevator by a number of floors
    def move_floors(self, num_floors):
        self.current_floor += num_floors  # Update the current floor
        self.log(f"On floor {self.current_floor}")  # display the current floor
        self.handle_making_a_stop()  # Check if the elevator needs to stop

    # Method to handle stopping at a floor
    def handle_making_a_stop(self):
        if self.current_floor in self.floors_to_visit:
            self.log(f"Stopping at floor {self.current_floor}")  # Log the stop
            if self.current_no_passengers < 8:
                self.current_no_passengers +=1
                self.log(f"{self.name} current capacity is at {self.current_no_passengers} passengers. The maximum capacity is 8")
            else:
                self.log(f"{self.name} elevator has reached maximum capacity")
            self.floors_to_visit.remove(self.current_floor)  # Remove floor from visit list


    # Method to log messages and print them
    def log(self, message):
        self.eventlog.append(message)  # Add message to the event log
        print(f"Elevator {self.name}: {message}")  # Print the message

