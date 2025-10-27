def calc(a, b, exp, n):
    """진법 n에서 a와 b의 연산 결과를 반환"""
    # 진법 n 이상의 숫자가 포함되어 있으면 불가능
    a_str = str(a)
    b_str = str(b)
    
    for digit in a_str:
        if int(digit) >= n:
            return -1
    for digit in b_str:
        if int(digit) >= n:
            return -1
    
    # 10진법으로 변환
    a_decimal = 0
    b_decimal = 0
    
    for i, digit in enumerate(reversed(a_str)):
        a_decimal += int(digit) * (n ** i)
    
    for i, digit in enumerate(reversed(b_str)):
        b_decimal += int(digit) * (n ** i)
    
    # 연산 수행
    if exp == '+':
        result_decimal = a_decimal + b_decimal
    elif exp == '-':
        result_decimal = a_decimal - b_decimal
        if result_decimal < 0:
            return -1
    else:
        return -1
    
    # 결과를 진법 n으로 변환
    if result_decimal == 0:
        return 0
    
    result_n = ""
    while result_decimal > 0:
        result_n = str(result_decimal % n) + result_n
        result_decimal //= n
    
    return int(result_n)


def solution(expressions):
    answer = []
    
    # 최소 진법 찾기
    min_base = 2
    for exp in expressions:
        exp_list = exp.split(' ')
        a = exp_list[0]
        b = exp_list[2]
        
        for digit in a + b:
            min_base = max(min_base, int(digit) + 1)
    
    # 가능한 진법들 찾기
    possible_bases = set(range(min_base, 10))
    
    # 알려진 식들로 가능한 진법들을 좁혀나가기
    for exp in expressions:
        exp_list = exp.split(' ')
        a = exp_list[0]
        e = exp_list[1]
        b = exp_list[2]
        res = exp_list[4]
        
        if res != 'X':
            valid_bases = set()
            for base in range(min_base, 10):
                if calc(int(a), int(b), e, base) == int(res):
                    valid_bases.add(base)
            
            # 교집합으로 가능한 진법 업데이트
            possible_bases = possible_bases.intersection(valid_bases)
            
            # 가능한 진법이 없으면 빈 배열 반환
            if not possible_bases:
                return []
    
    # X가 있는 식들의 결과 계산
    for exp in expressions:
        exp_list = exp.split(' ')
        a = exp_list[0]
        e = exp_list[1]
        b = exp_list[2]
        equal = exp_list[3]
        res = exp_list[4]
        
        if res == 'X':
            results = set()
            for base in possible_bases:
                result = calc(int(a), int(b), e, base)
                if result != -1:
                    results.add(result)
            
            if len(results) == 1:
                answer.append(f"{a} {e} {b} {equal} {list(results)[0]}")
            else:
                answer.append(f"{a} {e} {b} {equal} ?")
    
    return answer

