# Coding_Challenge
This project implements a function to classify packages based on their dimensions and mass, simulating logic used in an automated robotic dispatch system.

Objective:

Sort packages into the correct handling stack using the following rules:

A package is bulky if:

Its volume (Width × Height × Length) is greater than or equal to 1,000,000 cm³

OR any of its dimensions is greater than or equal to 150 cm

A package is heavy if its mass is greater than or equal to 20 kg

Stack Categories:

STANDARD - Package is neither bulky nor heavy
SPECIAL - Package is bulky OR heavy (but not both)
REJECTED - Package is both bulky AND heavy

Function Signature:

def sort(width, height, length, mass)

The function returns one of the following strings:

"STANDARD"

"SPECIAL"

"REJECTED"

Example Usage:

print(sort(100, 100, 100, 10)) # STANDARD
print(sort(200, 50, 20, 10)) # SPECIAL
print(sort(50, 50, 50, 25)) # SPECIAL
print(sort(200, 200, 200, 25)) # REJECTED

Files:

main.py - Contains the sort() function and sample test cases
README.txt - This description file
