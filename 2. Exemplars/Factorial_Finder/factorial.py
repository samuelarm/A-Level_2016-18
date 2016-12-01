""" Factorial Finder
    Name: Mr Gorman
    Date: 01/12/2016
    """

def find_factorial_loop(n):
    """ Function to find factorial using iteration.
        For more info on range:
        https://docs.python.org/3/library/stdtypes.html#range
        """
    factorial = 1
    for i in range(n, 0, -1): # alternatively, for i in range(1, n + 1):
        factorial *= i
    return factorial

def find_factorial_recursive(n):
    """ Function to find factorial using recursion.
        For more info on recursion limit:
        https://docs.python.org/3/library/sys.html#sys.getrecursionlimit
        """
    if n == 0:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)
    

def main():
    number = 5

    print(find_factorial_loop(number))
    print(find_factorial_recursive(number))

if __name__ == "__main__":
    main()