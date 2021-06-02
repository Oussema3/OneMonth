#!/usr/bin/python3

"""  ____________CHALLENGE_____________ """


""" Create a function called uppercase_and_reverse that takes a little bit of text,
    uppercases it all, and then reverses it (flips all the letters around) so that: """

def uppercase_and_reverse(name):
    result = name[::-1]
    result_2 = result.upper()
    return result_2

print(uppercase_and_reverse("Do not go gentle into that good night."))

"""  Other way of doing this  """

""" 
def upper_and_reverse(text):
    return text.upper()[::-1]

print(upper_and_reverse("aabb"))

"""
