#Samuel Armstrong
#cypher coding challange

def char_int(user_list):
    text = []
    for i in user_list:
        text.append(ord(i))
    return text

def encode_decode(text,encode_or_decode):
    if encode_or_decode == "D":
        for i in range(len(text)):
            text[i] = text[i] - 2
    else:
        for i in range(len(text)):
            text[i] = text[i] + 2
    return text

def int_char(text):
    user_list = ""
    for i in text:
        user_list += chr(i)
    return user_list
    


def main ():
    user_input = input("> ")
    user_list = list(user_input)
    encode_or_decode =input ("do you want to [E]ncode or [D]ecode > ").upper()
    text = char_int(user_list)
    text = encode_decode(text,encode_or_decode)
    user_list = int_char(text)
    print(user_list)
    
    
if  __name__ == "__main__":
    main()

