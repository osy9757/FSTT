import sys
input = sys.stdin.readline

# 함수: 최대공약수(Greatest Common Divisor) 계산
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

# 함수: 최소공배수(Least Common Multiple) 계산
def LCM(a, b):
    return a * b // GCD(a, b)

# 함수: 이진수에서 1의 개수 계산
def count_one(mask):
    cnt = 0
    for i in range(0, 7):
        if mask & (1 << i) != 0:
            cnt += 1
    return cnt

# 함수: 주어진 마스크에 해당하는 최소공배수 계산
def LCMs(mask):
    ret = 1;
    for i in range(0, 7):
        if mask & (2 ** i) != 0:
            ret = LCM(ret, arr[i])
    return ret

# 입력: N 값
N = int(input())

# 주어진 숫자 패턴 : 소수 2, 3, 5, 7, 11, 13, 17
arr = [11, 111, 11111, 1111111, 11111111111, 1111111111111, 11111111111111111]

# 초기값: 결과 변수 ret에 N 대입
ret = N;

# 모든 경우의 수에 대해 반복
for i in range(0, (2 ** 7)):
    # 이진수로 표현했을 때 1의 개수가 짝수이면 빼기, 홀수이면 더하기
    if count_one(i) % 2 == 0:
        ret -= N // LCMs(i)
    else:
        ret += N // LCMs(i)

# 결과 출력
print(ret)