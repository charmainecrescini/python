# This file converts camel case to snake case
def main():
    # Get user input - camel case
    camel = input("camelCase: ")
    print(snake(camel))

# Converts camel case to snake case
def snake(camel):
    snake = ""
    for i in range(len(camel)):
        if camel[i].isupper():
            snake += "_" + camel[i].lower()
        else:
            snake += camel[i]
    return snake

main()
