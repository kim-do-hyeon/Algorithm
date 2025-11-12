# [골드 3] 백준 10096 - 세 친구

N = int(input())
U = input()

if len(U) % 2 == 0 :
    print("NOT POSSIBLE")
else :
    n = len(U) // 2

    def solve(a, b) :
        n = len(a)

        lcp = n
        for i in range(n) :
            if a[i] != b[i] :
                lcp = i
                break
        
        lcs = n
        for i in range(n) :
            if a[-1 - i] != b[-1 - i] :
                lcs = i
                break
                
        return lcp + lcs >= n
    # U[:n], U[n:]
    # U[n + 1:], U[:n + 1]

    answer = []
    if solve(U[:n], U[n:]) :
        answer.append(U[:n])
    if solve(U[n + 1:], U[:n + 1]) :
        answer.append(U[n + 1 :])
    
    answer = list(set(answer))

    if len(answer) == 0 :
        print("NOT POSSIBLE")
    elif len(answer) != 1 :
        print("NOT UNIQUE")
    else :
        print(answer[0])