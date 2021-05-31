#!/usr/bin/python3

the_count = [1, 2, 3, 4]
stocks = ["AAPL", "GOOG","TSlA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["OH, NO !!", "A list inside of a list"]]

for number in the_count:
    print("this is count", number)
print()
for stock in stocks:
    print("stock ticker:", stock)
print()
for thing in random_things:
    print("the thing is :", thing)

# we can also build lists from scratch using some predifined functions such as "append()" function
people = []
people.append("Oussema")
people.append("khaled")
people.append("garrech")
print()
print(people)
#we can also remove from a list using "remove()" function
print()
people.remove("garrech")
print()
print(people)
print()
print()
#square of numbers from 1 to 10
print("squares from 0 to 10")
print()
numbers = [*range(11)]
for n in numbers:
    print(f"square of {n} is :", n**2)
