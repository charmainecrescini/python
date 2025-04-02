def main():
    x, y, z = input("Expression: ").split(" ")
    answer = calculate(x, y, z)
    print(f"{answer: .1f}")

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