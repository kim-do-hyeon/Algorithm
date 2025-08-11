# 백준 1357 - 뒤집힌 덧셈

X, Y = input().split()
X = list(X)
Y = list(Y)
X.reverse()
Y.reverse()
X = int("".join(X))
Y = int("".join(Y))
result = list(str(X + Y))
result.reverse()
while result[0] == "0" :
    if result[0] == "0" :
        del result[0]
print("".join(result))