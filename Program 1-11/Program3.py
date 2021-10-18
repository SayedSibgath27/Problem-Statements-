'''
Creat a function trimstring which accept one paramenter, s1
function return first half of a string if the count of the vovel is greater than consonebt otherwise return second half 
'''



def trimstring(s1):
    #logic 
    
   vovel=0
   conconet=0
   for i in s1: 
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
            vovel=vovel+1
        else:
            conconet=conconet+1
   print (vovel,conconet)
   if vovel>conconet:
       #return first half of string 
       length=len[s1]
       mid=int(length/2)
       firsthalf=s1[0:mid]
       return firsthalf
   else:
       length=len(s1)
       mid=int(length/2)
       firsthalf=s1[mid:]
       return firsthalf
s1=(input("Enter first Word:- "))
result=trimstring(s1)
print(result)