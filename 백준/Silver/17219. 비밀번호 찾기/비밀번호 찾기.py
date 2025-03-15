# 백준 17219 - 비밀번호 찾기
# 분류 : 구현

N, M = map(int, input().split())
password_lists = {}
for i in range(N) :
    site, password = input().split()
    password_lists[site] = password

for i in range(M) :
    find_site = input()
    print(password_lists[find_site])