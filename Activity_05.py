a = (input("Enter any 5 no's : "))

lst = a.split(' ')
sum=0

for i in lst:
    sum+=int(i)

print("%d"%(sum))
