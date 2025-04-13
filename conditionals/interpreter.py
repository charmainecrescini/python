# This file calculates the mathematical expression 
# e.g. "1 + 1" will return 2.0

# Main function that accepts input and calls calculate function
def main():
    x, y, z = input("Expression: ").split(" ")
    answer = calculate(x, y, z)
    print(f"{answer: .1f}")

# Match the math expression and returns the calculated value
def calculate(x, y, z):
    match y:
        case "+":
            return float(x) + float(z)
        case "/":
            return float(x) / float(z)
        case "-":
            return float(x) - float(z)
        case "*":
            return float(x) * float(z)

main()