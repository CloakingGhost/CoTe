from collections import defaultdict

a, b, c = int(input()), int(input()), int(input())
num_dict = defaultdict(int)
for num in str(a * b * c):
    num_dict[num] += 1

for i in '0123456789':
    print(num_dict.get(i) if num_dict.get(i) else 0)
