#Read the txt file and print the total number of vovel into it. 
file=open("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Dataanalytic\\database.txt",'r')
content=file.read()
print(content)

#prepare list of character
data=list(content)
print(data)

#Logic
count=0
count1=0

for i in(data):
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
    else:
        count1=count+1        
print(count)
print(count1)