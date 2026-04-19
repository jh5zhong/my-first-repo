# total = 10
# for letter in 'python':
#     if letter == 'h':
#         break
#     print(letter)
#     total -= 1
# print(total)





n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n += 1
print('END')
