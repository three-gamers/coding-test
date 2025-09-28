def moveDirection(curr, dir, map, result):
    currSand = map[curr[1]][curr[0]]

    for d in dir:
        newDir = (curr[0] + d[0], curr[1] + d[1])
        # 빠져나간 모래 양
        if newDir[0] >= len(map) or newDir[0] < 0 or newDir[1] >= len(map) or newDir[1] < 0:
            result += (currSand * d[2] * 100) // 100
        else:
            map[newDir[1]][newDir[0]] += (currSand * d[2] * 100) // 100
    
    map[curr[1]][curr[0]] = 0

    print(map)
        

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
result = 0

curr = (N // 2, N // 2)

l = [(-1, 0, 0.55), (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01), (-1, -1, 1), (-1, 1, 1), (-2, 0, 0.05)]
r = [(1, 0, 0.55), (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (-1, -1, 0.01), (-1, 1, 0.01), (1, -1, 1), (1, 1, 1), (2, 0, 0.05)]
u = [(0, -1, 0.55), (-2, -1, 0.02), (-1, -1, 0.07), (1, -1, 0.07), (2, -1, 0.02), (-1, 0, 0.01), (1, 0, 0.01), (-1, -2, 1), (1, -2, 1), (0, -2, 0.05)]
d = [(0, 1, 0.55), (-2, 1, 0.02), (-1, 1, 0.07), (1, 1, 0.07), (2, 1, 0.02), (-1, 0, 0.01), (1, 0, 0.01), (-1, 2, 1), (1, 2, 1), (0, 2, 0.05)]

# left 1번, down 1번
# right 2번, up 2번
# left 3번, down 3번
# right 4번, up 4번
# left 5번, down 5번
# 이렇게해서 right가 N번일 때까지 반복

# 이 때 curr 좌표 + l 배열의 좌표가 밖으로 튀어나가면 연산

for i in range(N):
    for ii in range(i):
        # right, up 방향
        if i % 2 == 0:
            curr = (curr[0], curr[1] + 1)
            moveDirection(curr, r, map, result)

            curr = (curr[0] - 1, curr[1])
            moveDirection(curr, d, map, result)
        # left, down 방향
        else: 
            curr = (curr[0], curr[1] - 1)
            moveDirection(curr, r, map, result)

            curr = (curr[0] + 1, curr[1])
            moveDirection(curr, d, map, result)

print(result)


