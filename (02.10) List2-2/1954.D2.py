# 달팽이 숫자

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    k = 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        while k < N:
            ni, nj = i + di*k, j + dj*k
            k += 1
    print(f'#{tc} {arr}')