# Binary search Tree는 데이터를 빨리 찾기 위한 방법이다.
# 이진트리형태로 되어있으므로 logN의 시간복잡도를 가지고, 최악의 경우에 N의 시간복잡도(이진트리가 아니라 한쪽으로 쏠려있어서 배열과 별반 다른 게 없는 경우)를 갖게 된다.

class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def insert(node, val):

    # 만약에 root가 비어있을 때
    # node를 root로 만든다.

    if node is None:
        return Node(val)

    # 만약 root의 val가 새로운 val보다 클 경우
    if val<node.val:
        node.left=insert(node.left, val)

    # 만약 root의 val가 새로운 val보다 작을 경우
    else:
        node.right=insert(node.right, val)

    # root 리턴
    return node

def remove(root, val):
    if val<root.val:
        root.left=remove(root.left, val)
    elif val>root.val:
        root.right=remove(root.right, val)
    else:
        # 자식노드가 한 개이거나 두 개인 경우
        if root.left is None:
            temp_node=root.right
            return temp_node
        elif root.right is None:
            temp_node=root.left
            return temp_node
        # 자식노드가 두 개 일 때
        temp_node=minimum(root.right)
        root.val=temp_node.val
        root.right=remove(root.right, temp_node.val)

    return root

# inorder

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# 가장 작은 값 출력
def minimum(node):
    # 노드가 가장 왼쪽으로 갈 경우
    while (node.left is not None):
        node=node.left
    return node