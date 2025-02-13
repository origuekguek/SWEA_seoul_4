# [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    num_lst = [0] * 10

    for i in range(N):
        num_lst[num[i]] += 1

    max_idx = max(num_lst)  # 2
    max_value = num_lst.index(max_idx)
    
    # 최대값이 여러개일 경우 가장 마지막 인덱스 반환
    if num_lst.count(max(num_lst)) > 1:
        max_value = (9 - num_lst[::-1].index(max_idx))

    print(f'#{tc} {max_value} {max_idx}')