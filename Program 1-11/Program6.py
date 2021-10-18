#Create a function by name positivelist whcih except one parameterlist. The function return total number of positivelist element into it. 
def positivelist(l1):
    #Logic
    count=0
    for i in l1:
        if i>0:
            count=count+1
    return count       
        
a=list()
numofdata=int(input("Enter the number of element:-"))
for i in range(numofdata):
    data=int(input("Enter the data:-"))
    a.append(data)
result=positivelist(a)
print(result)