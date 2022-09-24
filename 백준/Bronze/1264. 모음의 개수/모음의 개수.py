#모음의 개수
while True:
    sentence = input()
    if sentence == '#':
        break
    vowel = ['a', 'e', 'i', 'o', 'u']
    sentence = sentence.lower()
    count = 0
    for x in sentence:
        if x in vowel:
            count += 1
    print(count)
