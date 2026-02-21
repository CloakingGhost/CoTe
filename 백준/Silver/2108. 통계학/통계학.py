# https://www.acmicpc.net/problem/2108

"""
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
"""

import sys
from collections import Counter

input = sys.stdin.readline


class Solution:
    def __init__(self, N=0, nums=[]):
        self.N = N
        self.nums = nums
        self.sorted_nums = sorted(nums)

    def get_sum(self):
        return round(sum(self.nums) / self.N)

    def get_medium(self):
        return self.sorted_nums[N // 2]

    def get_max_frequency(self):
        counter = Counter(self.nums)
        num, max_count = counter.most_common(1)[0]

        max_nums = list(filter(lambda x: x[1] == max_count, counter.items()))
        if len(max_nums) > 1:
            return sorted(max_nums)[1][0]

        return num

    def get_range(self):
        return abs(self.sorted_nums[-1] - self.sorted_nums[0])


N = int(input())

nums = [int(input()) for _ in range(N)]

solution = Solution(N, nums)
print(solution.get_sum())
print(solution.get_medium())
print(solution.get_max_frequency())
print(solution.get_range())
