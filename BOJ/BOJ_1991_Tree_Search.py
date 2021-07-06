import sys


def preorder(node):
    print(chr(node+65), end='')
    if l[node]:
        preorder(l[node])
    if r[node]:
        preorder(r[node])


def inorder(node):
    if l[node]:
        inorder(l[node])
    print(chr(node+65), end='')
    if r[node]:
        inorder(r[node])


def postorder(node):
    if l[node]:
        postorder(l[node])
    if r[node]:
        postorder(r[node])
    print(chr(node+65), end='')


N = int(input())
l = [0] * N
r = [0] * N
for _ in range(N):
    nodes = list(sys.stdin.readline().split())
    nodes[0] = ord(nodes[0]) - 65
    if nodes[1] != '.':
        nodes[1] = ord(nodes[1]) - 65
        l[nodes[0]] = nodes[1]
    if nodes[2] != '.':
        nodes[2] = ord(nodes[2]) - 65
        r[nodes[0]] = nodes[2]

preorder(0)
print()
inorder(0)
print()
postorder(0)