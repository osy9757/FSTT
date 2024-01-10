from sys import stdin

input = stdin.readline

N = int(input())
children = [0]
dp = [1 for i in range(N + 1)]

for i in range(N):
    children.append(int(input()))

for i in range(1, N + 1):
    for j in range(1, i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))