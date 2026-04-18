class Chair:
    def __init__(self, numOfLegs = 4, rolling = False, material = "Wood"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material
    def show(self):
        if self.rolling:
            roll = "rolling"
        else:
            roll = "not rolling"
        print(f"Your chair has {self.numOfLegs} legs, is {roll}, and is made of {self.material}.")
print("You are about to create a chair.")
legs = int(input("How many legs does your chair have: "))
if input("Is your chair rolling (true/false): ") == "true":
    roll = True
else:
    roll = False
material = input("What is your chair made of: ")
my_chair = Chair(legs, roll, material)
my_chair.show()
print("This program is going to change that.")
my_chair = Chair()
my_chair.show()