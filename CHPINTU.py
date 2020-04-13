t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    d = {}
    for i in range(n):
        if arr[i] in d.keys():
            d[arr[i]] += brr[i]
        else:
            d[arr[i]] = brr[i]
    l = []
    for x in d:
        l.append(d[x])
    print(min(l))
    t -= 1