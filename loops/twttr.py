# This file removes vowels from user input

# List of vowels
vowels = ["a", "e", "i", "o", "u"]

# Tweet from user
tweet = input("Input: ")

# Variable for tweet without vowels
new_tweet = ""

# Remove vowels on tweet
for letter in tweet:
    if not letter.lower() in vowels:
        new_tweet += letter

# Print tweet without vowels
print(new_tweet)