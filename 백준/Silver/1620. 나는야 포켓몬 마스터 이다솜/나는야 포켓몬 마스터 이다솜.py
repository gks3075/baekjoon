# 포켓몬
N, M = map(int, input().split())
pokedex = {}
inv = {}
for i in range(N):
    pokemon = input()
    pokedex[pokemon] = i + 1
    inv[i + 1] = pokemon

for j in range(M):
    a = input()
    try:
        a = int(a)
        print(inv[a])
    except:
        print(pokedex[a])
