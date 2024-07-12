n,m=map(int,input().split())

def swap(a,b):
    a,b=b,a
    return a,b

swap_n,swap_m=swap(n,m)
print(swap_n,swap_m)