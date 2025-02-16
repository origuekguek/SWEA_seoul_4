# 오목 판정

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    flag = 'No'
    i = 0

    while i < N-4:
        for j in range(N-4):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 'o':
                flag = 'Yes'
            if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j] == 'o':
                flag = 'Yes'
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 'o':
                flag = 'Yes'
	        
        i += 1
        
    print(f'#{tc} {flag}')