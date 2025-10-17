def solve(diff, level, times, index):
    count = diff - level
    timeCur = times[index]
    timePrev = times[index - 1]

    if count <= 0:
        return timeCur

    return (diff - level) * (timeCur + timePrev) + timeCur


def solution(diffs, times, limit):
    start = 0
    end = max(diffs)
    level = 0
    

    while (start + end) // 2 != level:
        level = (start + end) // 2
        total = 0

        for index, diff in enumerate(diffs):
            total += solve(diff, level, times, index)

        if total < limit:
            end = level

        elif total > limit:
            start = level
            
        else:
            return level

    return level + 1