# https://www.acmicpc.net/problem/1991
# 트리 순회

import sys

input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]


preorder_result = []
inorder_result = []
postorder_result = []


def preorder(node, result_arr):
    if node == ".":
        return
    result_arr.append(node)
    preorder(tree[node][0], result_arr)
    preorder(tree[node][1], result_arr)


def inorder(node, result_arr):
    if node == ".":
        return
    inorder(tree[node][0], result_arr)
    result_arr.append(node)
    inorder(tree[node][1], result_arr)


def postorder(node, result_arr):
    if node == ".":
        return
    postorder(tree[node][0], result_arr)
    postorder(tree[node][1], result_arr)
    result_arr.append(node)


preorder("A", preorder_result)
inorder("A", inorder_result)
postorder("A", postorder_result)


print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))
