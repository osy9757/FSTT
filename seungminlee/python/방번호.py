from sys import stdin

input = stdin.readline
room = []

N = int(input())
room = list(map(int, input().split()))
M = int(input())
if N > 1:
    first_num = [1, room[1]]
    max_len = 0
    room_num = 0
    min_cost = room[0]
    answer = []

    for i in range(1, N):
        if room[room_num] >= room[i]:
            room_num = i
            min_cost = room[i]
        if first_num[1] >= room[i]:
            first_num = [i, room[i]]

    if first_num[1] <= M:
        answer.append(first_num[0])
        money = M - first_num[1]
        max_len = money // min_cost
        money = money - min_cost * max_len
        for i in range(max_len):
            answer.append(room_num)

        for i in range(len(answer)):
            for j in range(N - 1, answer[i], -1):
                if money >= room[j] - room[answer[i]]:
                    money = money - (room[j] - room[answer[i]])
                    answer[i] = j
                    break

        for i in answer:
            print(i, end='')

    else:
        print(0)
else:
    print(0)
