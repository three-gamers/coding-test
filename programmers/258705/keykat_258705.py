# https://school.programmers.co.kr/learn/courses/30/lessons/258705?language=python3

#     1,1     3,1             7,1
# 0,0 1,0 2,0 3,0 4,0 5,0 6,0 7,0  8,0
def solution(n, tops):
    dp = [[0 for _ in range(n)] for _ in range(2)]    
    if tops[0] == 1:
        dp[0][0] = 3 # 왼쪽, 위쪽, 각각 으로 해서 총 3개 케이스
        dp[1][0] = 1 # 오른쪽 해서 총 1개 케이스

    else:
        dp[0][0] = 2
        dp[1][0] = 1

    for i in range(1, n):
        if (tops[i] == 1):
            dp[0][i] = (dp[0][i - 1] * 3 + dp[1][i - 1] * 2) % 10007
        else:
            dp[0][i] = (dp[0][i - 1] * 2 + dp[1][i - 1]) % 10007

        dp[1][i] = (dp[0][i - 1] + dp[1][i - 1]) % 10007

    return (dp[0][n - 1] + dp[1][n - 1]) % 10007


ans = solution(4, [1,1,0,1])
print(ans)
