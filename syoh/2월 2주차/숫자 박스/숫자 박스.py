import sys

def max_value_of_number_box(N, top_row, bottom_row):
    DT = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                DT[i][j][k] = max(
                    DT[i][j][k-1],  
                    DT[i-1][j][k-1] + top_row[i-1] * 0 if top_row[i-1] != 0 else DT[i-1][j][k-1], 
                    DT[i][j-1][k-1] + 0 * bottom_row[j-1] if bottom_row[j-1] != 0 else DT[i][j-1][k-1],  
                    DT[i-1][j-1][k-1] + top_row[i-1] * bottom_row[j-1] if top_row[i-1] != 0 and bottom_row[j-1] != 0 else DT[i-1][j-1][k-1]  
                )

    return DT[N][N][N]

N = int(input())
A1 = list(map(int,sys.stdin.readline().split()))
A2 = list(map(int,sys.stdin.readline().split()))

print(max_value_of_number_box(N, A1, A2))


아직 다 안품