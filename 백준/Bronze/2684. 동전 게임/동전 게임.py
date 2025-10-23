def check_coin_case(case):
    check_list = [
        "TTT", "TTH", "THT", "THH", 
        "HTT", "HTH", "HHT", "HHH",
    ]
    
    check_result = []
    
    for check in check_list:
        check_count = 0
        for idx in range(len(case) - len(check) + 1):
            curr_coin = case[idx:idx+len(check)]
            
            if curr_coin == check:
                check_count += 1
                
        check_result.append(check_count)
        
    return check_result


def coin_game(case_list):
    answer = []
    
    for case in case_list:
        check_result = check_coin_case(case=case)
        check_result = " ".join(list(map(str, check_result)))
        answer.append(check_result)
        
    return answer


if __name__ == "__main__":
    N = int(input())
    case_list = []
    
    for _ in range(N):
        case = input()
        case_list.append(case)
        
    answer = coin_game(case_list=case_list)
    
    for ans in answer:
        print(ans)