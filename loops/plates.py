def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isnumeric() and s[1].isnumeric():
        return False
    elif not s.isalnum():
        return False
    elif not is_plate_format(s):
        return False
    else:
        return True

def is_plate_format(s):
    for i in range(len(s)):
        if i > 1:
            if s[i].isnumeric() and s[i - 1].isalpha():
                if s[i] == '0':
                    return False
            elif s[i].isalpha() and s[i - 1].isnumeric():
                return False
    return True        
main()