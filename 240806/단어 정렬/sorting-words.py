n = int(input())
dictionary = [input() for _ in range(n)]
sorted_dic = sorted(dictionary)

for item in sorted_dic:
    print(item)