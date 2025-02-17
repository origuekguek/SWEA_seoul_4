# [S/W 문제해결 기본] 2일차 - Sum

import sys
sys.stdin = open("input.txt", "r")

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합 중 최대
    max_row_sum = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        max_row_sum = max(max_row_sum, sum)

    # 각 열의 합 중 최대
    max_col_sum = 0
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
        max_col_sum = max(max_col_sum, sum)

    # 하향 대각선 합 중 최대
    max_dec_dia_sum = 0
    for i in range(100):
        sum = 0
        sum += arr[i][i]
        max_dec_dia_sum = max(max_dec_dia_sum, sum)

    # 상향 대각선 합 중 최대
    max_inc_dia_sum = 0
    for i in range(100):
        sum = 0
        sum += arr[i][99 - i]
        max_inc_dia_sum = max(max_inc_dia_sum, sum)

    result = max(max_row_sum, max_col_sum, max_dec_dia_sum, max_inc_dia_sum)

    print(f'#{tc} {result}')