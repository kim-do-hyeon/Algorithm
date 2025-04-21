# 백준 2914 - 저작권
# 분류 : 수학

music, avg = map(int, input().split())
melody = music * avg
answer = 0
for i in range(melody, 1, -1) :
    temp = i / music
    if temp <= 1.0 :
        answer += 1

print(melody - answer)