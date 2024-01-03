N = int(input())
solution = list(map(int, input().split()))

solution = sorted(solution)


def binary_search():
    answer = 3 * 1e9 + 1
    answer_num = []
    for i in range(N - 2):
        start = i + 1
        end = N - 1
        while start < end:
            temp = solution[i] + solution[start] + solution[end]

            if answer > abs(temp):
                answer_num = [solution[i], solution[start], solution[end]]
                answer = abs(temp)

            if temp > 0:
                end -= 1
            elif temp < 0:
                start += 1
            elif temp == 0:
                answer_num = [solution[i], solution[start], solution[end]]
                return answer_num

    return answer_num


ans = binary_search()
for i in ans:
    print(i, end=' ')
    