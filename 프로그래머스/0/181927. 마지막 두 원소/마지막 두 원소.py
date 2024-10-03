def solution(num_list):
    
    l = len(num_list) - 1
    z = num_list[l]
    y = num_list[l-1]
    
    if(z > y):
        num_list.append(z-y)
    else:
        num_list.append(z*2)
        
    return num_list