a=input("Enter a number you want to check for pallindrome:")
flag=0
for i in range (0,len(a)):
    b=len(a)-i-1
    if a[i]!=a[b]:
        flag=1
        break
if flag!=0:
    print('It is not a pallindrome')
else:
    print('It is a pallindrome')