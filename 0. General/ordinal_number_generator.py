def get_ordinal(number):
    number_string = str(number)
    number_length = len(number_string)
    first_digit = number_string[number_length - 1 : number_length]
    second_digit = number_string[number_length - 2 : number_length - 1]

    if first_digit == "1" and second_digit != "1":
        return "st"
    elif first_digit == "2" and second_digit != "1":
        return "nd"
    elif first_digit == "3" and second_digit != "1":
        return "rd"
    else:
        return "th"

def main():
    # test cases
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 
                   20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                   100, 101, 111, 121, 150,
                   1000, 1001, 1002, 1003, 1004, 
                   1000000, 1000001, 1000002, 1000003, 1000004,
                   0]

    for number in number_list:
        print("%d%s" % (number, get_ordinal(number)))

if __name__ == "__main__":
    main()
