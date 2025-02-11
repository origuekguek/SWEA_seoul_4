# 의석이의 세로로 말해요

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):

    given_words = [input() for _ in range(5)]   # ['AABCDD', 'afzz', '09121', 'a8EWg6', 'P5h3kx']
    max_len_idx = 0

    for i in range(len(given_words)-1):
        if len(given_words[i]) < len(given_words[i+1]):
            max_len_idx = i+1

    padded_words = [word+"%"*(len(given_words[max_len_idx])-len(word)) if len(word)<len(given_words[max_len_idx]) else word for word in given_words]

    reverse_given_words = list(zip(*padded_words))   # 90도 시계방향 회전
    join_words = "".join("".join(tup) for tup in reverse_given_words)   # 회전된 튜플들을 공백없이 합친것들을 공백없이 합침
    spt_words = join_words.split()

    print(f'#{tc} {"".join(spt_words).replace("%","")}')
