f = [1,1]
for i in range(2,100):
    n = f[i-1] + f[i-2]
    f.append(n)
print(f)