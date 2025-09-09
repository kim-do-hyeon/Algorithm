# 백준 1373 - 2진수 8진수

N = input()
print(oct(int("0b" + N, 2))[2:])