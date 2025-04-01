# This file converts :) to smily emoji and :( as sad emoji

# Main function that calls for convert and print
def main():
    text = input("Type anything with :) or :( ")
    text = convert(text)
    print(text)


# Convert function that replace string with emoji
def convert(text):
    text = text.replace(":)", "😊")
    text = text.replace(":(", "☹️")
    return text

main()