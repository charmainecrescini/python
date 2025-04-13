# This file determines the meal schedule based on time (24-hour format)
# 7:00-8:00 Breakfast time, 12:00-13:00 Lunch time, 18:00-19:00 Dinner time

# Main function the gets user's input and calls convert function
def main():
    time = input("What time is it? ")
    meal = convert(time)
    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")

# Converts time into corresponding number of hours as float
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

main()