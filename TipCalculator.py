#!/usr/bin/python3
name = input("whats your name ? ")
print(f"Hi {name} ")
print()
bill_coast = float(input("how much your bill worth ? "))
tip = (bill_coast * 10) / 100
print(f"you better give as a tip {tip}$")
total = tip + bill_coast
print()
print(f"so the total is {total}$ ")
