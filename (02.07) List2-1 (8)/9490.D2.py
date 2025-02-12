# 풍선팡

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balls = ["".join(input().split()) for _ in range(N)]
    print(balls)

    def pop_balls(balls):
        max_cnt = 0
        for i in range(N):
            for j in range(M):
                cnt = int(balls[i][j])
                if j > 0:
                    cnt += int(balls[i][j-1])
                if j < M-1:
                    cnt += int(balls[i][j+1])
                if i > 0:
                    cnt += int(balls[i-1][j])
                if i < N-1:
                    cnt += int(balls[i+1][j])
                max_cnt = max(max_cnt, cnt)
        return max_cnt

    result = pop_balls(balls)

    print(f'#{tc} {result}')