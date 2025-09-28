button, rest = map(int,input().split()) # button = 입력 시간 , rest = 같은 숫자 연속입력 시 기다리는 시간
result = 0
check = 0
text = list(input())
al_dic = {
          2 : ['A', 'B', 'C'],
          3 : ['D', 'E', 'F'],
          4 : ['G', 'H', 'I'],
          5 : ['J', 'K', 'L'],
          6 : ['M', 'N', 'O'],
          7 : ['P', 'Q', 'R', 'S'],
          8 : ['T', 'U', 'V'],
          9 : ['W', 'X', 'Y', 'Z']}
for alpha in text :
    count = [number for number, chars in al_dic.items() if alpha in chars] # 해당 문자가 있는 키 값 전달
    if not count : # 공백일 경우
        result += button
        check = 0
    else :
        # 문자가 위치한 인덱스를 찾아 +1을 하면 그것이 곧 연속적으로 입력해야하는 횟수가 된다
        t = [c for c in range(len(al_dic[count[0]])) if alpha == al_dic[count[0]][c]] # count키값에 맞는 value 리스트에서
                                                                                      # alpha가 위치한 인덱스값
        if check == count : # 이전 문자와 비교
            result += rest + button*(t[0]+1)
        else :
            result += button*(t[0]+1)
        check = count
print(result)