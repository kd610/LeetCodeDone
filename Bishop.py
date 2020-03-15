import math
h, w = input().split()
h, w = int(h), int(w)
if h is 1 or w is 1:
    print(1)
else:
    print(math.floor((h*w+1)/2))
