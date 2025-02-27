# 백준 1316 - 그룹 단어 체커
# 분류 : 문자열
N = int(input())
arr = [input() for _ in range(N)]

count = 0
for word in arr :
    check = [False] * 26
    prev = ''
    for w in word :
        if prev != w :
            if check[ord(w) - 97] :
                break
            check[ord(w) - 97] = True
        prev = w
    else :
        count += 1

print(count)