#!/usr/bin/python3

def greet(name):
    return f"hello {name}"

print(greet("Oussema"))
print(greet("Khaled"))

def concatinating(word_one, word_two):
    return word_one + word_two
print()
print(concatinating("Hey","Oussema"))


def age_in_dog_years(age):
    result = age * 7
    return result
print()
print(age_in_dog_years(23))
""" We can specify wich arguement apeears fist like the above """

print(concatinating(word_one="Oussema !!",word_two ="Hello man"))
      
