def solution(x1, x2, x3, x4):
    answer = True
    a = True
    b = True
    
    if x1 == True:
        if x2 == True:
            a = True
        else:
            a = True
    else:
        if x2 == True:
            a = True
        else:
            a = False
            
    if x3 == True:
        if x4 == True:
            b = True
        else:
            b = True
    else:
        if x4 == True:
            b = True
        else:
            b = False
            
    if a == True:
        if b == True:
            answer = True
        else:
            answer = False
    else:
        answer = False
        
    return answer