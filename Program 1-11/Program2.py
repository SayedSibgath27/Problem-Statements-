'''
Creat a function by name changestring which accept teo paramenter s1, s2
the function return the string which has max no of vovel 
'''

def changestring(s1, s2):
    #Logic 
    #vovel in s1 
    counts1=0
    for i in s1: 
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
            counts1=counts1+1
            
    counts2=0
    for i in s2: 
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
            counts2=counts2+1
            
    if counts1>counts2:
        return s1 
    else:
        return s2
            
            
s1=(input("Enter first String :- "))
s2=(input("Enter Second String:- "))
results=changestring(s1, s2)
print (results)
