#Creat a function by name validcontactnumber it accepet one paramenter list l1# List contain cointact number of n useres. The function return the list of valid contact number 

def validcontactnumber(l1):
    #Logic 
    nwecontact=list()
    for i in l1:
        if len(i)==10:
            nwecontact.append(i)
    return nwecontact
            

n=int(input("Enter the number of contact:-"))
a=list()
for i in range(n):
    contact=(input("Enter the contact number:-"))
    a.append(contact)
result=validcontactnumber(a)
print(result)
