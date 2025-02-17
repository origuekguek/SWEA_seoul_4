# [S/W 문제해결 기본] 2일차 - Ladder1

import sys
sys.stdin = open("input.txt", "r")

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    endpoint_i = 99
    endpoint_j = 0

    # arr[i][j]에서 arr[i][j] == 2 이면 그게 end_point
    for j in range(100):
        if arr[endpoint_i][j] == 2:
            endpoint_j = j

    while endpoint_i > 0:
        if 0 < endpoint_j and arr[endpoint_i][endpoint_j - 1] == 1:
            while 0 < endpoint_j and arr[endpoint_i][endpoint_j - 1] > 0:
                endpoint_j -= 1
        elif endpoint_j < 99 and arr[endpoint_i][endpoint_j + 1] == 1:
            while endpoint_j < 99 and arr[endpoint_i][endpoint_j + 1] > 0 :
                endpoint_j += 1

        endpoint_i -= 1

    print(f'#{tc} {endpoint_j}')