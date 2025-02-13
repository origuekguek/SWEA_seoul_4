# 삼성시의 버스 노선

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N = 2
    line_len = [list(map(int, input().split())) for _ in range(N)]  # [[1, 3], [2, 5]]
    P = int(input())    # P = 5
    stops = [int(input()) for _ in range(P)]  # [1, 2, 3, 4, 5]
    line_stop = [0 for _ in range(5001)]
    for stop in stops:
        line_stop[stop-1] = stop-1

    arr = []
    for i in range(N):  # 0 1
        stop_arr = [0] * 5001  # [0, 0, 0, 0, 0]
        # stop_arr 에서 범위 안에 있는 수를 모두 1로 바꾸기
        start = line_len[i][0] - 1
        end = line_len[i][1] - 1
        for k in range(start, end+1):
            if (line_stop[k] - 1) < 0:  # 가능한 노선수에서 1을 뺐을 때 더이상 가능하지 않으면, 하나씩 밀기
                start += 1
                end += 1
            else:
                for j in range(start, end+1):
                    stop_arr[j] = 1

            line_stop[k] -= 1   # 가능한 노선 수를 하나씩 줄이기
        arr.append([stop_arr[stop] for stop in stops])    # [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1]]
        # arr[i].pop(0)

    line_num = list(zip(*arr))  # [(1, 0), (1, 1), (1, 1), (0, 1), (0, 1)]
    line_sum = list(sum(tup) for tup in line_num)  # [1, 2, 2, 1, 1]
    result = " ".join(map(str, line_sum))  # 1 2 2 1 1
    print(f'#{tc} {result}')

