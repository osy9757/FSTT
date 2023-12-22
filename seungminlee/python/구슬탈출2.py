# #: 장애물, 벽  .:빈 칸   O: 골인 지점,  R: 빨간 구슬의 위치,  B: 파란 구슬의 위치
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(red_dot, blue_dot):
    next_point = deque([[red_dot[0], red_dot[1], blue_dot[0], blue_dot[1]]])
    visited = [[red_dot[0], red_dot[1], blue_dot[0], blue_dot[1]]]
    answer = 0

    while next_point:
        answer += 1
        if answer > 10:
            return -1
        point = deepcopy(next_point)
        next_point = deque([])
        while point:
            red_x, red_y, blue_x, blue_y = point.popleft()
            for i in range(4):
                next_red_x = red_x + dx[i]
                next_red_y = red_y + dy[i]
                next_blue_x = blue_x + dx[i]
                next_blue_y = blue_y + dy[i]

                while True:
                    if board[next_red_x][next_red_y] == '#':
                        next_red_x -= dx[i]
                        next_red_y -= dy[i]
                        break
                    elif board[next_red_x][next_red_y] == 'O':
                        break
                    next_red_x += dx[i]
                    next_red_y += dy[i]

                while True:
                    if board[next_blue_x][next_blue_y] == '#':
                        next_blue_x -= dx[i]
                        next_blue_y -= dy[i]
                        break
                    elif board[next_blue_x][next_blue_y] == 'O':
                        break
                    next_blue_x += dx[i]
                    next_blue_y += dy[i]

                if board[next_blue_x][next_blue_y] == 'O':
                    continue
                elif board[next_red_x][next_red_y] == 'O':
                    return answer
                elif next_blue_y == next_red_y and next_blue_x == next_red_x:
                    if abs(red_x - next_red_x) + abs(red_y - next_red_y) > \
                            abs(blue_x - next_blue_x) + abs(blue_y - next_blue_y):
                        next_red_x -= dx[i]
                        next_red_y -= dy[i]
                    else:
                        next_blue_x -= dx[i]
                        next_blue_y -= dy[i]

                if [next_red_x, next_red_y, next_blue_x, next_blue_y] not in visited:
                    next_point.append([next_red_x, next_red_y, next_blue_x, next_blue_y])

    else:
        return -1


board = []
N, M = map(int, input().split())
for i in range(N):
    temp = str(input().rstrip())
    board.append(list(temp))

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_point = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue_point = [i, j]
            board[i][j] = '.'

print(bfs(red_point, blue_point))
