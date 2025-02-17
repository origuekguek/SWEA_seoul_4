# 풍선팡

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    # 배열을 순회하며 좌표를 하나 잡는다.
    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            # arr[i][j] 의 값 안에서
            for k in range(1, arr[i][j]+1):
                # 4개의 방향을 돌아가며 합을 늘린다.
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di*k, j + dj*k
                    if 0 <= ni < N and 0 <= nj < M:
                        sum += arr[ni][nj]

            max_sum = max(max_sum, sum)

    print(f'#{tc} {max_sum}')