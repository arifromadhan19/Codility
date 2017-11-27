def solution(A):
    temp = []
    for i in range(len(A)):
        for j in range(len(A)):
            if i < j < len(A):
                d = set(A[i:j + 1])
                unique = len(d)
                if unique <= 2:
                    temp.append(set(A[i:j + 1]))
    return  len(set(map(frozenset, temp)))

A = [5,4,4,5,0,12]
print(solution(A))




