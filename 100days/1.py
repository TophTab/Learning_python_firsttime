for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')#end表示结尾不换行
    print()

for x in range(1,10):
    for y in range(1,x+1):
        z=x*y
        print(str(x)+'*'+str(y)+'='+str(z)+' \t')
    print()