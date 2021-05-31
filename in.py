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
    
