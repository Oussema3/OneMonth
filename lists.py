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
