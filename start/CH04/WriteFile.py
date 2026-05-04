#!/usr/bin/env python3
# Sample script that writes to a file
# By Ray G Peckham
# Script 1 - Collect info and save to hackme.txt
"""
Write a script that saves user input into a file, that gathers data about the user
"""

#These variables are questions that need to be answered
name = input("What is your name?")
color = input("What is your favorite color?")
pet = input("What is your first pets name?")
maiden = input("What is your mother's maiden name?")
school = input("What elementary school did you attend?")

with open("hackme.txt" , "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Color: {color}\n")
    file.write(f"First Pet: {pet}\n")
    file.write(f"Mother's Maiden Name: {maiden}\n")
    file.write(f"Elementary School: {school}\n")

print("Saved to hackme.txt Great Work!")
