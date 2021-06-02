#!/usr/bin/python3

"""  ____________CHALLENGE_____________ """


""" Create a function called uppercase_and_reverse that takes a little bit of text,
    uppercases it all, and then reverses it (flips all the letters around) so that: """

def uppercase_and_reverse(name):
    result = name[::-1]
    result_2 = result.upper()
    return result_2

print(uppercase_and_reverse("Do not go gentle into that good night."))

# Method 2

""" 
def upper_and_reverse(text):
    return text.upper()[::-1]

print(upper_and_reverse("aabb"))

"""
# Method 3

"""
def reverse(text):
    return text[::-1]

def reverse_and_upper(text):
    return reverse(text.upper())

print(reverse_and_upper("hi"))

"""
