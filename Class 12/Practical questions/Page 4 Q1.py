def binary(n):
    if n>1:
        binary(n//2)
    print(n%2,end='')
def octahedral(n):
    if num>7 or cnt==0:
        if cnt==0:
            return int((num%8)+octahedral(num//8,cnt+1))
        else:
            return int((num%8)*(10**cnt)+octahedral(num//8,cnt+1))
    elif num<=7 and num>0:
        return num*(10**cnt)
def hexadecimal(n):
    l=[]
    x=n//16
    if x<10:
        l.append(x)
    elif x==10:
        l.append('a')
    elif x==11:
        l.append('b')
    elif x==12:
        l.append('c')
    elif x==13:
        l.append('d')
    elif x==14:
        l.append('e')
    elif x==15:
        l.append('f')
    y=n%16
    if y<10:
        l.append(y)
    elif y>=10:
        z=y
        hexadecimal(z)
    return ''.join(map(str,l))
cont='y'
while cont!='n':
    number=int(input('Enter a number:'))
    option=(input('Desired type:'))
    if option=='B' or option=='b':
        print(binary(number))
    elif option=='O' or option=='o':
        print(octahedral(number))
    elif option=='H' or option=='h':
        print(hexadecimal(number))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'
