A = 'ABCD'
B = 'EFGHIJKLMN'

N = len(A)
M = len(B)
i = j = 0   # A[i], B[j]

# 문자열을 이용한 방법
# ans = ''

# while i + j < N + M:
#     if i < N:
#         ans += A[i]
#         i += 1
#     if j < M:
#         ans += B[j]
#         j += 1

# print(ans)

# 리스트를 이용한 방법법
ans = [0]*(N+M)
while i+j < N+M:
    if i < N:
        ans[i+j] = A[i]
        i += 1
    if j < M:
        ans[i+j] = B[j]
        j += 1

print(''.join(ans))