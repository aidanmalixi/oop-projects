class Pet: 
    def __init__(self, name, hunger_level=5, happiness_level=5): # constructor method, when someone creates a pet, you must establish these parameters
        self.name = name 
        self.hunger_level = hunger_level
        self.happiness_level = happiness_level

    def feed(self):
        if self.hunger_level > 0:
            self.hunger_level -=2
        self.happiness_level +=2
        print(f"{self.name} has been fed.")
        print (f"{self.name} now has a hunger level of {self.hunger_level} and a happiness level of {self.happiness_level}")

    def play(self):
        self.happiness_level +=2
        self.hunger_level +=2
        print(f"You played with {self.name}.")
        print (f"{self.name} now has a hunger level of {self.hunger_level} and a happiness level of {self.happiness_level}")

    def rest(self):
        if self.happiness_level > 0:
            self.happiness_level -=1
        else:
            print("Happiness level is very low. Please recharge.")
        self.hunger_level +=1
        print(f"{self.name} has rested.")
        print (f"{self.name} now has a hunger level of {self.hunger_level} and a happiness level of {self.happiness_level}")

    
    def status(self):
        print(f"\n{self.name}'s Current Status:")
        print(f"Happiness level: {self.happiness_level}")
        print(f"Hunger level: {self.hunger_level}")
