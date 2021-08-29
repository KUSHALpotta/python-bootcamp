lst=[]
n = int(input("Enter the total no of elements"))

for i in range(0,n):
    element=int(input("enter"))
    lst.append(element)

print(lst)
print(lst[0:3])

lst[0]=0
lst[4]=0
print(lst)
print(lst[0:3])

