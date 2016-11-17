#Samuel Armstrong
#cypher coding challange

user_input = input("> ")
user_list = list(user_input)
print (user_list)
text=[]
for i in user_list:
    text.append(int(ord(i)))
print(text)


index = (0)
for i in text:
    text[0+index] = text[0+index] + 2
    index += 1

    
print (text)
##map (int, text.split (','))
##[int(s) for s in text.split(',')]

user_list = ""
for i in text:
    user_list += chr( int(i, 10))
    
print (user_list)
