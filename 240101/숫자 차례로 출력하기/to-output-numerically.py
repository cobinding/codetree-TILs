n=int(input())

def print_sorted(n):
    if n == 0 : return
    print_sorted(n-1)
    print(n, end = ' ')
    
def print_reversed_sorted(n):
    if n == 0 : return
    print(n, end = ' ')
    print_reversed_sorted(n-1)
    
print_sorted(n)
print("")
print_reversed_sorted(n)