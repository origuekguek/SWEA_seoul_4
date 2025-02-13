# 간단한 소인수분해

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    exp_lst = [0] * 5   # a, b, c, d, e 개수 리스트 만들기
    factor_lst = [2, 3, 5, 7, 11]   # 소인수 리스트 만들기

    # factor_lst를 순회하며 나눗셈
    for i in range(5):
        while N % factor_lst[i] == 0:
            N //= factor_lst[i]
            exp_lst[i] += 1
            
    print(f'#{tc} {" ".join(map(str, exp_lst))}')