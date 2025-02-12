# 3
# 1 2 3
# 4 5 6
# 7 8 9 

N = int(input())    # 배열 행과 열의 크기
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0]*N for i in range(N)]
# [[0]*4]*3 이런거 쓰지말자. arr2[2][1] = 1 로 바꾸어도 나머지도 바뀌어버림.
# 모든 행 [0, 1, 0, 0]. 참조 3번 반복 (참조할 대상이 1개라서)

print(arr)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr2) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(N):
    for j in range(N):      # 행 우선순회 방법
        print(arr[i][j])    # 1 -> 2 -> 3 -> 4 순서로 출력