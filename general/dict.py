#Dictionary
#Samuel Armstrong
my_dict = {"A" : "You selcted A",
           "B" : "You selected B",
           "Default" : "Unrecognised selection"
           }

user_input = input ("> ")
#if user_input in my_dict:
    try:
        print  (my_dict[user_input])
    except KeyError:
        print  (my_dict["Default"])
    
        
        
#else:
#   print  (my_dict["Default"])
    
