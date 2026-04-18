from tkinter.messagebox import showerror


class Dog:
    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed
    def bark(self):
        print("Woof! Woof!")
    def rename(self, name):
        self.name = name
    def eat(self, food):
        self.weight += food
    def show(self):
        print(f"{self.name} is a {self.age} year old {self.furColor} {self.breed} that weighs {self.weight} lbs.")

print("You are about to create a dog.")
age = input("How old is the dog: ")
weight = float(input("How much does the dog weigh: "))
name = input("What is the dog’s name: ")
color = input("What color is the dog: ")
breed = input("What breed is the dog: ")
myDog = Dog(age, weight, name, color, breed)
myDog.show()
myDog.bark()
myDog.eat(float(input(f"{name} is hungry, how much should he eat: ")))
myDog.rename(input(f"{name} isn’t a very good name. What should they be renamed to: "))
myDog.show()