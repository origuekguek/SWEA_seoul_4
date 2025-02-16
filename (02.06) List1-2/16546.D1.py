# Baby-gin_실습

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\algorithm_hw\SWEA_seoul_4\(02.06) List1-2\input.txt", "r")

def is_baby_gin(numbers):
        counts = [0]*10
        for num in numbers:
            counts[int(num)] += 1

        i = 0
        while i < 10:
            # tri 인지 확인
            if counts[i] >= 3:
                counts[i] -= 3
                continue
            if i <= 7 and counts[i] > 0 :
                counts[i] -= 1
                counts[i+1] -= 1   
                counts[i+2] -= 1
                continue
            i += 1
        
        if sum(counts) == 0:
            return 'true'
        else:
            return 'false'
        
T = int(input())
for tc in range(1, T+1):
    numbers = input()
    print(f'#{tc} {is_baby_gin(numbers)}')