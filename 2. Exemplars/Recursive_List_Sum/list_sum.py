""" Recursive List Sum
    Name: Mr Gorman
    Date: 05/12/2016
    """

def sum_list(lst):
    """ Function to find the sum of all elements in a list using recursion.
        """
    total = 0
    for element in lst:
        if type(element) == list:
            total += sum_list(element) # <-- recursive
        else:
            total += element
    return total

def main():
    # testing the algorithm
    test_cases = [ 
                 [1, 2, 3, 4, 5, 6],
                 [1, 2, [3, 4, 5, 6]],
                 [1, 2, [3, 4], [5, 6]],
                 [1, 2, [3, 4], [5, [6]]],
                 [1, 2, [[3, 4], [5, [6]]]]
                 ]

    for i in range(len(test_cases)):
        result = sum_list(test_cases[i])
        if result == 21:
            print("Test %d: Passed! (Result: %d)" % (i + 1, result))
        else:
            print("Test %d: Failed! (Result: %d)" % (i + 1, result))

if __name__ == "__main__":
    main()