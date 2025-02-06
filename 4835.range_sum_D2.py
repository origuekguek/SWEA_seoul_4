T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # 받는 값이 단일이라 list() 필요 X
    numbers = list(map(int, input().split()))   # 다중이라 list 필요 O

    max_sum = -float('inf')
    min_sum = float('inf')

    for i in range(N-M+1):                      # 마지막쪽 범위 신경 써주어야함. N이 아니라 N-M+1 까지만
        current_sum = 0                         # current_sum은 사용할 범위 안에서 명시해주기.
        for j in range(M):
            current_sum += numbers[i+j]         # 그림그려보면서 어디까지 더해나가야하는지 정확히 계산.
        if max_sum < current_sum:
            max_sum = current_sum
        if min_sum > current_sum:
            min_sum = current_sum

    difference = max_sum - min_sum

    print(f"#{tc} {difference}")
