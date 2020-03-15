elements = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
K = int(input())
th = K-1
print(elements[th])


"""
K = 27
K -= 1
for i, val in enumerate(elements):
    if i is K:
        print(val)
        break
"""

"""
if K < 16:
    th = K-1
    print(elements[th])
else:
    th = -(32-K)-1
    print(elements[th])
    """



