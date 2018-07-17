num=int(input("Enter a number:"))
num1=num+1
for i in range(2,num1):
    if num%i==0:
        break
else:
    d=num
    c=0
    while d!=0:
        b=d%10
        c=c*10+b
        d=d//10
    if num==c:
        print(num,"is a palinprime")