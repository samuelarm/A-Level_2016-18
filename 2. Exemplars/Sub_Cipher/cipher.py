""" Substitution Cipher
    Name: Mr Gorman
    Date: 19/11/2016
    """

CHARS = "abcdefghijklmnopqrstuvwxyz"

def process_text(text, option):
    processed_text = ""
    for char in text:
        if char in CHARS or char in CHARS.upper():
            if option == "e":
                processed_text += chr(ord(char) + 2)
            elif option == "d":
                processed_text += chr(ord(char) - 2)
        else:
            processed_text += char
    return processed_text

def get_text_from_file(filename):
    pass

def get_text_from_userinput():
    text = ""
    while text == "":
        text = input("Enter text: ")
    return text

def get_option():
    option = ""
    while option != "e" and option != "d":
        option = input("(E)ncrypt or (D)ecrypt? ").lower()
    return option

def main():

    option = get_option()
    text = get_text_from_userinput()
    text = process_text(text, option)
    print(text)

if __name__ == "__main__":
    main()