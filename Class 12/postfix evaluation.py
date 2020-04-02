postfix=[10,20,'+',5,9,'*','-']
operation=['**','*','/','%','+','-']
stack=[]
for i in postfix:
    if i not in operation:
        stack.append(i)
    else:
        num1=stack.pop()
        num2=stack.pop()
        if i=='**':
            stack.append(num1**num2)
        if i=='*':
            stack.append(num1*num2)
        if i=='+':
            stack.append(num1+num2)
        if i=='/':
            stack.append(num1/num2)
        if i=='-':
            stack.append(num1-num2)
        if i=='%':
            stack.append(num1%num2)
print(stack[0])