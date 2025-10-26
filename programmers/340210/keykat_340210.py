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
            print(aCurrIndex, bCurrIndex)

            if int(listA[aCurrIndex]) < int(listB[bCurrIndex]):
                tempIndex = aCurrIndex - 1
                while int(listA[aCurrIndex]) <= 0:
                    listA[tempIndex] = n - 1
                    tempIndex = tempIndex - 1

                print("tempIndex:", tempIndex)

                listA[tempIndex] = str(int(listA[tempIndex]) - 1)
                listA[aCurrIndex] = str(n - int(listB[bCurrIndex]) + int(listA[aCurrIndex]))
            
            else:
                listA[aCurrIndex] = str(int(listA[aCurrIndex]) - int(listB[bCurrIndex]))

        print(listA, listB)

    elif exp == '+':
        for idx, _ in enumerate(cStr):
            aCurrIndex = len(aStr) - idx - 1
            bCurrIndex = len(bStr) - idx - 1
            print(aCurrIndex, bCurrIndex)

            if int(listA[aCurrIndex]) + int(listB[bCurrIndex]) >= n:
                tempIndex = aCurrIndex - 1
                while int(listA[aCurrIndex]) <= 0:
                    listA[tempIndex] = n + 1
                    tempIndex = tempIndex - 1

                print("tempIndex:", tempIndex)

                listA[tempIndex] = str(int(listA[tempIndex]) + 1)
                listA[aCurrIndex] = str(int(listB[bCurrIndex]) + int(listA[aCurrIndex]) - n)
            
            else:
                listA[aCurrIndex] = str(int(listB[bCurrIndex]) + int(listA[aCurrIndex]))

        print(listA, listB)




def solution(expressions):
    answer = []
    return answer



result = calc(14, 3, '-', 8)
print(result)