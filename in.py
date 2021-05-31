#!/usr/bin/python3

answer = input(" do you wanna hear a joke ? ")
affirmativ_answers = ["YES", "Y","yes", "y"]
negative_answers = ["NO", "N","no","n"]
if answer in  affirmativ_answers:
    print("I'm against picketing, but I don't know how to show it.")
elif answer in negative_answers:
    print("Fine :( ")
else:
    print("i dont understand")
#another way of doing that     
"""
answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")
"""
