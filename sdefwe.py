x,y=input().split()
y=int(y)
for i in range(y):
    b=(''.join(reversed(x)))
    print(b[i],end="")
