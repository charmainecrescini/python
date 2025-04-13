# this file returns $0 for greetings starting as "Hello"
# While returns $20 for greetings that start with "H" except Hello
# By default, $100 is returned for any other greeting

# Get user's input
greeting = input("Greeting: ").lower()

# If else condition
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")