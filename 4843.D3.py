#[파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = [0] * N

    # 선택정렬
    def selection_sort(arr, N):
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    selection_sort(arr, N)
   
    for small_idx, small_num in enumerate(arr[:N//2]):  # 제일 작은~중간전까지 값 1 3 5 7 9 번 index에 저장
        result[2 * small_idx + 1] = small_num

    for big_idx in range(N//2):                         # N=10 이면 5까지 0 1 2 3 4 까지의 인덱스까지
        big_num = arr[N - 1 - big_idx]                  # arr의 끝값부터 순회
        result[2 * big_idx] = big_num                   # 그 값을 result에 짝수번에 저장장

    print(f'#{tc} {" ".join(map(str, result[:10]))}')