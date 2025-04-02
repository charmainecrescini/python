def main():
    file = input("File name: ")

    # Check for file extension (.)
    if "." in file:
        print(f"{extension(file)}")
    else:
        print("application/octet-stream")

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