# 숫자 배열 회전

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    original_arr = [list(map(int, input().split())) for _ in range(N)]
    matrix = []

    # (N * N)을 90도 회전하는 함수
    def rotate_90_clockwise_matrix(matrix):
        return list(map(list, zip(*matrix[::-1]))) # Why? 90도 회전 =>  1. 전치(zip) (j,i) 2. 행 뒤집기(::-1) (n-1-j, i)

    rotated_90 = rotate_90_clockwise_matrix(original_arr)
    rotated_180 = rotate_90_clockwise_matrix(rotated_90)
    rotated_270 = rotate_90_clockwise_matrix(rotated_180)

    print(f'#{tc}')
    for i in range(N):
        print("".join(map(str, rotated_90[i])), end= " ")
        print("".join(map(str, rotated_180[i])), end= " ")
        print("".join(map(str, rotated_270[i])), end= " ")
        print()