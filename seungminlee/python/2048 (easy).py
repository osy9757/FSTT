import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
real_board = []
answer = 0


def move(count, board):
    if count == 5:
        global answer
        for i in range(N):
            answer = (max(answer, max(board[i])))
        return

    temp_board = deepcopy(board)

    for i in range(4):
        board = deepcopy(temp_board)
        if i == 0:
            # 아래로
            for k in range(N):
                cursor = N - 1
                for j in range(N - 2, -1, -1):
                    if board[j][k]:
                        temp = board[j][k]
                        board[j][k] = 0
                        if board[cursor][k] == 0:
                            board[cursor][k] = temp
                        elif board[cursor][k] == temp:
                            board[cursor][k] *= 2
                            cursor -= 1
                        else:
                            cursor -= 1
                            board[cursor][k] = temp

            move(count + 1, board)

        elif i == 1:
            # 위로
            for k in range(N):
                cursor = 0
                for j in range(1, N):
                    if board[j][k]:
                        temp = board[j][k]
                        board[j][k] = 0
                        if board[cursor][k] == 0:
                            board[cursor][k] = temp
                        elif board[cursor][k] == temp:
                            board[cursor][k] *= 2
                            cursor += 1
                        else:
                            cursor += 1
                            board[cursor][k] = temp

            move(count + 1, board)

        elif i == 2:
            # 왼쪽
            for k in range(N):
                cursor = 0
                for j in range(1, N):
                    if board[k][j]:
                        temp = board[k][j]
                        board[k][j] = 0
                        if board[k][cursor] == 0:
                            board[k][cursor] = temp
                        elif board[k][cursor] == temp:
                            board[k][cursor] *= 2
                            cursor += 1
                        else:
                            cursor += 1
                            board[k][cursor] = temp

            move(count + 1, board)

        elif i == 3:
            # 오른쪽
            for k in range(N):
                cursor = N - 1
                for j in range(N - 2, -1, -1):
                    if board[k][j]:
                        temp = board[k][j]
                        board[k][j] = 0
                        if board[k][cursor] == 0:
                            board[k][cursor] = temp
                        elif board[k][cursor] == temp:
                            board[k][cursor] *= 2
                            cursor -= 1
                        else:
                            cursor -= 1
                            board[k][cursor] = temp

            move(count + 1, board)


for i in range(N):
    real_board.append(list(map(int, input().rstrip().split())))

move(0, real_board)

print(answer)