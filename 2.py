# 使用print直接输出类型信息
print(type(666))
print(type(13.14))
print(type("黑马程序员"))



# 使用变量储存type（）语句的结果
int_type = type(666)
float_type = type(13.14)
string_type = type("黑马程序员")
print(int_type)
print(float_type)
print(string_type)

# 使用type（）语句，查看变量储存的数据类型信息
name = 666
name_type = type(name)
print(name_type)