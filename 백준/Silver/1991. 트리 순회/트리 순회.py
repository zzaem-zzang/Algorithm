class Node:
    def __init__(self, item):
        self.item= item
        self.left = None
        self.right = None
# 노드의 개수 N
# 항상 A가 루트 노드 자식 노드가 없는 경우 . 으로 표현
# 전위순회
def preorder(node):
    if node is None:
        return
    
    print(node.item, end='')
    preorder(node.left)
    preorder(node.right)
# 중위순회
def inorder(node):
    if node is None:
        return
    
    inorder(node.left)
    print(node.item, end='')
    inorder(node.right)
# 후위순회
def postorder(node):
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.item, end='')

N = int(input())
nodes = {}
for _ in range(N):
    root , l, r = input().split()
    if root not in nodes:
        nodes[root] = Node(root)
    if l !='.' and l not in nodes:
        nodes[l]= Node(l)
    if r !='.' and r not in nodes:
        nodes[r]= Node(r)
# 트리 생성
    # 자식 연결
    nodes[root].left = nodes[l] if l !='.' else None
    nodes[root].right = nodes[r] if r !='.' else None

preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])
print()


