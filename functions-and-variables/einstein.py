# This file prompts the user for mass as an integer (in kilograms)
# Then outputs the equivalent number of Joules as an integer.

# Main function that takes input in kilograms
def main():
    kilograms = int(input("Input kilograms: "))
    joules = calculate_joules(kilograms)
    print(f"{kilograms} kg is", f"{joules} joules")

# Calculate the joules
def calculate_joules(kg):
    speed_of_light = 300000000
    joules = kg * (speed_of_light * speed_of_light)
    return joules

main()