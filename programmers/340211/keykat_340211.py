def solution(points, routes):
    answer = 0
    robotRoutes = []

    for route in routes:
        move = []
        move.append(points[route[0] - 1])

        for pointIndex in range(1, len(route)):
            startIndex = route[pointIndex - 1] - 1
            endIndex = route[pointIndex] - 1  
            start = points[startIndex]
            end = points[endIndex]
            curr = start.copy()

            # y좌표 이동
            while curr[0] != end[0]:
                if curr[0] < end[0]:
                    move.append([curr[0] + 1, curr[1]])
                    curr[0] = curr[0] + 1

                elif curr[0] > end[0]:
                    move.append([curr[0] - 1, curr[1]])
                    curr[0] = curr[0] - 1

                else:
                    break

            # x좌표 이동
            while curr[1] != end[1]:
                if curr[1] < end[1]:
                    move.append([curr[0], curr[1] + 1])
                    curr[1] = curr[1] + 1

                elif curr[1] > end[1]:
                    move.append([curr[0], curr[1] - 1])
                    curr[1] = curr[1] - 1

                else:
                    break

        robotRoutes.append(move.copy())
        move.clear()

    for orderIndex in range(max(len(route) for route in robotRoutes)):
        collisionMap = [[0 for _ in range(102)] for _ in range(102)]
        for route in robotRoutes:
            if orderIndex < len(route):
                point = route[orderIndex]
                collisionMap[point[0]][point[1]] += 1

        for row in collisionMap:
            for col in row:
                if col > 1:
                    answer += 1

    return answer
