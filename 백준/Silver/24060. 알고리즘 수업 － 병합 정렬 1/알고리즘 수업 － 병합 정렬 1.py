import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
result = -1


def merge_sort(A, l, r):
    if l < r:
        m = l + ((r - l) // 2)
        merge_sort(A, l, m)
        merge_sort(A, m + 1, r)
        merge(A, l, m, r, K)


# 오른쪽 배열 시작 인덱스 = 왼쪽 배열의 마지막 인덱스 + 1
def merge(
    A, l, m, r, target
):  # 원본, 시작 인덱스, 왼쪽 배열의 마지막 인덱스, 끝 인덱스
    global count
    global result
    ll, mm = l, m + 1  # 왼쪽 배열 시작 인덱스, 오른쪽 배열 시작 인덱스
    tmp = []

    while ll <= m and mm <= r:  # 왼쪽, 오른쪽 중 out of range 직전까지

        if A[ll] <= A[mm]:
            tmp.append(A[ll])
            ll += 1
        else:
            tmp.append(A[mm])
            mm += 1

    while ll <= m:  # 왼쪽 나머지
        tmp.append(A[ll])
        ll += 1

    while mm <= r:  # 오른쪽 나머지
        tmp.append(A[mm])
        mm += 1

    for t in range(l, r + 1):  # 정렬된 부분을 원본배열에 복사
        A[t] = tmp[t - l]
        count += 1
        if target == count:
            result = A[t]



merge_sort(A, 0, len(A) - 1)
print(result)
