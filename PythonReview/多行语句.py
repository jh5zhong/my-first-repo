"""
Python语句中一般以新行作为语句的结束符。
也可以使用斜杠（/）将一行的语句分为多行显示。
"""
item_one = "钟军华"
item_two = "是"
item_three = "编程高手"
total = item_one + \
        item_two + \
        item_three
print(total)

#如果语句中包含[],{}或()括号就不需要使用多行连接符。
days1 = ['Monday','Tuesday','Wednesday','Thursday','Friday']
days2 = ['Monday','Tuesday',
         'Wednesday','Thursday','Friday']
days3 = ['Monday','Tuesday',
'Wednesday','Thursday','Friday']
days4 = ['Monday','Tuesday'
         ,'Wednesday','Thursday','Friday']

print(id(days1))
print(id(days2))
print(days1[2])
print(days2[2])
print(days3[2])
print(days4[2])