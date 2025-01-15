def solution(arr, queries):
    for sublist in queries:
        for i, j in [sublist]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
    return arr