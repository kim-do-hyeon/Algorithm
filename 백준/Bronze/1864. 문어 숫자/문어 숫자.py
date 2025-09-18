# [브론즈 2] 백준 1864 - 문어 숫자

DATA = {
    "-" : 0,
    "\\" : 1 ,
    "(" : 2,
    "@" : 3,
    "?" : 4,
    ">" : 5,
    "&" : 6,
    "%" : 7,
    "/" : -1
}

while True :
    S = input()
    if S == "#" :
        break
    else :
        result = 0
        S = list(S)
        for index, value in enumerate(S) :
            result += DATA[value] * (8 ** (len(S) - index - 1))
    print(result)
