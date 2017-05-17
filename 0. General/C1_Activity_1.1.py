"""
    Assembly Code:

            LDA ONE     # load value of one to acc
            STA COUNT   # store value of acc in count
            OUT         # output value of acc
                        # -- start of loop --
    LOOPTOP LDA COUNT   # load value of count to acc
            ADD ONE     # add value of one to value of acc
            OUT         # output value of acc
            STA COUNT   # store value of acc in count
            SUB TEN     # subtract value of ten from value of acc
            BRP ENDLOOP # if value of acc is positive end loop,
            BRA LOOPTOP # otherwise return to start of loop
    ENDLOOP HLT         # -- end of program --
    ONE     DAT 1       # data storage (one = 1)
    TEN     DAT 10      # data storage (ten = 10)
    COUNT   DAT 0       # data storage (count = 0)
    """

one = 1
ten = 10
count = 0

count = one
print(count)

while True:
    count += one
    print(count)
    if count - ten >= 0:
        break

""" The below loop would also be functionally correct,
    however, unlike the assembly code, it performs a
    logical test (checking for a negative value rather
    than a positive) before incrementing the count and
    subtracting the value of ten from it

    while count - ten < 0:
        count += one
        print(count)
    """
