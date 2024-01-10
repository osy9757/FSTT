N = input()
length = len(N)
answer = set()


def create_num(left, right, recursion, temp_num):
    if recursion == length:
        answer.add(temp_num)

    else:
        if left - 1 >= 0:
            create_num(left - 1, right, recursion + 1, temp_num + ' > ' + N[left - 1:right + 1])

        if right + 1 < length:
            create_num(left, right + 1, recursion + 1, temp_num + ' > ' + N[left:right + 2])


for i in range(len(N)):
    create_num(i, i, 1, N[i])

print(len(answer))
