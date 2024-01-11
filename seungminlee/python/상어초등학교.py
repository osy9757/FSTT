from sys import stdin

input = stdin.readline

N = int(input())
classroom = [[0 for i in range(N)] for j in range(N)]
like_list = [[] for i in range(N ** 2)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def find_seat(likes):
    seats = [0, 0]
    like_count = -1
    for i in range(N):
        for j in range(N):
            temp_count = 0
            for k in range(4):
                temp_x = i + dx[k]
                temp_y = j + dy[k]
                if 0 <= temp_x < N and 0 <= temp_y < N:
                    if classroom[temp_x][temp_y] in likes:
                        temp_count += 10
                    elif classroom[temp_x][temp_y] == 0:
                        temp_count += 1

            if like_count < temp_count and not classroom[i][j]:
                seats = [i, j]
                like_count = temp_count

    return seats


for i in range(N ** 2):
    temp = list(map(int, input().split()))
    student = temp[0]
    like_list[student - 1] = temp[1:]
    seated = find_seat(like_list[student - 1])
    classroom[seated[0]][seated[1]] = student

for i in range(N):
    for j in range(N):
        student = classroom[i][j]
        count = 0
        for k in range(4):
            temp_x = i + dx[k]
            temp_y = j + dy[k]
            if 0 <= temp_x < N and 0 <= temp_y < N:
                if classroom[temp_x][temp_y] in like_list[student - 1]:
                    if count:
                        count *= 10
                    else:
                        count = 1

        answer += count

print(answer)