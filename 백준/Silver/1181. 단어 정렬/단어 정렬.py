# 단어 정렬
N = int(input())
words = list(input() for _ in range(N))
words = list(set(words))
words.sort(key=lambda x : [len(x)] + [ord(x[i]) for i in range(len(x))])

for i in range(len(words)):
    print(words[i])