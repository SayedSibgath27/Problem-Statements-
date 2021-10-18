'''
Creat a function by name addstring which accept 3 parameter s1, s2, s3
The function return string which has max length 
'''
def addstring(s1, s2, s3):
    #Logic
    lengthofs1=len(s1)
    lengthofs2=len(s2)
    lengthofs3=len(s3)
    print (lengthofs1,lengthofs2,lengthofs3)
    if lengthofs1>lengthofs2 and lengthofs1>lengthofs3:
        return s1
    elif lengthofs2>lengthofs1 and lengthofs2>lengthofs3:
        return s2
    else:
        return s3
a=(input("Enter first number:- "))
b=(input("Enter Second number:- "))
c=(input("Enter third number:- "))
ans=addstring(a,b,c)
print(ans)


