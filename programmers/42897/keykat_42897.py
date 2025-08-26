# https://school.programmers.co.kr/learn/courses/30/lessons/42897#

def solution(money):
    dp1 = [0 for _ in money]
    dp2 = [0 for _ in money]
    
    dp1[0] = money[0]
    dp2[1] = money[1]
    
    dp1[1] = money[1]
    dp2[2] = money[2]
    
    dp1[2] = dp1[0] + money[2]
    dp2[3] = dp2[1] + money[3]
    
    for i in range(3, len(money) - 1):
        dp1[i] = max(dp1[i - 2], dp1[i - 3]) + money[i]
        
    for i in range(4, len(money)):
        dp2[i] = max(dp2[i - 2], dp2[i - 3]) + money[i]
        
        
    return max(max(dp1), max(dp2))