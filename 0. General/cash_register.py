def calculate_change(change_due, cash_available):

    cash_description = [ cash_available[i][0] for i in range(len(cash_available)) ]
    cash_value       = [ cash_available[i][1] for i in range(len(cash_available)) ]
    cash_count       = [ cash_available[i][2] for i in range(len(cash_available)) ]

    for i in range(len(cash_available)):
        
        count=0

        while change_due > cash_value[i] and cash_count[i] > 0:
            change_due -= cash_value[i]
            cash_count[i] -= 1
            count+=1

        if count > 0:

            if cash_value[i] > 0.5:
                cash_type = "note"
            else:
                cash_type = "coin"
            
            if count > 1:
                cash_type += "s"
            
            print("You need to provide %d %s %s" % (count, cash_description[i], cash_type))

def main():
    cash_available = [ ["£50",  50, 3 ],
                       ["£20",  20, 5 ],
                       ["£10",  10, 12],                   
                       ["£5",    5, 10],
                       ["£2",    2, 15],
                       ["£1",    1, 20],
                       ["50p", 0.5, 5 ],
                       ["20p", 0.2, 20],
                       ["10p", 0.1, 30],
                       ["5p", 0.05, 10],
                       ["2p", 0.02, 15],
                       ["1p", 0.01, 10]
                     ]
    change_due = 105.69

    print("Change due:", change_due)
    calculate_change(change_due, cash_available)

if __name__ == "__main__":
    main()
