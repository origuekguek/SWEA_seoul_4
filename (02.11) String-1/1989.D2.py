# 초심자의 회문 검사
 
def pd_test(T):
    if T == T[::-1]:
        return 1
    else:
        return 0
 
T = int(input())
for tc in range(1, T+1):
    T = input()
 
    result = pd_test(T)
    print(f'#{tc} {result}')