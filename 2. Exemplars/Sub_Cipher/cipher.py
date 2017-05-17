""" Substitution Cipher
    Name: Mr Gorman
    Date: 19/11/2016
    """
# Global constants
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def process_text(text, option):
    """ Function to encrypt or decrypt lowercase and uppercase alpha characters based on selected option.
        """
    processed_text = ""
    
    for char in text:
        if char in CHARS or char in CHARS.lower():
            if option == "e":
                char = ord(char) + 2
                if char > 90 and char < 97 or char > 122:
                    char -= 26
            elif option == "d":
                char = ord(char) - 2
                if char < 97 and char > 90 or char < 65:
                    char += 26
            char = chr(char)
        processed_text += char
    
    return processed_text

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