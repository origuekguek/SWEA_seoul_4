for i in range(1, 11):
    number_of_buildings = int(input())  # 건물 개수 입력
    building_heights = list(map(int, input().split()))  # 건물 높이 입력
    view_buildings = 0  # 조망권 확보된 세대 수

    for j in range(2, number_of_buildings - 2):  # 양 끝 2칸 제외
        # 현재 건물과 좌우 2칸씩 가져오기
        left_2 = building_heights[j - 2]
        left_1 = building_heights[j - 1]
        current = building_heights[j]
        right_1 = building_heights[j + 1]
        right_2 = building_heights[j + 2]

        # 현재 건물이 주변보다 높을 경우에만 조망권 확보 가능
        max_surrounding = max(left_2, left_1, right_1, right_2)

        if current > max_surrounding:
            view_buildings += current - max_surrounding  # 차이만큼 조망권 세대 수 추가

    print(f'#{i} {view_buildings}')  # 결과 출력