R, C, ZR, ZC = map(int, input().split())
res = []
for _ in range(R):
    li = input()
    result = ""
    for i in li:
        result += i * ZC
    for i in range(ZR):
        res.append(result)
for i in res:
    print(i)