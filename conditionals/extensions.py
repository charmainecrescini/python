# This file determines the file extensions and return the type

# Main function that accepts file name
def main():
    file = input("File name: ")

    # Check for file extension (.)
    if "." in file:
        print(f"{extension(file)}")
    else:
        print("application/octet-stream")

# Match the file extension types
def extension(f):
    f = f.split(".")[1].lower()
    match f:
        case "jpg" | "jpeg":
            return "Image/jpeg"
        case "gif" | "png":
            return "Image/" + f
        case "pdf" | "zip":
            return "application/" + f
        case "txt" | "zip":
            return "text/plain"
        case _:
            return "application/octet-stream"

main()