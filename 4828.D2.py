T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))   # 주어진 숫자들 꼭 공백 기준 split 하기

    max_num = numbers[0]                        # 첫 원소를 최댓값으로 가정
    min_num = numbers[0]                        # 첫 원소를 최솟값으로 가정

    for i in range(len(numbers)):
        if max_num < numbers[i]:                # 현재 설정된 max_num보다 numbers[i]가 크면 최댓값 변경
            max_num = numbers[i]
        if min_num > numbers[i]:                # 현재 설정된 min_num보다 numbers[i]가 작으면 최솟값 변경
            min_num = numbers[i]

    difference = max_num - min_num

    print(f'#{tc} {difference}')