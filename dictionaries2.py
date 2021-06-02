#!/usr/bin/python3
""" dictionaries and Lists can be inside of each other"""
animal_sounds = {
    "cat": ["Mewo", "purr"],
    "Dog": ["woof", "bark"],
    "Fox": []
    }
Oussema = {"Name": "Oussema","scndName": "Ajmi","Height": "190 cm","Weight": "74 kgs","Hair": "Brown","Eyes": "brown"}
Khaled = {"Name": "Khaled","scndName": "Daly","Height": "182 cm","Weight": "70 kgs","Hair": "black","Eyes": "brown"}
Garesh = {"Name": "Mohammed","scndName": "Garresh","Height": "180 cm","Weight": "174 kgs","Hair": "brown","Eyes": "black"}
""" this is a list of dictionaries """
people = [Oussema, Khaled, Garesh]
print(animal_sounds)
print()
print(people)


for person in people:
    print(person.get("Height","Not found"))


