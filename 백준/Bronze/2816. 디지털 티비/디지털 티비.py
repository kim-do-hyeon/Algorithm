# 백준 2816 - 디지털 티비

N = int(input())
tv = []
for i in range(N) :
    name = input()
    if name == "KBS1" :
        index1 = i
    elif name == "KBS2" :
        index2 = i
    tv.append(name)

result = ""
result += "1" * index1
result += "4" * index1
if index1 > index2 :
    index2 += 1
result += "1" * index2
result += "4" * (index2 - 1)
print(result)