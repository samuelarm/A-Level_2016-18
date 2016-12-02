#Samuel Armstrong
#Coding Challange
#could just use range user_num but this is adapted from the factor finder code 
user_num = int(input("> "))
factor = []
for i in range (1, user_num+1):
        factor.append (i)
print (factor)
product = (1) 
for i in factor:
    product *= (i)
print (product)

    
    
