# Creat a function by the name studentdatabase which accept studentname, studenttotalmarks, fathername. The function return the name of the all the students whose total marks is >=80. 

def studentdatabase(studentname, totalmarks, fathername):
    selectedstudent=list()
    for i in range(n):
        if totalmarks[i]>=80:
            name=studentname[i]
            selectedstudent.append(name)
    return selectedstudent



n=int(input("Enter the nomber of students:-"))
studentname=list()
totalmarks=list()
fathername=list()
for i in range(n):
    sname=(input("Enter the studentname:- "))
    studentname.append(sname)
    tmarks=int(input("Enter the totalmarks:- "))
    totalmarks.append(tmarks)
    fname=(input("Enter the fathername:- "))
    fathername.append(fname)
results=studentdatabase(studentname, totalmarks, fathername)
print(results)