# 문자열 T로 시작하는 단어만 따로 리스트에 추출

n, k, t = input().split()
n = int(n)
k = int(k)

words = [input() for _ in range(n)]
t_words = []

for word in words :
    if t == word[:len(t)]:
        t_words.append(word)

t_words = sorted(t_words, key = lambda x : x)
print(t_words[k-1])