# [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    print(f'#{tc}\n')
    print(f'N = {N}')
    print(f'M = {M}')
    print(f'weight = {weight}')
    print(f'capacity = {capacity}\n')