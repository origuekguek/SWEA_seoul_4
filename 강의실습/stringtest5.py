s1 = 'abc'
s2 = 'abc'
s3 = 'def'

print(s1==s2)   # True
print(s1 is s2) # True

s1 = 'abc'
s2 = 'ab'
s3 = 'def'
s4 = s2 + 'c'

print(s1==s4)           # True  => 내용이 같니?
print(s1 is s4)         # False => 같은 메모리니?
print(s1 is 'abc')      # True
print(s4 is 'ab'+'c')   #False => 연산되니까 다른 메모리

s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
s4 = 'AC'
s5 = 'abc'
s6 = ' ab'

print(s1 == s2)             # True
print(s1 < s2)              # False
print(s1 < s3)              # True
print(s3 < s4)              # False
print(ord('a'), ord('A'))   # 97 65  => 비교 가능
print(s1 < s5)              # True
print(s4 < s6)              # False


