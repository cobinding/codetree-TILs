n=int(input())

stack=[]
for _ in range(n):
    s=input()
    if s[:4] == 'push':
        comm, num = s.split()
        stack.append(num)
    elif s == 'pop':
        num = stack.pop()
        print(num)
    elif s == 'top':
        print(stack[-1])
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
       print(1) if len(stack) == 0 else print(0)