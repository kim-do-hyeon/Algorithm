# 백준 17255 - N으로 만들기
# 분류 : 브루트포스

N = input()

def f(n) :
    if n == N :
        return 1
    
    if N.find(n) == -1 :
        return 0
    
    ret = 0
    for i in range(10) :
        left = str(i) + n
        right = n + str(i)

        if left == right :
            ret += f(left)
        else :
            ret += f(left)
            ret += f(right)

    return ret

answer = 0
for i in range(10) :
    answer += f(str(i))

print(answer)