# 백준 5355 - 화성 수학
# 문제집 : Python 배우기

T = int(input())
for i in range(T) :
    answer = 0.00
    formula = input().split()
    num = float(formula[0])
    formula = formula[1:]
    for j in formula :
        if j == "@" :
            num *= 3
        elif j == "%" :
            num += 5
        elif j == "#" :
            num -= 7
    print("{:.2f}".format(num))