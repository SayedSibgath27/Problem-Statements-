#Creat a finction filterdata which accept 3 list, firstname, lastname, contact number. Return the firstname annd last name of all the users is valid.

def filterdata(firstname,lastname,contactnumber):
    #print(firstname,lastname,contactnumber)
    validuser=list()
    for i in range(n):
        if len(contactnumber[i])==10:
            fname=firstname[i]
            lname=lastname[i]
            fullname=fname+lname
            validuser.append(fullname)
    return validuser

            
            
            
n=int(input("enter the number of users:- "))
firstname=list()
lastname=list()
contactnumber=list()
for i in range(n):
    fname=(input("Enter your first name:-"))
    firstname.append(fname)
    lname=(input("Enter your last name:-"))
    lastname.append(lname)
    cnumber=(input("Enter your contact number:-"))
    contactnumber.append(cnumber)
result=filterdata(firstname,lastname,contactnumber)
print(result)