num = 456789

c = [0]*12  # c[10], c[11]은 항상 0. 여분 만들어논 것

for _ in range(6):  # 단순 반복 6회
    c[num%10] += 1  # num의 1의 자리 알아내기
    num //= 10

print(c)    # [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]

i = 0
tri = run = 0
while i <10:    # 카드 번호가 9 까지라서
    if c[i] >=3:    # tri 확인
        c[i] -=3
        tri += 1
        continue

    if c[i] >=1 and c[i+1] >= 1 and c[i+2] >=1: # run 확인 여기서 i+2 때문에 앞에서 12개 만든 것!!!!
        c[i] -= 1
        c[i+1] -= 1 
        c[i+2] -= 1
        run += 1
        continue 
    i += 1  # 없으면 1 증가

if run+tri == 2:
    print('win')
else:
    print('lose')