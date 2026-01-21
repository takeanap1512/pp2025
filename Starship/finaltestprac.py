import threading
class Starship:
    def __init__(self,speed,shield,firepower,price):
        self.__speed = speed
        self.__shield = shield
        self.__firepower = firepower
        self.__price = price

    @property
    def getSpeed(self):
        return self.__speed
    @getSpeed.setter
    def setSpeed(self,speed):
        self.__speed = speed
    @property
    def getShield(self):
        return self.__shield
    @getShield.setter
    def setShield(self,shield):
        self.__shield = shield
    @property
    def getFirepower(self):
        return self.__firepower
    @getFirepower.setter
    def setFirepower(self,firepower):
        self.__firepower = firepower
    @property
    def getPrice(self):
        return self.__price
    @getPrice.setter
    def setPrice(self,price):
        self.__price = price
    def display(self):
        print(f"Speed:{self.__speed} \nShield:{self.__shield} \nFirePower:{self.__firepower} \nPrice:{self.__price}")
    def compute_combat_power(self):
        return (self.__speed**2 + self.__shield**2 + self.__firepower**2)**0.5

def input_handle(file):
    try:
        with open(file,"r") as f:
            n = int(f.readline())
            shiplist = []
            for l in f:
                speed, shield, firepower, price = [int(i) for i in l.split()]
                shiplist.append(Starship(speed,shield,firepower,price))
    except Exception:
        print("Exception")
    return shiplist
def BuybuyPrice(shiplistIdx,result1 = []):
    gold = 80
    sortbyprice = sorted(shiplistIdx, key = lambda x:x[1].getPrice)
    for x in sortbyprice:
        if gold >= x[1].getPrice:
            result1.append(x[0])
            gold = gold - x[1].getPrice
    return result1

def BuybuyPower(shiplistIdx,result2 = []):
    gold = 80
    sortbycombatpower = sorted(shiplistIdx, key = lambda x:x[1].compute_combat_power(),reverse=True)
    for x in sortbycombatpower:
        if gold >= x[1].getPrice:
            result2.append(x[0])
            gold = gold - x[1].getPrice
    return result2

def output_handle(file,result1,result2):
    try:
        with open(file,"w") as f:
            f.write(f"{result1} \n")
            f.write(f"{result2} \n")
    except Exception:
        print(Exception)
def main():
    shiplist = input_handle("input.txt")
    shiplistIdx = [(i+1,ship) for (i,ship) in enumerate(shiplist)]
    result1 =[]
    result2 = []
    t1 = threading.Thread(target= BuybuyPrice,args = (shiplistIdx,result1))
    t2 = threading.Thread(target= BuybuyPower,args = (shiplistIdx,result2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    output_handle("output.txt",result1,result2)

main()