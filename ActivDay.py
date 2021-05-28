#!/usr/bin/python3
import random

""" the topic is that we are trying to find out how to spend your day"""
breakfast = ["juice and sandwish", "milk and eggs", "crepe and coffee"]
fstAct = [ "jogging", "running", "having coffee with a friend"]
sndAct = [ "play chess", "play vedio games"]
studies = ["Maths", "Python" , "Javascript", "SQL"]
eating = ["fish and fries", "sandwish", "meat and maccoroni"]
trdAct = ["go out and see friends", "get weed", "get drinks "]

random_breakfast = random.choice(breakfast)
random_fstAct = random.choice(fstAct)
random_sndAct= random.choice(sndAct)
random_studies= random.choice(studies)
random_eating = random.choice(eating)
random_trdAct = random.choice(trdAct)
print("here we goin to show how to spend you day randomly")

print(f"first have {random_breakfast} as breakfast then go for {random_fstAct} , then {random_sndAct} , u better next study some {random_studies} , then eat some {random_eating} Finally {random_trdAct} ")
