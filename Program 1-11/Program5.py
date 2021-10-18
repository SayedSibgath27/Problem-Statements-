#Read 5 element in a list and print the sum of all element 

b=list()
for i in range(5):
    num=int(input("Enter the number:-"))
    b.append(num)
print(b)
#logic
sum=0
for eachdata in b:
    sum=sum+eachdata
print(sum)

sum=0
firsthalf=b[0:2]
print(firsthalf)
for eachdata in firsthalf:
    sum=sum+eachdata
print(sum)