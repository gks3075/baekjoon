word = input()
    
c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in c:
    word = word.replace(i, " ")

print(len(word))