N = int(input())
nums = [int(input()) for _ in range(N)]
sum_num = 0

positive_num = sorted([ num for num in nums if num > 1], reverse = True)
negative_num = sorted([ num for num in nums if num < 0])
is_zero = False if 0 in nums else True

for i in range(0,len(positive_num)-1,2):
    sum_num += positive_num[i] * positive_num[i+1]

if (len(positive_num)%2 != 0):
    sum_num += positive_num[-1]

for i in range(0,len(negative_num)-1,2):
    sum_num += negative_num[i] * negative_num[i+1]

if (len(negative_num)%2 != 0) and is_zero:
    sum_num += negative_num[-1]

sum_num += sum([ num for num in nums if num == 1])
print(sum_num)