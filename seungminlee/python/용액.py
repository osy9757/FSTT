N = int(input())
water = list(map(int, input().split()))

start = 0
end = N - 1
numbs = abs(water[start] + water[end])
answer = [water[start], water[end]]

while start < end:
    temp = water[start] + water[end]
    if abs(temp) < numbs:
        answer = [water[start], water[end]]
        numbs = abs(temp)

    if temp < 0:
        start += 1
    else:
        end -= 1

for i in answer:
    print(i, end=' ')