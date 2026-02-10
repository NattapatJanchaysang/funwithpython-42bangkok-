#!/usr/bin/python3
number = int(input("Enter number less than 25: "))
if number >= 25:
    print("Error: Number must be less than 25.")
else:
    while number <= 25:
        print(f"Current number: {number}")
        number += 1