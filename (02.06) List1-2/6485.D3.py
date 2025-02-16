# 삼성시의 버스 노선

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\algorithm_hw\SWEA_seoul_4\(02.06) List1-2\input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line_len = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    bus_stops = [0] * 5001

    for line in line_len:
        for i in range(line[0], line[1]+1):
            bus_stops[i] += 1
    
    arr = ''
    for stop in C:
        arr += str(bus_stops[stop])
    
    result = " ".join(arr)
    
    print(f'#{tc} {result}')