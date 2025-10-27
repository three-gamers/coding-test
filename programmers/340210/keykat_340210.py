def calc(a, b, exp, n):
    aStr = str(a)
    bStr = str(b)

    li = [str(i) for i in range(n, 10)]
    if any(n in aStr for n in li) or any(n in bStr for n in li):
        return -1

    cStr = bStr if len(aStr) > len(bStr) else aStr
    result = '' 

    listA = list(aStr)
    listB = list(bStr)

    if exp == '-':
        for idx, _ in enumerate(cStr):
            aCurrIndex = len(aStr) - idx - 1
            bCurrIndex = len(bStr) - idx - 1

            if int(listA[aCurrIndex]) < int(listB[bCurrIndex]):
                tempIndex = aCurrIndex - 1
                while int(listA[tempIndex]) <= 0:
                    listA[tempIndex] = n - 1
                    tempIndex = tempIndex - 1
                

                listA[tempIndex] = str(int(listA[tempIndex]) - 1)
                listA[aCurrIndex] = str(n - int(listB[bCurrIndex]) + int(listA[aCurrIndex]))
            
            else:
                listA[aCurrIndex] = str(int(listA[aCurrIndex]) - int(listB[bCurrIndex]))

    elif exp == '+':
        for idx, _ in enumerate(cStr):
            aCurrIndex = len(aStr) - idx - 1
            bCurrIndex = len(bStr) - idx - 1

            if int(listA[aCurrIndex]) + int(listB[bCurrIndex]) >= n:
                tempIndex = aCurrIndex - 1
                if tempIndex != -1:
                    listA[tempIndex] = str(int(listA[tempIndex]) + 1)

                    while int(listA[tempIndex]) == n - 1:
                        listA[tempIndex] = str(int(listA[tempIndex]) + 1)
                        tempIndex = tempIndex - 1

                        if tempIndex == -1:
                            break

                listA[aCurrIndex] = str(int(listB[bCurrIndex]) + int(listA[aCurrIndex]) - n)
                if tempIndex == -1:
                    listA.insert(0, '1')

            else:
                listA[aCurrIndex] = str(int(listB[bCurrIndex]) + int(listA[aCurrIndex]))

    return int(''.join(listA))




def solution(expressions):
    answer = []

    maxFormation = 0
    for exp in expressions:
        expList = exp.split(' ')
        a = expList[0]
        b = expList[2]

        # a와 b의 각 자릿수를 int로 변환하여 최대값 찾기
        maxFormation = max(maxFormation, max(map(int, a)) + 1)
        maxFormation = max(maxFormation, max(map(int, b)) + 1)

    possibleFormations = list(range(maxFormation, 10))
    for exp in expressions:
        expList = exp.split(' ')
        a = expList[0]
        e = expList[1]
        b = expList[2]
        res = expList[4]
        formations = set()

        if res != 'X':
            for i in range(maxFormation, 10):
                if int(res) == calc(int(a), int(b), e, i):
                    # print('i::::::', i)
                    formations.add(i)

                # print(int(res), calc(int(a), int(b), e, i))

            if len(formations) == 1:
                # print("sdfdasfdas: ", formations)
                possibleFormations = [formations.pop()]
                break

            # print("formations::: ", formations)
    
            for pf in possibleFormations:
                if pf not in formations:
                    possibleFormations.remove(pf)

    # print(possibleFormations)

    for exp in expressions:
        expList = exp.split(' ')
        a = expList[0]
        e = expList[1]
        b = expList[2]
        equal = expList[3]
        res = expList[4]
        results = set()

        if res == 'X':
            for form in possibleFormations:
                results.add(calc(int(a), int(b), e, form))

        else:
            continue

        if len(results) == 0 or len(results) > 1:
            answer.append(a + ' ' + e + ' ' + b + ' ' + equal + ' ' + '?')
        else:
            answer.append(a + ' ' + e + ' ' + b + ' ' + equal + ' ' + str(results.pop()))


    return answer





# print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
# print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))