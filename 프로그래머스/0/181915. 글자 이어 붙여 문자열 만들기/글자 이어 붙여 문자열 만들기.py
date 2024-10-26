def solution(my_string, index_list):
    answer = ''
    l = len(index_list)
    for i in range(0, l):
        j = index_list[i]
        answer += my_string[j]
    return answer