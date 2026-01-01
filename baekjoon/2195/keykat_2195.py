S = str(input())
P = str(input())

# S = 'abaabba'
# P = 'aaabbbabbbaaa'

# abaabba
# aaabbbabbbaaa

# S = 'aaaaaaaaaaa'
# P = 'aaaaaaaaaa'

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



    # print(pStr, count)

# print("index::", index)
# print("count:: ", count)

print(count)


