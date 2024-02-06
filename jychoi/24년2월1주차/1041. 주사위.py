import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0
min_lists = []

if N == 1: # 주사위 1개일 때
    arr.sort()
    for i in range(5):
        ans += arr[i]
else:
    # 주사위 여러개인 경우, 마주보는 면 중 작은 값을 선택하여 리스트에 저장
    min_lists.append(min(arr[0], arr[5]))
    min_lists.append(min(arr[1], arr[4]))
    min_lists.append(min(arr[2], arr[3]))
    min_lists.sort()

    # 1, 2, 3개의 면을 보았을 때의 최소값
    min1 = min_lists[0]
    min2 = min_lists[0] + min_lists[1]
    min3 = sum(min_lists)

    # 각 경우에 대한 주사위 개수 계산
    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    # 최종 정답 계산
    ans += min1 * n1
    ans += min2 * n2
    ans += min3 * n3

# 결과 출력
print(ans)
