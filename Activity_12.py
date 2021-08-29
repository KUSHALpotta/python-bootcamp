def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

a=input("Enter 3 no's with space")
lst=a.split(" ")

great= greatest(lst[0],lst[1],lst[2])

print(great)
