'''
Creat a function by name pallindrome need a paramenter s1, The function return true if it is pallindrome else retrun false
'''


def pallindrome(s1):
    #logic
    reverses1=s1[::-1]
    print (reverses1)
    if s1==reverses1:
        return True
    else:
        return False 
s1=(input("Enter first Word:- "))
result=pallindrome(s1)
print(result)
    