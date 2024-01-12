import copy
from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
node = []
parents = [0 for i in range(N + 1)]
connection = [[] for i in range(N + 1)]
degree = [0] * (N + 1)
answer = [-1] * (N + 1)

for i in range(N):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
    degree[a] += 1
    degree[b] += 1

temp_connect = copy.deepcopy(connection)

while True:
    trigger = True
    for i in range(1, N + 1):
        if degree[i] == 1:
            parent = temp_connect[i].pop()
            parents[i] = parent
            degree[i] -= 1
            degree[parent] -= 1
            temp_connect[parent].remove(i)
            trigger = False

    if trigger:
        break

deque = deque()
for i in range(N + 1):
    if not parents[i]:
        answer[i] = 0
        deque.append(i)

while deque:
    station = deque.popleft()
    for i in connection[station]:
        if answer[i] == -1:
            answer[i] = answer[station] + 1
            deque.append(i)

for i in range(1, N + 1):
    print(answer[i], end=' ')
