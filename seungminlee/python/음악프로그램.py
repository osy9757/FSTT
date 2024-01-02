from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
staff = []
singer = [[] for i in range(N + 1)]
degree = [0 for i in range(N + 1)]
answer = []
trial = deque()

for i in range(M):
    temp = list(map(int, input().split()))
    staff.append(temp[1:])

for i in staff:
    for j in range(len(i) - 1):
        degree[i[j + 1]] += 1
        singer[i[j]].append(i[j + 1])

for i in range(1, N + 1):
    if degree[i] == 0:
        trial.append(i)
        answer.append(i)

while trial:
    temp = trial.popleft()
    for i in singer[temp]:
        degree[i] -= 1
        if degree[i] == 0:
            trial.append(i)
            answer.append(i)

if len(answer) == N:
    for i in answer:
        print(i)
else:
    print(0)