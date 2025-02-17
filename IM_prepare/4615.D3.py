# 재미있는 오셀로 게임

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]   # [i, j, 흑/백]

    board = [[0]*N for _ in range(N)]
    b_count = 0
    w_count = 0
    # 돌을 놓기
    for i in range(M):
        put_j = arr[i][0] - 1
        put_i = arr[i][1] - 1
        put_color = arr[i][2]

        board[put_i][put_j] = put_color
        other_color = 3 - put_color

        # 가로 검사
        if (put_color and other_color in board[put_i]) and (board[put_i].index(put_color) < board[put_i].index(other_color) and board[put_i][::-1].index(put_color) < board[put_i][::-1].index(other_color)):
            for k in range(board[put_i].index(put_color), N - board[put_i][::-1].index(put_color)):
                board[put_i][k] == put_color
        # 세로 검사
        elif (put_color and other_color in board[i][put_j]) and (board[put_i].index(put_color) < board[put_i].index(other_color) and board[put_i][::-1].index(put_color) < board[put_i][::-1].index(other_color)):
            for k in range(board[put_i].index(put_color), N - board[put_i][::-1].index(put_color)):
                board[put_i][k] == put_color
        # if 1 in range arr.index(2)  ~  N - arr[::-1].index(2) + 1 이면
        # arr.index(2)  ~  N - arr[::-1].index(2) + 1 까지 전부 = 2

    print(f'#{tc} arr = {arr}\nboard = {board}')