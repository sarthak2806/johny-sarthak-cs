a=input('Enter:')
b=input('Enter another:')
flag=0
if len(a)==len(b):
    for i in range (0,len(a)):
        b=len(a)-i-1
        if a[i]!=a[b]:
            flag=1
            break
if flag!=0:
    print('They are not equal.')
else:
    print('They are equal.')