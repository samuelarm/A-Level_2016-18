my_dict = {"A" : "You selected A",
           "B" : "You selected B",
           "Default" : "Unrecognised selection"
           }

user_input = input("> ").upper()

try:
    print(my_dict[user_input])
except KeyError:
    print(my_dict["Default"])
