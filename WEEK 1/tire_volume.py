"""
For creativity, I added a code that asks user if he/she wants to buy tires with the specifications 
and prompts them to input their phone number and if the number doesn't equal to specified number character,
re-prompts them to input the phone number
"""

# Import the datetime and math module to be used in the program
import datetime
import math

# Get the tire width from the user
width = float(input("What is the tire width in mm: "))

# Get the tire aspect ratio from the user
aspect_ratio = float(input("What is the aspect ratio: "))

# Get the tire diameter from the user
diameter = float(input("What is the diameter in inches: "))

# Compute the approximate volume of the tire
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10000000000

# Print out the volume to the user
print(f"The approximate volume is {volume:.2f} litres")

# Ask the user if he/she wants to buy the tire with the dimensions entered
response = (input("Do you want to buy the tires with the dimensions you specified: ")).lower()


if response == "yes":
    phone_number = input("Input your phone number: ")

    # Loop until the correct number character of phone number is typed in
    while len(phone_number) != 11:
        print("Invalid phone number, must be eleven characters")

        # Reprompt the phone number input
        phone_number = input("Input your phone number: ")
        print("Thanks for your patronage")

else:
    phone_number = "Nil"
    print("Thanks for your patronage")

# Get the current date from the computer's operating system
date_today = datetime.datetime.now().strftime('%Y-%m-%d')

# Open the text file named volume.txt for appending
with open("volumes.txt", "at") as volume_file:

    # Append the current date, width, aspect ratio, diameter and volume to the text file
    print(f"{date_today}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f} - {phone_number}", file = volume_file)

