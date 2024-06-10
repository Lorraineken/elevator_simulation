# elevator_simulation

This project is based on developing an elevator simulation system for a building with two elevators. The simulation is implemented in python and it operates based on the principle of prioritizing passengers based on the order they called the elevator and the floor they are on.


## Requirements Achieved
1. Elevator Control Logic
The elevator maintains its current floor and direction of travel (upwards or downward). It also responds to calls from passengers on different floors.

2. Passenger Handling
Passengers are able to call an elevator from any floor and are able to specify their destination floor when calling the elevator

3. Prioritization
The prioritization of the elevator is based on the floor the passenger is on and direction they want to travel


## Assumptions
1. When the elevator starts running there are no passengers in them
2. Whenever the elevator stops at a given floor 1 passenger gets in ... Simulation of passengers alighting from the elevators is yet to be done

## Design Choice
Threading is used to simulate concurrent lift requests. Multiple users might press the lift buttons simultaneously which will require the system to handle these requests at the same time. Threading allows replication of the concurrent activity by generation threads for individual requests.
Below is a sample executed code.

 ![Sample code](./screens/screenshot1.png?raw=true "sample usecase")


## Pre-requisites
In order to use this repo you need to have the following installed:

- OS [either: Windows 10+, Linux or MacOS(running on x86 or arm architecture)]
- Python

## Installation

To use this repo on your machine requires some simple steps

### Alternative One

- Open a terminal / command line interface on your computer
- Clone the repo by using the following:

        git clone https://github.com/Lorraineken/elevator_simulation

- Be patient as it creates a copy on your local machine for you.
- Change directory to the repo folder:

        cd elevator_simulation

- (Optional) Open it in ``Visual Studio Code``

        code .

- (Alternate Option) Open it in any editor of your choice.



## Running the application
To run the application on the terminal 

    python3 elevator_simulation.py

The elevator_simulation.py file contains a use case scenario


# Authors
This project was contributed to by:
- [Lorraine Kupa](https://github.com/Lorraineken)

# License
The project is licensed under Apache 2.0.