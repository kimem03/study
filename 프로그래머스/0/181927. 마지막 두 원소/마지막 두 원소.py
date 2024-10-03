def solution(num_list):
    answer = num_list
    
    l = len(num_list) - 1
    z = num_list[l]
    y = num_list[l-1]
    
    if(z > y):
        answer.append(z-y)
    else:
        answer.append(z*2)
        
    return answer