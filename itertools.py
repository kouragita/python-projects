from itertools import count

for i in count(3):
    print(i)

    if i >= 20:
        break

from itertools import accumulate

num = list(accumulate(range(8)))
print(num)

from itertools import accumulate, takewhile

num = list(accumulate(range(8)))
print(num)
print(list(takewhile( lambda x: x <= 6, num)))
9