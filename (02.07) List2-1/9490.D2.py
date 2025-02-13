# 풍선팡

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balls = [list(map(int,input().split())) for _ in range(N)]

    def pop_balls(balls):
        max_cnt = 0
        for i in range(N):
            for j in range(M):
                cnt = balls[i][j]

                for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:     # 좌표가 주어진 리스트에서 빠저나가지 않으면
                        cnt += balls[ni][nj]            # cnt를 업데이트

                max_cnt = max(max_cnt, cnt)             # 다음 좌표의 cnt와 비교해서 max 저장장
        return max_cnt

    result = pop_balls(balls)

    print(f'#{tc} {result}')