# Creat a function by name givenvaliduser which accept 3 parameter username, password, contact number. The function return the contact nmber of validuserid and password. 

def givenvaliduser(username, password,contactnumber):
    userid=(input("Enter your user ID:-"))
    pwd=(input("Enter your password:-"))
    #print(username, password, contactnumber)
    for i in range(n):
        if username[i]==userid and password[i]==pwd:
            return contactnumber[i]
    return "Invalid userid or password"
        
            
       


n=int(input("Enter the number of user:-"))
username=list()
password=list()
contactnumber=list()
for i in range(n):
    uname=(input("Enter the user name:- "))
    username.append(uname)
    pword=(input("Enter the password:- "))
    password.append(pword)
    cnumber=(input("Enter the contact number:- "))
    contactnumber.append(cnumber)
result=givenvaliduser(username, password, contactnumber)
print(result)