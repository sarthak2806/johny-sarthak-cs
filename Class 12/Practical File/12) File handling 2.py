f=open('12) text handling 1.txt','a')
a=input('Enter the line you want to insert:')
f.write(a+'\n')
f=open('12) text handling 1.txt','r')
l=f.readlines()
print(l[-1])