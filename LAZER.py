t = int(input())
while t > 0:
   n,q = map(int,input().split())
   arr = list(map(int,input().split()))
   d = dict()
   for i in range(1,n+1):
       d[i] = arr[i-1]
   for i in range(q):
       x1,x2,y = map(int,input().split())
       count = 0
       for j in range(1,n):
           if d[j+1] > d[j]:
               if (x1 < j+1 and x2 > j) and (y >= d[j] and y <= d[j+1]):
                   count += 1
           else:
               if (x1 < j+1 and x2 > j) and (y >= d[j+1] and y <= d[j]):
                   count += 1
       print(count)
               
       
   t -= 1
    