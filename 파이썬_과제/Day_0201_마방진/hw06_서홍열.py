def _():

    count = 1
    n = 3

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
            print('test1')
            print(f'{count} 번째 {squre}')

        else : 
            print(y, x)
            y+=2
            x-=1
            print(y, x)
            print("끝")

        if y == -1:
            y = n - 1
        elif y >= n:
            #질문
            print(f'질문{y,x}')
            y %= n
            print(f'질문끝{y,x}')

        if x >= n:
            x = 0
        elif x == -1:
            x = n-1
        
    for x in squre:
        print(*x,end="")
        print()

_()