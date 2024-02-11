import sys
input = sys.stdin.readline


def count(num):
    cnt = 0
    # 주어진 숫자를 이진수로 변환하여 저장
    bin_num = bin(num)[2:]
    # 이진수의 길이 구하기
    length = len(bin_num)

    # 이진수를 뒤에서부터 순회하면서 1의 개수 계산
    for i in range(length):
        if bin_num[i] == '1':
            # 현재 자릿수의 2의 거듭제곱 값
            val = length - i - 1
            # 현재 자릿수까지의 1의 개수를 누적
            cnt += one_sum[val]
            # 가장 큰 2의 거듭제곱 수까지의 1의 개수를 더해줌
            cnt += (num - 2 ** val + 1)
            # 다음 자릿수 계산을 위해 현재 자릿수 제외
            num = num - 2 ** val

    # 최종적으로 계산된 1의 개수 반환
    return cnt

# 입력 받기
x, y = map(int, input().split())

# 각 자릿수의 1의 개수를 저장하는 리스트 초기화 (log2(10**16))
one_sum = [0 for _ in range(60)]

# one_sum 리스트 계산
for i in range(1, 60):
    # 현재 자릿수까지의 1의 개수를 계산하기 위해 2의 거듭제곱을 사용, i - 1은 현재 자릿수
    one_sum[i] = 2 ** (i - 1) + 2 * one_sum[i - 1]

# A부터 B까지의 1의 개수 합을 계산하고 출력
print(count(y) - count(x - 1))