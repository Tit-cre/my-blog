# a,b地址输出
a=5
b=5
print(id(a))
print(id(b))
print(type(a))
print(type(b))

#
strl = 'abcd'
print(strl[1])

strl = [1,2,3]
strl[1] = 5
print(strl)

print("1\n2\n3")

# 修正
s = "    haPPy BirThDay to U"
# 去前后空格
s1 = s.strip()
# 全部切换小写
s2 = s1.lower()
# 将u改为you
s3 = s2.replace("u","you")
print(s3)

s = "    haPPy BirThDay to U"
print(s.strip().lower().replace("u","you"))
