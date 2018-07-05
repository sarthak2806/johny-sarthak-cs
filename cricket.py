from time import sleep
import random
over=int(input("Enter the number of overs:"))
result="000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222222222333333333333333333333333333333333333333444444444444444444444444444444445555555555555555555555555555555555566666666666666666OOOOOOOOO"
score=0
cnt=0
for i in range(0,over):
    for ball in range(1,7):
        p =''.join(random.sample(result,1))
        if p!='O':
            print("On the",ball,"st ball the result is",p)
            sleep(0.5)
            score+=int(p)
        else:
            if p=='O':
                print("It is an out!!!!!!")
                cnt+=1
                break
    print("\nOver",i+1,"finished\n")
    if cnt==10:
        break
print("Total score is",score,"runs for",cnt,"wickets")