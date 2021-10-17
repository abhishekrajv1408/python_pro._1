# This is a sample Python script.
# Variable and Data Types *****************************************************************************************
c=input('Enter your name :')
a=int(input('Enter the integral  value of a: '))
b=float(input('enter the floating point value b: '))

print('value of a+b ',a+b)
print("a*b: ",a*b)
print("a/b: ",a/b)
print("a-b: ",a-b)
print("your name is:  ",c)
print("data type of a is: ",(a))
print("data type of b is: ",type(b))
print("data type of c is:",type(c))



# *******************************String *****************************************************************************
print("###program related to STRING")
name = ' abhishek raj verma'
print(name[0: 17:3])
print(name[17: 0:-1])
print('Number of characters in name is: ', len(name))
print('Count the "a" characters in name: ', name.count("a"))
print('Replace a by n , the name become : ', name.replace('a','n'))

# ***************************************Lists and Tuples ***************************************************
# lists is mutable but tuples are immutables .
print('###Program related to LIST')
lists1 = ["abhishek", 3, 4, 5, 3.3, "raj"]
lists2 = ["rahul", "verma", 6, 8, 4.3, "rahul"]
print('Items in list1 is : ')
for i in range(0,6):
    print(lists1[i])
print("Items in list2: ")
for i in range(0, 6):
    print(lists2[i])
print('Now we have to update our lists, we add shyam in list1 and lov-kush in list2')
lists1.append('shyam')
lists2.append('lov-kush')
for i in range(0,7):
    print(lists1[i])
for i in range(0, 7):
    print(lists2[i])

# Tuple
print('###Program for tuple')
tuple=(1,1,1,1,12,3,4,5,6)
print(tuple.count(1))
print('What is the index value of 4: ',tuple.index(4))

#******************************************** Dictionary*************************************************************

print('###Program related to DICTNARY')
Gender= {
    "boy":"male",
    "girl":"femail",
    "sir":"male",
    "maam":"femail"
}
print(Gender["sir"])
print(Gender.items())
print(Gender.keys())
print(Gender.get("sir"))
print(Gender.get("maam"))
Gender.update({"teacher":"comman"})
print(Gender.items())
print(Gender.get("sir"))

#******************************************************SETs******************************************************
print("###Program related to SET")
b=set()
a=set()
b.add(3)
b.add(2)
b.add(1)
b.add(5)
a.add(0)
a.add(9)
a.add(9)
a.add(8)
a.add(7)
a.add(6)
a.add(5)
print(a)
print(b)
print(len(a))
print(len(b))
print(b.union(a))
print(b.intersection(a))

print(b)
print(a)

#*************************************FOR LOOP**********************************************************************
#PATTERN
print("###Program for print shapeof rectangle and triangle")
print('For rectangle press 1')
print('For rightangle triangle press 2')
a = int(input())

#*************************************FOR RECTANGLE******************************************************************
if a == 1:
    print('enter the length of sides')
    x = int(input())
    y = int(input())
    for i in range(1, x+1):
        for j in range(1, y+1):
            if j==y:
                print('*')
            elif j!=y:
                print('*',end=' ')

#****************************************FOR TRIANGLE**************************************************************

if a==2:
    x=int(input('Enter the  heigt side of rightangle triangle'))
    for i in range(1,x+1):
        for j in range(1,i+1):
            if j!=i:
                print('*',end=' ')
            else:
                print('*')



