# [S/W 문제해결 기본] 3일차 - 회문1

T = 10
for tc in range(1, T+1):
    word_len = int(input())
    words = [input() for _ in range(8)]
    cnt = 0

    for word in words:
        for s in range(8-word_len+1):
            if word[s:s + word_len] == word[s:s + word_len][::-1]:  # 만약 회문이면
                cnt += 1

    reverse_words = list(zip(*words))
    reverse_lst = ["".join(tup) for tup in reverse_words]

    for word in reverse_lst:
        for s in range(8-word_len+1):
            if word[s:s + word_len] == word[s:s + word_len][::-1]:  # 만약 회문이면
                cnt += 1

    print(f'#{tc} {cnt}')