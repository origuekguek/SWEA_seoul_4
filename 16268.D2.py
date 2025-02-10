# 풍선팡 2

import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(arr)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            temp_sum = arr[i][j]
            for k in range(4):
                if arr[i+dx[k]][j+dy[k]] in list:
                    temp_sum += arr[i+dx[k]][j+dy[k]]
            if temp_sum >= max_sum:
                max_sum = temp_sum

    print(f'#{tc} {max_sum}')