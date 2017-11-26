# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    temp = []
    for i in range(1,len(A)):
        sum_head = sum(A[0:i])
        sum_tail = sum((A[i:len(A)]))
        temp.append(abs(sum_head- sum_tail))
    return min(temp)
    pass