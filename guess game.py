import random
num=random.randint(0,100)
cnt=0
while cnt<4:
    guess=int(input("Guess a number in range 0-100:"))
    if guess==num:
        print("It is correct")
        break
    else:
        print("Wrong guess")
        if cnt==2:
            print("Hint: The number is near",num-5)
        cnt+=1
if cnt==4:
    print("The correct answer is",num)

input("Press enter to continue...")
