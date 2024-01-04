from sys import stdin

input = stdin.readline

N = int(input())
x_planets = []
y_planets = []
z_planets = []
tunnel = []
parents = [i for i in range(N)]
answer = 0


def find_parent(num):
    if parents[num] != num:
        parents[num] = find_parent(parents[num])
    return parents[num]


def union_parents(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for i in range(N):
    x, y, z = map(int, input().split())
    x_planets.append((x, i))
    y_planets.append((y, i))
    z_planets.append((z, i))

x_planets.sort()
y_planets.sort()
z_planets.sort()

for i in x_planets, y_planets, z_planets:
    for j in range(1, N):
        tunnel.append((abs(i[j - 1][0] - i[j][0]), i[j - 1][1], i[j][1]))

tunnel.sort()

for i in tunnel:
    if find_parent(i[1]) != find_parent(i[2]):
        union_parents(i[1], i[2])
        answer += i[0]

print(answer)
