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





class Cyclist:
    def __init__(self, name, age, weight,proficiency,protectiveGear=False  ): #these are called attributes 
        self.name = name    # Writing the class definition and include an empty constructor
        self.age= age
        self.weight = weight 
        self.proficiency= proficiency
        self.protectiveGear = protectiveGear 

    def accelerate(self):
        print(f" {self.name} your are now accelerating")
        
        
    
    def brakes(self):
        print(f" {self.name} you have hit the brakes")

    def direction(self, turn):
        print(f" you have taken a {turn} turn ")

    def protectivEequipment(self, protectiveGear):
        if protectiveGear == False :
            self.protectiveGear == True
            print(f" you are waring protective Gear ")
        else:
             self.protectiveGear == False
             print(f"you have taken off your protective Gear ")




        

        #so a def (define/function) in a class is called a method
       
    