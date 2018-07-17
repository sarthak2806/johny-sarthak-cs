a=int(input("Enter the number you want to check for armstrong:"))
c=0
d=a
while a!=0:
    b=a%10
    c+=b*b*b
    a//=10
if c==d:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.")