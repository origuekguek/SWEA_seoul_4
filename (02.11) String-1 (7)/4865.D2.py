# [파이썬 S/W 문제해결 기본] 3일차 - 글자수

T = int(input())
for tc in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    count_lst = [0]*len(str1)   # [0, 0, 0, 0]

    for str2_char in str2:      # H O F S T J P V P P 이렇게 순회하면서
        if str2_char in str1:  # S T J J 로 이루어진 str1의 리스트 안에 그 문자가 존재하면
            count_lst[str1.index(str2_char)] += 1   # 그 문자의 인덱스번호를 str1에서 찾아 count_lst의 카운트를 올림
            # 중복된 문자는 비워놓게 된다!
    maximum = max(count_lst)

    print(f'#{tc} {maximum}')