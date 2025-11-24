n = int(input())

cnt = 0
n1, n2 = 0, 1
while cnt <= n:
  n3 = n1 + n2
  n1, n2, n3 = n2, n3, n1
  cnt += 1
print(n3)