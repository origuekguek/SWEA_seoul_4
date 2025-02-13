# 연속한 1의 개수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    max_len = 0
    j = 0
    for i in range(N-1):
        cnt = 1
        if arr[i] == 1:
            for j in range(1, N-i):
                if arr[i+j] == 1:
                    cnt += 1
                else:
                    break
        max_len = max(max_len, cnt)
    print(f'#{tc} {max_len}')