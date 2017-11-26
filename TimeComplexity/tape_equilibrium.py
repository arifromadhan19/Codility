# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#FISRT WAY BUT SCORE = 50
def solution1(A):
    # write your code in Python 3.6
    temp = []
    for i in range(1,len(A)):
        sum_head = sum(A[0:i])
        sum_tail = sum((A[i:len(A)]))
        temp.append(abs(sum_head- sum_tail))
    return min(temp)
    pass

#SECOND WAY, SCORE = 100
def solution2(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)

    for index in range(1, len(A) - 1):
        head += A[index]
        tail -= A[index]
        if abs(head - tail) < min_dif:
            min_dif = abs(head - tail)

    return min_dif
    pass


A = [3, 1, 2, 4, 3]
print(solution1(A))
print(solution2(A))


