# 최대 최소의 간격

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = - 1
    min_num = 100
    for i in range(N):
        if arr[i] >= max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]

    rev_arr = arr[::-1]     # max는 더 나중 인덱스를 반환해야해서.
    difference = (N - rev_arr.index(max_num)-1) - arr.index(min_num)
    
    print(f'#{tc} {abs(difference)}')