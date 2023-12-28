import sys
input = sys.stdin.readline

nums = list(range(1, 10001))
list_ = []

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if i < 10001:
        list_.append(i)
for list_ in set(list_):
    nums.remove(list_)
for i in nums:
    print(i)