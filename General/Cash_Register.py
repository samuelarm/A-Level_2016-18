cash_register = [ [50, 3], # £50
                  [20, 5], # £20
                  [10, 12], # £10
                  [5, 10], # £5
                  [2, 15], # £2      
                  [1, 20], # £1
                  [0.5, 5], # 50p
                  [0.2, 20], # 20p
                  [0.1, 30], # 10p
                  [0.05, 10], # 5p
                  [0.02, 15], # 2p
                  [0.01, 10]  # 1p
                ] 
change_due = 105.69 # The amount that needs to be provided from cash in cash_register

def calc_change(change_due, cash_register):
    """ Function to calculate the amount of change required in notes and coins
        """ 
    # for loop to run the while loop for every coin/note in cash_register
    for i in range(len(cash_register)):
        
        count=0
        
        # figures out how many of each coin/note needs to be given in order to equal the change due
        while change_due > cash_register[i][0] and cash_register[i][1] > 0:

            change_due -= cash_register[i][0]
            cash_register[i][1] -= 1
            count+=1
        
        if count > 0:

            if cash_register[i][0] > 0.5:
                output = "£%d note" % cash_register[i][0]
            else:
                output = "%dp coin" % (cash_register[i][0] * 100)
            if count > 1:
                output += "s"

            print("You need to provide %d %s" % (count, output))

print("Change due:", change_due)
calc_change(change_due, cash_register)