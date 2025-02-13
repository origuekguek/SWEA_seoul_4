# [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stops = list(map(int, input().split()))
    fuel = 0
    cnt = 0

    # 연료가 표시된 버스 정류장 생성
    bus_stops = [0]*(N+fuel+K+1)
    for _ in range(M):
        bus_stops[charge_stops[_]] = K
        # bus_stops[0] = K

    print(f'K = {K} N = {N} M = {M} ')
    print(bus_stops)

    i = 0
    while i <= N-K-fuel:
        if i > N - fuel - K:
            break
        else:
            print(f'처음 인덱스 = {i}')
            for j in range(fuel+K+1):         # 연료 범위 안에서 이동
                if bus_stops[i+K-j] == K:  # K만큼 이동해서 거꾸로 순회하며 충전소 보이면 충전
                    cnt += 1             # 충전 횟수 +1
                    fuel = j  # 연료 사용 후 충전
                    i += fuel + K - j  # 충전한 정류장 인덱스로 이동

                else:
                    i -= fuel + K - j - 1   # 한 칸 줄이고 다시 탐색

        print(f'연료량 = {fuel}')
        print(f'이동할 거리 = {fuel + K - j}')
        print(f'변경 인덱스 = {i}')

    print(f'#{tc} {cnt}')