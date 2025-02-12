def bruteforce(p, t):
    N = len(t)
    M = len(p)

    # 텍스트에서 비교할 위치 i / 텍스트 길이 N
    # 패턴에서 비교할 위치 j / 패턴 길이 M

    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:    # 다르면
            i = i -j + 1    # i - j 비교를 시작했던 위치
            j = 0           # j는 다시 0으로 되돌리면 되죠.
        else:               # 같으면
            i += 1
            j += 1

    if j == M:              # while문을 벗어난 이유가 j와 M이 같아서라면
        return i -j         # 패턴의 시작 인덱스 반환
    else:
        return -1

t = 'TTTTTATTAATA'
p = 'TTA'

print(bruteforce(p, t))