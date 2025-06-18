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
        print(f"[pet_simulator.py] __name__ is: {__name__}")

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

def show_menu(pet):
    print(f"1: Feed {pet.name}.")
    print(f"2: Play with {pet.name}.")
    print(f"3: Let {pet.name} rest.")
    print(f"4: Show happiness and hunger status of {pet.name}.")
    print(f"5: Exit menu.")

def main():
    pet_name = input("Please enter name for your pet: ")
    if pet_name:
        pet = Pet(pet_name)
    else:
        print("Pet name cannot be blank. Please try again.")
    while True:
        show_menu(pet)
        option = int(input("Choose an option: "))
        if option == 1:
            pet.feed()
        elif option == 2:
            pet.play()
        elif option == 3:
            pet.rest()
        elif option == 4:
            pet.status()
        elif option == 5:
            print(f"{pet.name} will miss you!")
            break
        else:
            print("Please enter a valid number in the menu.")

if __name__ == "__main__":
    main()
    
