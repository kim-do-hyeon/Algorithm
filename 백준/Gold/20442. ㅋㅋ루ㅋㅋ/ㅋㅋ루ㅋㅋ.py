# 백준 20442 - ㅋㅋ루ㅋㅋ
# 분류 : 문자열, 투 포인터

S = input()

num_k = 0
num_r = 0

for i in range(len(S)) :
    if S[i] == 'K' :
        num_k += 1
    if S[i] == 'R' :
        num_r += 1


start = -1
end = len(S)

max_length = 0

for i in range(num_k // 2 + 1) :
    if num_r == 0 :
        break

    # 앞, 뒤로 K가 i개씩 있는 경우
    max_length = max(max_length, 2 * i + num_r) 

    start += 1
    end -= 1
    while start < end and S[start] != 'K' :
        start += 1
        num_r -= 1
    while start < end and S[end] != 'K'  :
        end -= 1
        num_r -= 1
    
print(max_length)