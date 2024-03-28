n, x = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

for m in range(0,n):
    if(a[m] < x):
        print(a[m], end=" ")