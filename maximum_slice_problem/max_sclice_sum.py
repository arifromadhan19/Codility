A = [3,2,-6,3,0]

max_slice_ending_here = A[0]
max_slice = A[0]


for element in A[1:]:
    max_slice_ending_here = max(element, max_slice_ending_here + element)
    print(max_slice_ending_here)
    max_slice = max(max_slice, max_slice_ending_here)


# print(max_slice)

