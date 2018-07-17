a=rev=int(input("Enter the number you want to to check for pallandrom number: "))
c=0
while a!=0:
    b=a%10
    c=c*10+b
    a=a/10
if c==rev:
    print("The number is pallandrom number.")
    if c==2 or c==3 or c==5 or c==7:
        print("It is a prime number.")
    else:
        if c%2==0 or c%3==0 or c%5==0 or c%7==0:
            print("It is not a prime number.")
        else:
            print("It is a prime number.")
else:
    print("The number is not a pallandrom number.")