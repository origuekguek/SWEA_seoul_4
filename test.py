# https://www.acmicpc.net/problem/12927

arr = list(input())
N = len(arr)
Y_count = arr.count("Y")
N_count = arr.count("N")
count = 0

to_N_num_lst = [0]*N
to_Y_num_lst = [0]*N

def switch_max(arr):
    for i in range(1,N+1):  # 1 2 3 4 5 6 7 8 9 10 11 12 ... N 까지 순회회
        # 배수들 다 Y-> N로 바꿨을때 원래보다 N_count > Y_count 이면 그렇게 한다.
        max_to_N_count = 1
        max_to_Y_count = 1
        for j in range(1,N//i):   # N 범위 안에서 i의 j배 배수들 순회
            if arr[i*j] == "Y":
                max_to_N_count += 1     # N으로 바꿀 Y 개수 최댓값 세기
            # elif arr[i*j] == "N": 
            #     max_to_Y_count += 1     # Y으로 바꿀 N 개수 최댓값 세기
        to_N_num_lst[i-1] = max_to_N_count
        to_Y_num_lst[i-1] = max_to_Y_count
    
    max_to_N_idx = to_N_num_lst.index(max(to_N_num_lst))
    max_to_Y_idx = to_Y_num_lst.index(max(to_Y_num_lst))

    # if max(to_N_num_lst) >= (N - max(to_Y_num_lst)):
    #     max_idx = max_to_N_idx
    # if max(to_N_num_lst) < (N - max(to_Y_num_lst)):
    #     max_idx = max_to_Y_idx
    max_idx = max_to_N_idx
    return max_idx

def switch_chage(arr, max_idx):
    for j in range(1,N//(max_idx+1)+1):     # max로 스위치 바꾸는 애의 배수들의 스위치를 전환
        if arr[(max_idx+1)*j-1] == "Y":
            arr[(max_idx+1)*j-1] = "N"
        elif arr[(max_idx+1)*j-1] == "N":
            arr[(max_idx+1)*j-1] = "Y"
    return arr

switch_max(arr)
print(to_N_num_lst)
switch_chage(arr, switch_max(arr))
print(arr)

to_N_num_lst = [0]*N
to_Y_num_lst = [0]*N

switch_max(arr)
print(to_N_num_lst) 
switch_chage(arr, switch_max(arr))
print(arr)

print(count)

