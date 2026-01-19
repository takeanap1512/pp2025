"""
Tank class:
- Attributes: HP, Damage, Armor, Price
- Implement all getters and setters
- display(): Display info about the tanks
- compute_strength(): strength = sqrt(HP**2+Damage**2+Armor**2)

input_handle(): Read a list of tanks info from input.txt, the file looks like this:
4
5 5 5 20
3 8 9 15
10 20 9 45
20 10 30 30

Tasks:
- Task 1: Sort the tanks by prices so user can buy the most tanks with 75 coins
- Task 2: So coins
- Using threading and return the results as array of tank indexes (the line which the tank's info belong)

output_handle(): perform both tasks above and write the result to the file output.txt as follow:
[2,3,1]
[1,2,3]

Assemble everything in the main() function
    """
import threading
class Tank:
    def __init__(self, HP, Damage, Armor,Price):
        self.HP = HP
        self.Damage = Damage
        self.Armor = Armor
        self.Price = Price

    def getHP(self):
        return self.HP
    def setHP(self,HP):
        self.HP = HP
    def getDamage(self):
        return self.Damage
    def setDamage(self,Damage):
        self.Damage = Damage
    def getArmor(self):
        return self.Armor
    def setArmor(self,Armor):
        self.Armor = Armor
    def getPrice(self):
        return self.Price
    def setPrice(self,Price):
        self.Price = Price

    def display(self):
         print(f"Tank:{self.HP} HP, {self.Damage} DMG, {self.Armor} Armor,Price: {self.Price} ")
    def compute_strength(self):
        return (self.HP**2 + self.Damage**2 + self.Armor**2 )**0.5
    
def input_handle(file):
    try:
        with open(file,"r") as f:
            n = int(f.readline())
            tanklist = []
            for line in f:
                HP,Damage,Armor,Price = [int(i) for i in line.split()]
                tanklist.append(Tank(HP,Damage,Armor,Price))
    except Exception:
            print(Exception)
    return tanklist

def BuyPrice(tanklistIdx, result1 = []):
    gold = 75
    sortbyPrice = sorted(tanklistIdx, key = lambda x:x[1].Price)
    for x in sortbyPrice:
        if gold >= x[1].Price:
            result1.append(x[0])
            gold =gold - x[1].Price 

    return result1

def BuyStrength(tanklistIdx, result2 = []):
    gold = 75
    sortbyStrength = sorted(tanklistIdx, key = lambda x:x[1].compute_strength(),reverse=True)
    for x in sortbyStrength:
        if gold >= x[1].Price:
            result2.append(x[0])
            gold =gold - x[1].Price 
    return result2


def output_handle(file,result1,result2):
    try:
        with open(file,"w") as f:
            f.write(f"{result1} \n")
            f.write(f"{result2} ")
    except Exception:
        print(Exception)
def main():
    tanklist = input_handle("input.txt")
    tanklistIdx = [(i+1,tank) for (i,tank) in enumerate(tanklist)]
    result1 = []
    result2 = []
    t1 = threading.Thread(target=BuyPrice,args=(tanklistIdx,result1,))
    t2 = threading.Thread(target=BuyStrength,args=(tanklistIdx,result2,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    output_handle("output.txt",result1,result2)
    
    
main()

    


 