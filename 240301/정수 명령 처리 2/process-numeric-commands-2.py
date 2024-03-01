n=int(input())

q=[]
for _ in range(n):
    s=input()
    
    if s[:4] == "push":
        comm, num = s.split()
        q.append(num)
    elif s == "front":
        print(q[0])
    elif s == "size":
        print(len(q))
    elif s == "pop":
        print(q[0])
        q.remove(q[0])
    elif s == "empty":
        print(1) if len(q) == 0 else print(0)