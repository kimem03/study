def solution(num_list):
    answer = 0
    sum = 0
    mul = 1
    for i in num_list:
        sum += i
        mul *= i
    
    if mul < sum*sum:
        answer = 1
    else:
        answer = 0
    return answer