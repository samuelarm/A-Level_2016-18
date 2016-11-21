#Samuel Armstrong
#cypher coding challange
import random

user_input = input("> ")
user_list = list(user_input)
print (user_list)
text=[]
for i in user_list:
    text.append(ord(i))
print(text)


index = (0)
for i in text:
    text[0+index] = text[0+index] + 2
    index += 1

    
print (text)


user_list = ""
for i in text:
    user_list += chr(i)
    
print (user_list)
print("\n")

# with a random int as the + on now

print ("now testing with a random interger")
print ("\n")

random_interger = random.randint(0,10)

user_input = input("> ")
user_list = list(user_input)
print (user_list)
text=[]
for i in user_list:
    text.append(ord(i))
print(text)


index = (0)
for i in text:
    text[0+index] = text[0+index] + random_interger
    index += 1

    
print (text)


user_list = ""
for i in text:
    user_list += chr(i)
    
print (user_list)
print("\n")

#decoding it now

print ("now decoding it using the random interger one(2nd set of results)")
print ("\n")

text=[]
for i in user_list:
    text.append(ord(i))
print(text)

index = (0)
for i in text:
    text[0+index] = text[0+index] - random_interger
    index += 1

    
print (text)


user_list = ""
for i in text:
    user_list += chr(i)
    
print (user_list)


