k = 0
for i in range(1,6,2):
    for j in range(1,5-i+1):
        print(" ",end="")
    while (k != (2 * i)):
        if (k == 0 or k == 2 * i - 2) :
            print(1,end="")
        else :
            print(" ",end="")
        k+=1
    k = 0
    print("")
for i in range (7,0,-2):
    for j in range(0,6-i+1):
        print(" ",end="")
    k = 0
    while (k != (2 * i)) :
        if (k == 0 or k == 2 * i - 2) :
            print(1,end="")
        else :
            print(" ",end="")
        k+=1
     
    print("")