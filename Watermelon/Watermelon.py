w = int(input())
lis = [int(i) for i in range(w)]
y =0
for i in lis:
    for j in lis:
        if i + j == w:
            if i%2 ==0 and j%2==0:
                y = 1
            else:
                n = 0
if y == 1:
    print("YES")
else:
    print('NO')
                