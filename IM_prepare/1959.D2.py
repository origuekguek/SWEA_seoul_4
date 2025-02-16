# 두 개의 숫자열

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\algorithm_hw\SWEA_seoul_4\IM_prepare\input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # len(B)가 더 작으면 작은애를 A로
    if len(B) < len(A):
        A, B = B, A
    
    max_s = 0
    for i in range(len(B)-len(A)+1):    # len(A)를 움직이면서 (len(B)-len(A)+1까지)
        s = 0
        for j in range(len(A)):
            s += A[j]*B[i+j]
        max_s = max(max_s, s)
    
    print(f'#{tc} {max_s}')