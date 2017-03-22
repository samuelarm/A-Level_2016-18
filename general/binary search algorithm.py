# Samuel Armstrong
# binary search algorithm

def binary_search(key, array, min, max):
    """Function to return key index usinbg a recursive
       binary search algorthim
       """
    
    if max<min:
        return -1
    else:
        mid_point = int((max-min) / 2) + min

    if array[mid_point] < key:
        return binary_search (key, array, mid_point + 1, max) 
    elif array[mid_point] > key:
        return binary_search (key, array, min, mid_point - 1)
    else:
        return mid_point
    
def linear_search(key, array, index):
    """Function to return key index usinbg a recursive
       linear search algorthim
       """
    if index < len(array):
        if array[index] != key:
            return linear_search (case, test_array, index +1)

        else:
            return index
    else:
        return -1
    



#tests
test_array = ["Aardvark", "Badger", "Cat", "Dog", "Eagle", "Frog", "Gecko", "Honey Badger",
              "Iguana", "Jackal", "Kid", "Llama", "Monkey", "Narwhal", "Ostrich", "Penguin",
              "Quail", "Rhinoceros", "Snake", "Tapir", "Upupa", "Viper", "Whale", "Xenon",
              "Yellow Mongoose", "Zebra"]

test_cases = ["Viper", "buffalo", "Hedgehog", "Jackal", "Kid", "Seahorse", "Penguin"]


#loop to searchy for our test data within the test array
for case in test_cases:
    position = binary_search (case, test_array, 0, len(test_array) - 1) + 1
    if position > 0:
        print(case, "is found at position", position)
    else:
        print (case, "not found in the array")

print("\n")
print("\n")

for case in test_cases:
    position = linear_search (case, test_array, 0) + 1
    if position > 0:
        print(case, "is found at position", position)
    else:
        print (case, "not found in the array")
