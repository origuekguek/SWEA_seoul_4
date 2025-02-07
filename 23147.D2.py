T = int(input())

for tc in range(1, T + 1):
    width_of_room = int(input())
    box_height = list(map(int, input().split()))

    max_v = 0  # 최대 낙차 변수

    for i in range(width_of_room - 1):  # 마지막 상자는 비교할게 없어서서
        cnt = 0  # 현재 상자의 낙차

        for j in range(i + 1, width_of_room):  # 오른쪽 모든 상자와 비교
            if box_height[i] > box_height[j]:  # 현재 상자보다 낮다면 낙차 증가
                cnt += 1

        if max_v < cnt:  # 최대 낙차 업데이트
            max_v = cnt

    print(f"#{tc} {max_v}")
