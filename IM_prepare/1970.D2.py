# 쉬운 거스름돈

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\algorithm_hw\SWEA_seoul_4\IM_prepare\input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bills = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * len(bills)

    for bill in bills:
        change[bills.index(bill)] = N // bill
        N %= bill

    print(f'#{tc}\n{" ".join(map(str, change))}')