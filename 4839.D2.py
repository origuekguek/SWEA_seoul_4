# [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

T = int(input())
for tc in range(1,T+1):
    P, Pa, Pb = list(map(int, input().split()))
    # 이진탐색
    def binary_search(total_page, target_page):
        start, end = 1, total_page
        count = 0
        while start <= end :
            count +=1
            mid = (start + end) // 2
            if mid < target_page:
                start = mid + 1
            elif mid > target_page:
                end = mid -1
            else: return count
        return count

    # 탐색에서 반환한 count를 각각 저장장
    a_count = binary_search(P, Pa)
    b_count = binary_search(P, Pb)

    # 탐색 횟수 비교
    if a_count < b_count:
        print(f'#{tc} A')
    elif a_count > b_count:
        print(f'#{tc} B')
    else: print(f'#{tc} 0')