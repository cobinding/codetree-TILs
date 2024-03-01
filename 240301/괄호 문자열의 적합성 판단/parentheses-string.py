s=input()

stack=[]
for i in s:
    if i == '(':
        stack.append("(")
    elif i == ')':
        if len(stack) == 0 :
            stack.append(")")
        else:
            stack.pop()

print("Yes") if len(stack) == 0 else print("No")