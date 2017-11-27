# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sum_of_A = sum(A)
    miss = total - sum_of_A
    return int(miss)

    pass

A = [2, 3, 1, 5]
print(solution(A))
