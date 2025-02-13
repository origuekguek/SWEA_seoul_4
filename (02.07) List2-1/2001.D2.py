# 파리 퇴치

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    
    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_fly = 0

            for x in range(M):
                for y in range(M):
                        temp_fly += flies[i+x][j+y]

            max_fly = max(max_fly, temp_fly)

    print(f'#{tc} {max_fly}')