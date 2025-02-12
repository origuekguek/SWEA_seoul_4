di = [0, 1, 0, -1]    # 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]

N = 2
M = 3

for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + di[dir]
            if 0<=ni<N and 0<=nj<M: # 행과 열의 범위가 다를 때 주의
                print(ni, nj)   