for _ in range(int(input())):
    x = list(map(int, input().split(" ")))
    k = []
    ans = 0
    
    for _ in range(x[0]):
        k.append(list(map(int, input().split(" "))))
    
    sticker_list = list(map(int, input().split(" ")))
    
    for i in range(x[0]):
        m = 100
        for j in range(1, k[i][0]+1):
            m = min(m, sticker_list[k[i][j] -1])
        ans += m * k[i][-1]
        
    print(ans)