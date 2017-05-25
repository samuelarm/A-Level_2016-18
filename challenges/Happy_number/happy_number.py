def happy_number(number):
    record = []
##    if trys == 100:
##        return False
##    else:
    total = 0
    number= str(number)
    for i in number:
        i = int(i)
        total = total + i**2
        if total in record:
            return False
        record.append(total)
            
    if total == 1:
        return True
    else:
        return (happy_number(total,))

number= int(input("Please input a number you want to test: "))
is_happy =(happy_number(number,))

if is_happy == True:
    print("This is a happy number")
else:
    print ("This is not a happy number")
    
