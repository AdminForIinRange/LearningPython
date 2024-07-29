class Bike:
    def __init__(self, type, maximumGears, currentGear):
        self.type = type
        self.maximumGears= maximumGears
        self.currentGear = currentGear
    # method
    def gearChange(self, change) : #so a def (define/function) in a class is called a method
        if (change == True):
            if (self.currentGear < self.maximumGears):
                self.currentGear += 1
                print(f"+ 1 To The Gear, The Current Gear is {self.currentGear} ")
            else:
                print(f"Gear is at Max, The Current Gear is {self.currentGear}")
        elif(change == False):
            if (self.currentGear > 1):
                self.currentGear -= 1
                print(f"- 1 To The Gear, The Current Gear is {self.currentGear} ")
            else:
                print(f"Gear is at the lowest, The Current Gear is {self.currentGear} ")
    

my_bike = Bike(type="Mountain Bike", maximumGears=18, currentGear=1)



