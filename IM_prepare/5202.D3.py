# [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    transit = [0]*25    # 0~24 시간 table
    count = 0

    for i in range(N):
        s = arr[i][0]
        e = arr[i][1]

        if 1 not in transit[s+1:e]:   # 아직 작업 신청이 없으면
            for j in range(s, e+1):
                transit[j] += 1     # 작업 신청
            count += 1

    print(f'#{tc} {count}')