def solution(picks, minerals):
    answer = 0
    Fatigue = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    current_pick = 0
    
    num = sum(picks) * 5
    if len(minerals)>sum(picks):
        minerals = minerals[:num]
    
    fiveMinerals = [minerals[i:i+5] for i in range(0,len(minerals),5)]
    mineralsToNum = [[0] * 3 for _ in range(len(fiveMinerals))]
    for i in range(len(fiveMinerals)):
        mineralsToNum[i][0] = fiveMinerals[i].count('diamond')
        mineralsToNum[i][1] = fiveMinerals[i].count('iron')
        mineralsToNum[i][2] = fiveMinerals[i].count('stone')
    mineralsToNum.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    
    for batch in mineralsToNum:
        while picks[current_pick] == 0:
            current_pick += 1
        
        answer += batch[0] * Fatigue[current_pick][0] + batch[1] * Fatigue[current_pick][1] + batch[2] * Fatigue[current_pick][2]       
        
        if current_pick <= 2:
            picks[current_pick] -= 1
            
        if sum(picks) == 0:
            break
    
    
    return answer