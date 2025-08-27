"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# Import the math library to use the floor function
import math

# Get the user's age and convert it to integer
age =  int(input("What is your age: "))

# Calculate the maximum heart rate
max_heart_rate_pm = 220 - age

# Get the minimum and maximum heart range
min_heart_range = math.floor((65 /100) * max_heart_rate_pm)
max_heart_range = math.floor((85 / 100) * max_heart_rate_pm)

# Print the output to the user
print(f"When you execerse to strengthen your heart, you should\nkeep your heart rate between {min_heart_range} and {max_heart_range} beats per minute")
