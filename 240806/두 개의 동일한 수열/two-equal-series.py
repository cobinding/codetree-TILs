n = int(input())
arr1 = sorted(map(int,input().split()))
arr2 = sorted(map(int,input().split()))

print("Yes") if arr1 == arr2 else print("No")