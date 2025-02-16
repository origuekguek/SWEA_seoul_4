# 점점 커지는 당근의 개수

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\algorithm_hw\SWEA_seoul_4\IM_prepare\input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))    # [1, 2, 1, 2, 3, 1, 2, 1]

    # arr[i] + diff = arr[i+1]일 때마다 count += 1
    # arr[i] + diff != arr[i+1]이면 다시 count = 1로 초기화 하고 arr[i+1] 조사
    # 더 큰 count가 max_count

    if N == 1:
        max_count = 1
        continue
    
    max_count = 1
    count = 1
    diff = arr[1] - arr[0]  # 첫 두 원소의 차이를 diff로 초기화

    for i in range(1, N):
        cur_diff = arr[i] - arr[i - 1]  # 현재 증가량 계산

        if cur_diff > 0: 
            if cur_diff == diff:
                count += 1
            else:
                count = 2 
        else:
            count = 1  # 연속 증가가 아니면 초기화

        diff = cur_diff  # 현재 증가량 갱신
        max_count = max(max_count, count)  # 최댓값 갱신

    print(f'#{tc} {max_count}')