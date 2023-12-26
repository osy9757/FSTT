import sys

input = sys.stdin.readline


def find_answer():
    for i in range(len(trial)):
        if degree[trial[i]] == 0:
            answer.append(trial[i])
            for j in preceding[trial[i]]:
                degree[j] -= 1
            trial.pop(i)
            return


N, M = map(int, input().split())
problems = []
trial = [i for i in range(1, N + 1)]
degree = [0 for i in range(N + 1)]
answer = []
preceding = [[] for i in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    degree[B] += 1
    preceding[A].append(B)

while len(answer) != N:
    find_answer()

for i in answer:
    print(i, end=' ')