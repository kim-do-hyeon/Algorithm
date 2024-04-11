def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2])

    intersection = 0
    union = 0

    for i in str1_list:
        if i in str2_list:
            intersection += 1
            union += 1
            str2_list.remove(i)
        else:
            union += 1

    union += len(str2_list)

    if union == 0:
        answer = 1
    else:
        answer = intersection / union
    answer = int(answer * 65536)

    return answer