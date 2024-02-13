def solution(a, b):
    answer = 0
    A = str(a)
    B = str(b)
    if A+B > B+A:
        answer = int(A+B)
    else:
        answer = int(B+A)
    return answer