# 가장 빠른 문자열 타이핑

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    T, P = input().split()

    N = len(T)
    M = len(P)
    cnt = 0

    i = 0
    while i <= N - M:
        if T[i:i+M] == P:
            cnt += 1
            i += M
        else:
            i += 1

    result = N - (M-1) * cnt

    print(f'#{tc} {result}')