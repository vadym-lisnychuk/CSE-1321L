class BuildingBlueprint:
    def __init__(self, number_of_stories = 10, number_of_apartments = 20, occupancy_rate = 1.0):
        self.number_of_stories = number_of_stories
        self.number_of_apartments = number_of_apartments
        self.occupancy_rate = occupancy_rate
        self.is_full = occupancy_rate == 1.0

    def update_occupancy(self, rate):
        self.occupancy_rate = rate
        self.is_full = self.occupancy_rate == 1.0

    def show(self, n):
        print(f"Building {n} has {self.number_of_stories} floors, {self.number_of_apartments} apartments, and is {int(self.occupancy_rate * 100)}% occupied. Full? {self.is_full}")

buildingOne = BuildingBlueprint()
buildingTwo = BuildingBlueprint(30, 30, .75)

print(f"Year 2025:")
buildingOne.show(1)
buildingTwo.show(2)

print("\nMany years passed\n")

buildingOne.update_occupancy(0)
buildingTwo.update_occupancy(1)

buildingOne.show(1)
buildingTwo.show(2)

print("Looks like people prefer taller buildings.")