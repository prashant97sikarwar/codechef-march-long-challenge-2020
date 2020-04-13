t,s = map(int,input().split())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    arr.sort()
    brr.sort()
    if s == 1:
        slope = 0
        for i in range(n):
            if arr[i] >= brr[i]:
                slope = 1
                print('NO')
                break
        if slope == 0:
            d = set()
            a = 0
            b = 0
            m = 0
            for i in range(n):
                if (i < n-1 and arr[i] == arr[i+1]):
                    a += 1
                if (i < n-1 and brr[i] == brr[i+1]):
                    b += 1
                if arr[i] in d:
                    m += 1
                else:
                    d.add(arr[i])
                if brr[i] in d:
                    m += 1
                else:
                    d.add(brr[i])
            count = m - b
            if count < n-1:
                print('NO')
            else:
                print('YES')
    
    t -= 1