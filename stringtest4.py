s = 'string'
s = s[::-1]

print(s, type(s)) # gnirts <class 'str'>

s_lst = list(s)
s_lst.reverse()

print(s_lst) 
print(''.join(s_lst))

s = "".join(s)
print(s)