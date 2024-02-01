N = int(input())
dice = list(map(int,input().split()))

min_two = min([
    dice[0]+dice[1], dice[0]+dice[2], dice[0]+dice[3], dice[0]+dice[4],  
    dice[1]+dice[2], dice[1]+dice[3], dice[1]+dice[5], 
    dice[2]+dice[4], dice[2]+dice[5],  
    dice[3]+dice[4], dice[3]+dice[5]  
])


min_three = min([
    dice[0]+dice[1]+dice[3], dice[0]+dice[1]+dice[4], 
    dice[0]+dice[2]+dice[3], dice[0]+dice[2]+dice[4], 
    dice[5]+dice[1]+dice[3], dice[5]+dice[1]+dice[4], 
    dice[5]+dice[2]+dice[3], dice[5]+dice[2]+dice[4]  
])




print(min_two, min_three)
if N==1:
    print(sum(dice) - max(dice))
else:
    total = 4*min_three + (8*N-12)*min_two + (N-2)*(N-2)*5*min(dice) + (N-2)*4*min(dice)
    print(total)