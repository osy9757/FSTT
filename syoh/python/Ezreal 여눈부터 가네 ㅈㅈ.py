N = int(input())
DP = [[0]*3 for _ in range(N+1)]
DP[1][1], DP[1][2] = 1, 1

for i in range(2, N):
    for j in range(3):
        DP[i][j] = DP[i-1][(j+1)%3] + DP[i-1][(j+5)%3]

print(DP[N-1][1]%1000000007)
