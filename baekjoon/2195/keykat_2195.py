# https://www.acmicpc.net/problem/2195

S = str(input())
P = str(input())

index = 0
count = 0
while index < len(P):
    pStr = P[index]

    if index + 1 < len(P):
        while index + 1 < len(P):
            index += 1
            tempStr = pStr + P[index]

            if tempStr in S:
                pStr = tempStr

            else:
                count += 1
                break
    
    else:
        index += 1
        count += 1

print(count)


