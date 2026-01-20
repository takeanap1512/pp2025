"""
Exercise 1 (5pt). Define a Python class named Robot with the following attributes:

serial: representing the robot's serial number (string).

model: representing the robot's model type (e.g., "Worker", "Drone").

energy: representing the robot's energy percentage (0-100).

Create an instance of the Robot class with the following details:

Serial: "R2-D2"

Model: "Astromech"

Energy: 100

Exercise 2 (5pt). Define a subclass named SecurityRobot inheriting from the Robot class. Add an additional attribute:

gadgets: a list representing the tools/weapons the robot carries.

Override the __str__() method in the SecurityRobot class to return a string displaying information about the robot, including its serial, model, energy, and the list of gadgets.

Exercise 3 (5pt). Add an instance method to the SecurityRobot class called save_log(filename) to save the current robot's information to a text file named filename.

Each attribute should be written on a separate line.

The save_log() method must handle exceptions using try/except to prevent the program from crashing if a runtime error occurs during file I/O.

Exercise 4 (5pt). Add an instance method to the SecurityRobot class called background_backup(filename).

This method should create a separate Thread.

Inside the thread, call the previously defined method save_log(filename).

In the main execution block, instantiate a SecurityRobot and call background_backup() to save its info to a file named "robot_data.txt".

"""
import threading
class Robot:
    def __init__(self, serial, model, energy):
        self.serial = serial
        self.model = model
        self.energy = energy
    
r1 = Robot("R2-D2","Astromech",100)

class SecurityRobot(Robot):
    def __init__(self, serial, model, energy, gadgets):
        super().__init__(serial, model, energy)
        self.gadgets = gadgets
    def __str__(self):
        return f"Serial:{self.serial} \n Model:{self.model} \n Energy:{self.energy} \n Gadget:{self.gadgets}"
    def save_log(self,filename):
        try:
            with open(filename, "w") as f:
                f.write(self.serial + "\n")
                f.write(self.model + "\n")
                f.write(str(self.energy) + "\n")
                f.write(str(self.gadgets) + "\n")
        except Exception:
            print("Execption")
    def background_backup(self,filename):
        t = threading.Thread(target = self.save_log, args= (filename,))    
        t.start()
r2 = SecurityRobot("R2-D3","Astromeche",90,["Gun"])
print(r2)
r2.background_backup("backup.txt")


