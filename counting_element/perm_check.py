# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    counter_check = [0] * len(A)

    for i in A:
        if not (1 <= i <= len(A)):
            return 0
        else:
            if (counter_check[i - 1]) != 0:
                return 0
            else:
                counter_check[i - 1] = 1
    return 1
    pass

A = [4,1,3,5]
print(solution(A))
