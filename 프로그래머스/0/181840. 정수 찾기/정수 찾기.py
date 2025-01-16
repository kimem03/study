def solution(num_list, n):    
    answer = 0
    for i in range(0, len(num_list)):
        if (num_list[i] == n):
            answer = 1
            break
        else:
            answer = 0
            continue
    return answer