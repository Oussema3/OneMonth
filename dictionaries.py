#!/usr/bin/python3

states = {"NY": "New york", "PA": "Pensselvenia", "CA": "California "}

print(states["NY"])
print()
#in this case the key FI dose not exist so if u try to get it by get method u will get None as a result instead of an error like the above comment
#print(states["FL"])
print(states.get("FI"))
#in this case we prevent the world none so we get as a result the value of the second arguement
print(states.get("FI","NOT FOUND"))
print(states.get("PA","NOT FOUND"))
print()
#this will print out all the keys of the dictionary
print(states.keys())
#this will print out all the values of the keys in the dictionary
print(states.values())
#adding a key with it value to the dictionary
states["FL"]= "Florida"
print(states.get("FL"))
print(states.keys())

#exemple of using dictionary to built a user

user = {"Name": "Oussema","scndName": "Ajmi","Height": "190 cm","Weight": "74 kgs","Hair": "Brown","Eyes": "brown"}
print(user)
print()
blog_post = {"Title": "11 sexy thing about me", "body": "blah blah blah blah blah blah blah blah blah blah blah "}
print(user["Name"])
print(user.get("Name","Not found"))
print(blog_post["Title"])
print(blog_post.get("Bodyy","Not Found"))
