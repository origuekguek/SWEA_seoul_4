# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N = 5 K = 3

    total = 0

    for _ in range(N):  # 0 1 2 3 4
        arr = list(map(int, input().split()))    # [0, 0, 1, 1, 1]
        i = 0
        while i < len(arr) - K + 1:           # 0 1 2 3 4
            cnt = 0
            if arr[i] == 1:
                for j in range(K):                  # 0 1 2
                    if arr[i] == arr[i+j]:
                        cnt += 1

                if cnt == K:
                    total += 1
                    i += K

            else:
                i += 1

    print(f'#{tc} {total}')