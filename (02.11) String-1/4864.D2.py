# [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
 
def in_str(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0
 
T = int(input())
for tc in range(1, T + 1):
    str1 = str(input()) # ABC
    str2 = str(input()) # ZZZZZABCZZZZZ
 
    result = in_str(str1, str2)
 
    print(f'#{tc} {result}')