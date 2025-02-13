# [S/W 문제해결 기본] 3일차 - 회문2

import sys
sys.stdin = open("input.txt", "r")

# 가로 방향으로 회문들의 길이 출력
def row_pd(words):
    global max_length
    for word in words:
        for s in range(100):
            for e in range(100 - s):
                if word[s:s + e] == word[s:s + e][::-1]:  # 만약 회문이면
                    max_length = max(max_length, len(word[s:s + e]))
    return max_length

#세로 방향으로 회문들의 길이 출력
def col_pd(words):
    reverse_words = list(zip(*words))
    global max_length
    for word in reverse_words:
        for s in range(100):
            for e in range(100 - s):
                if word[s:s + e] == word[s:s + e][::-1]:  # 만약 회문이면
                    max_length = max(max_length, len(word[s:s + e]))
    return max_length

T = 10
for tc in range(1, T + 1):
    case_num = int(input())
    words = [input() for _ in range(100)]
    max_length = 1

    row_pd(words)
    col_pd(words)

    # 가장 긴 회문의 길이 출력
    print(f"#{case_num} {max_length}")