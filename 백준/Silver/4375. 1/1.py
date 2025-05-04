# 백준 4375 - 1
# 분류 : 코딩 테스트 준비 - 기초 ) 수학

while True :
    try :
        N = int(input())
    except :
        break
    num = 1
    count = 1
    while True :
        if num % N != 0 :
            num = num * 10 + 1
            count += 1
        else :
            break
    
    print(count)