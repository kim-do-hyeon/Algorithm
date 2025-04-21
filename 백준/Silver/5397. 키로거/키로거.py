# 백준 5397 - 키로거
# 분류 : 자료구조

T = int(input())
for i in range(T) :
    S = input()
    
    stack1 = []
    stack2 = []
    for s in S :
        if s == "-" :
            if len(stack1) > 0 :
                stack1.pop(-1)
        elif s == "<" :
            if len(stack1) > 0 :
                stack2.append(stack1.pop(-1))
        elif s == ">" :
            if len(stack2) > 0 :
                stack1.append(stack2.pop(-1))
        else :
            stack1.append(s)
    print("".join(stack1) + "".join(stack2[::-1]))