# Baby-gin_실습

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    c = list(map(int, input()))

    sort_c = [0] * 11
    for i in range(6):
        sort_c[c[i]] += 1
    print(sort_c)

    # i = 0
    # tri = run = 0
    # while i < 10:
    #     pass
