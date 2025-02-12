s1 = list(input())
s2 = input()

print(s1) # ['a', 'b', 'c']
print(s2) # 'abc'

print(s1[1]) # b
print(s2[1]) # b

s1[1] = 'e'
s2[1] = 'e'
print(s1) # ['a', 'e', 'c']
print(s2) # TypeError. 
s2 = 'aec'
print(s2) # 'aec'