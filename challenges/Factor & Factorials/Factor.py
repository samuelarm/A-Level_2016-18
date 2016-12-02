#Samuel Armstrong
#Factor Finder
#note to self % returns the remainder after the devision

user_num = int(input("> "))
factor = []
for i in range (1, user_num+1):
    if user_num%i == 0:
        factor.append (i)
print (factor)
