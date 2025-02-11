# [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

T = int(input())
for tc in range(1, T + 1):
    given_str = str(input()) 

    given_lst = list(given_str)
    given_lst.reverse()         # 준 문자열을 좌우대칭 뒤집기
    mapping_dct = {'b':'d', 'd':'b', 'p':'q','q':'p'}

    change_lst = [mapping_dct[x] if x in mapping_dct else x for x in given_lst] # 그 리스트의 x값들을 위에서 매핑하기
    chage_str = "".join(change_lst)


    print(f'#{tc} {chage_str}') 
