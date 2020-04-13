t = int(input())
while t > 0:
    row,col = map(int,input().split())
    cunter = 0
    if row == 1 and col == 1:
        cunter = 20
    elif row == col:
        cunter = 21
    else:
        cunter = 22
    print(cunter)
    
    medr = (row + col)//2
    medc = (row + col)//2
    if (row != col):
        print(str(medr) + ' ' +str(medc))
    if ((row != col) or (row == col and row != 1)):
        print(str(1)+' '+str(1))
    print(str(2)+' '+str(2))
    print(str(1)+' '+str(3))
    print(str(6)+' '+str(8))
    print(str(2)+' '+str(4))
    print(str(1)+' '+str(5))
    print(str(4)+' '+str(8))
    print(str(2)+' '+str(6))
    print(str(1)+' '+str(7))
    print(str(2)+' '+str(8))
    print(str(8)+' '+str(2))
    print(str(7)+' '+str(1))
    print(str(6)+' '+str(2))
    print(str(8)+' '+str(4))
    print(str(5)+' '+str(1))
    print(str(4)+' '+str(2))
    print(str(8)+' '+str(6))
    print(str(3)+' '+str(1))
    print(str(2)+' '+str(2))
    print(str(8)+' '+str(8))
    print(str(1)+' '+str(1))
    t -= 1
        
        
        