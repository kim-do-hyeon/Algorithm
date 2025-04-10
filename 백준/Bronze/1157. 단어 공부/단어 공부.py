temp = input().upper()

uni_temp = list(set(temp))

cnt_list = []
for i in uni_temp :
    cnt = temp.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
else :
    max_index = cnt_list.index(max(cnt_list))
    print(uni_temp[max_index])