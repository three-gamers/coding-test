def moveDirection(curr, nextCurr, dir, map):
    result = 0

    # nextCurr가 밖이면 뿌릴 모래가 없음
    if nextCurr[0] >= len(map) or nextCurr[0] < 0 or nextCurr[1] >= len(map) or nextCurr[1] < 0:
        return 0

    currSand = map[nextCurr[1]][nextCurr[0]]  # 분산 기준은 nextCurr

    # dir[1:] 비율 먼저 뿌리기 (정수 내림)
    for d in dir[1:]:
        newDir = (nextCurr[0] + d[0], nextCurr[1] + d[1])
        amount = int(currSand * d[2])
        if newDir[0] >= len(map) or newDir[0] < 0 or newDir[1] >= len(map) or newDir[1] < 0:
            result += amount
        else:
            map[newDir[1]][newDir[0]] += amount
        map[nextCurr[1]][nextCurr[0]] -= amount

    # 알파(남은 모래): dir[0] 위치
    alphaPos = (nextCurr[0] + dir[0][0], nextCurr[1] + dir[0][1])
    alpha = map[nextCurr[1]][nextCurr[0]]
    if alphaPos[0] >= len(map) or alphaPos[0] < 0 or alphaPos[1] >= len(map) or alphaPos[1] < 0:
        result += alpha
    else:
        map[alphaPos[1]][alphaPos[0]] += alpha

    map[nextCurr[1]][nextCurr[0]] = 0
    return result

        

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
result = 0

curr = (N // 2, N // 2)

l = [(-1, 0, 0), (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01), (-1, -1, 0.1), (-1, 1, 0.1), (-2, 0, 0.05)]
r = [(1, 0, 0), (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (-1, -1, 0.01), (-1, 1, 0.01), (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)]
u = [(0, -1, 0), (2,  0, 0.02), (1,  0, 0.07), (-1,  0, 0.07), (-2,  0, 0.02), (1,  1, 0.01), (-1,  1, 0.01), (1, -1, 0.1),  (-1, -1, 0.1), (0, -2, 0.05)]
d = [(0,  1, 0), (-2, 0, 0.02), (-1, 0, 0.07), (1,  0, 0.07), (2,  0, 0.02), (-1, -1, 0.01), (1, -1, 0.01), (-1,  1, 0.1),  (1,  1, 0.1), (0,  2, 0.05)]

# left 1번, down 1번
# right 2번, up 2번
# left 3번, down 3번
# right 4번, up 4번
# left 5번, down 5번
# 이렇게해서 right가 N번일 때까지 반복

# 이 때 curr 좌표 + l 배열의 좌표가 밖으로 튀어나가면 연산

for i in range(N - 1):
        # right, up 방향
        if i % 2 != 0:
            for ii in range(i + 1):
                nextCurr = (curr[0] + 1, curr[1])
                result += moveDirection(curr, nextCurr, r, map)
                curr = nextCurr

                # for y in map:
                #     print(y)
                # print("\n")

                if curr[0] < 0 or curr[0] >= len(map) or curr[1] < 0 or curr[1] >= len(map):
                    break

            for ii in range(i + 1):
                nextCurr = (curr[0], curr[1] - 1)
                result += moveDirection(curr, nextCurr, u, map)
                curr = nextCurr

                # for y in map:
                #     print(y)
                # print("\n")

                if curr[0] < 0 or curr[0] >= len(map) or curr[1] < 0 or curr[1] >= len(map):
                    break


        # left, down 방향
        else: 
            for ii in range(i + 1):
                nextCurr = (curr[0] - 1, curr[1])
                result += moveDirection(curr, nextCurr, l, map)
                curr = nextCurr


                # for y in map:
                #     print(y)
                # print("\n")

                if curr[0] < 0 or curr[0] >= len(map) or curr[1] < 0 or curr[1] >= len(map):
                    break

            for ii in range(i + 1):
                nextCurr = (curr[0], curr[1] + 1)
                result += moveDirection(curr, nextCurr, d, map)
                curr = nextCurr


                # for y in map:
                #     print(y)
                # print("\n")

                if curr[0] < 0 or curr[0] >= len(map) or curr[1] < 0 or curr[1] >= len(map):
                    break

        if curr[0] < 0 or curr[0] >= len(map) or curr[1] < 0 or curr[1] >= len(map):
            break

for _ in range(N - 1):               # 추가
    nextCurr = (curr[0] - 1, curr[1])
    result += moveDirection(curr, nextCurr, l, map)
    curr = nextCurr

print(int(result))


