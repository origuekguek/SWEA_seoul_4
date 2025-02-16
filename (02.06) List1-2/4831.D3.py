# [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\algorithm_hw\SWEA_seoul_4\(02.06) List1-2\input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_idxes = list(map(int, input().split()))

    stops = [0] * (N + 1)
    for charge_idx in charge_idxes:
        stops[charge_idx] = 1

    cur_pos = 0 
    count = 0  

    while cur_pos + K < N:
        next_pos = cur_pos + K
        
        # 충전소 찾을 때까지 뒤로
        while cur_pos < next_pos and stops[next_pos] == 0:
            next_pos -= 1
        # 만약 충전소 못찾았으면 count = 0
        if cur_pos == next_pos:
            count = 0
            break

        cur_pos = next_pos
        count += 1

    print(f'#{tc} {count}')