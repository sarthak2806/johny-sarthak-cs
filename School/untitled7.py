a=input('Enter a sentence:')
b=''
cnt=1
b+=chr(ord(a[0])-32)
while cnt<len(a):
    if a[cnt]==' ':
        b+=a[cnt]
        b+=chr(ord(a[cnt+1])-32)
        cnt+=2
    else:
        b+=a[cnt]
        cnt+=1
print(b)