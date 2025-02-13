# [S/W 문제해결 기본] 3일차 - String

import sys
sys.stdin = open("input.txt", "r", encoding="utf-8")

# pattern이 나타나는 횟수를 반환하는 함수
def search_pattern(pattern, txt):
    N = len(txt)
    M = len(pattern)
    cnt = 0

    for i in range(N - M + 1):
            if txt[i:i+M] == pattern:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    txt = input()

    result = search_pattern(pattern, txt)

    print(f'#{tc} {result}')