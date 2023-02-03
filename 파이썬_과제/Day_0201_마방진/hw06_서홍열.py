def _():

    while True:
        try :
            n=int(input('홀수차 배열의 크기를 입력하세요 : '))
        except :
            continue
        
        if n%2==0:
            print('다시 입력하세요.')
        else:
            break

    count = 1

    #행 #열
    y = 0
    x = n//2

    squre = [[0]*n for i in range(n)]

    while True:

        if count > n ** 2:
            break
        
        if squre[y][x] == 0 :
            #값넣기
            squre[y][x] = count
            count += 1
            y -= 1
            x += 1 

        else : 
            # print(y, x)
            y+=2
            x-=1

        if y == -1:
            y = n - 1
        elif y >= n:
            #패턴
            y %= n


        if x >= n:
            x = 0
        elif x == -1:
            x = n-1
        
    for x in squre:
        print(*x,end="")
        print()

_()