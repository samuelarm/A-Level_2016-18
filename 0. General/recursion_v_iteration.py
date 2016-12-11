""" Factorial Finder
    Name: Mr Gorman
    Date: 01/12/2016
    """
import time

def find_factorial_loop(n):
    """ Function to find factorial using iteration.
        """
    factorial = 1
    for i in range(n, 0, -1): # alternatively, for i in range(1, n + 1):
        factorial *= i
    return factorial

def find_factorial_recursive(n):
    """ Function to find factorial using recursion.
        """
    if n == 0:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)
    

def main():
    number = 87

    # time iterative factorial finder
    i_start = time.clock()
    print(find_factorial_loop(number))
    i_end = time.clock()

    # time recursive factorial finder
    r_start = time.clock()
    print(find_factorial_recursive(number))
    r_end = time.clock()

    # calculate time duration
    i_diff = i_end - i_start
    r_diff = r_end - r_start

    print("Faster = ", end="")
    if i_diff < r_diff:
        print("Iteration")
    elif i_diff > r_diff:
        print("Recursion")
    else:
        print("Neither")
    print("\nIteration time:", i_diff)
    print("\nRecursion time:", r_diff)

if __name__ == "__main__":
    main()