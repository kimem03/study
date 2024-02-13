def solution(a, b):
    answer = 0
    A = str(a)
    B = str(b)
    if int(A+B) > 2*a*b:
        answer = int(A+B)
    else:
        answer = 2*a*b
    return answer