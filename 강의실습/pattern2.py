# 이중 for문 연습해보자.

t = 'TTTTTATTAATA'
p = 'TTA'           #TTA 이렇게 세번 비교

def search(p,t):
    N = len(t)
    M = len(p) 

    for i in range(N-M+1):      # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):      # p에서 t와 비교할 위치 인덱스
            if t[i+j] != p[j]:  # i부터 i+0 i+1 i+2 이것과 패턴의 j번째를 비교
                break
        else:                   # for-else구문. break에 걸리지 않고 for가 끝난 경우에 실행
            return i            # 패턴이 처음 나타난 인덱스 리턴
    return -1                   # t에 p 패턴이 없는 경우우

print(search(p,t))