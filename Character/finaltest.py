"""
Exercise 1. (5pt) Create a Python class called Character for a game with the following attributes:

name: representing the character's name.

level: representing the character's experience level (e.g., 1, 2, 3)

health: representing the character's health points (HP).

Create an instance of the Character class with the following details:

Name: Stone Giant

Level: 1

Health: 780

Exercise 2. (5pt) Define a subclass called PlayerCharacter inheriting from the Character class. Add an additional attribute:

inventory: representing the items the player character carries.

Override the __str__() method in the PlayerCharacter class to display information about the player character, including their name, level, health, and inventory.

Exercise 3. (5pt). Add an instance method to the PlayerCharacter class called save(filename) to save information of the current character to a text file filename. Each piece of information should be written on a separated line. The save() method should handle exception properly, just in case there is some error at runtime happened.

Exercise 4. (5pt). Add an instance method to the PlayerCharacter class called save_in_background(filename) to create a separated thread, in which calls the previously defined method save(filename).

In the main thread, call the save_in_background() method to save information to a file named "player.txt"
"""
import threading
class Character:
    def __init__(self,name,level,health):
        self.name = name
        self.level = level
        self.health = health
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getLevel(self):
        return self.level
    def setLevel(self,level):
        self.level = level
    def getHealth(self):
        return self.health
    def setHealth(self,health):
        self.health = health
c1 = Character("Stone Giant", 1, 780)
class PlayerCharacter(Character):
    def __init__(self,name,level,health,inventory):
        super().__init__(name,level,health)
        self.inventory = inventory
    def __str__(self):
        return f" Name:{self.name} \n Level:{self.level} \n Health:{self.health} \n Inventory:{self.inventory}"
    def save(self,filename):
        try:
            with open(filename,"w") as f:
                f.write(self.name + "\n")
                f.write(str(self.level) + "\n")
                f.write(str(self.health) + "\n")
                f.write(str(self.inventory)+ "\n")
        except Exception:
            print("Exception")

    def save_in_background(self,filename):
        t = threading.Thread(target=self.save,args=(filename,))
        t.start()
c2 = PlayerCharacter("Nap",100,1000,"Sword")
print(c2)
c2.save_in_background("player.txt")
