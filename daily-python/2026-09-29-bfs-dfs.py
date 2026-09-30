# 29 Eylül 2026 - BFS ve DFS
# Coding Interview University yol haritası

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def bfs(root):
    """Breadth-First Search - Genişlik öncelikli arama"""
    queue = deque([root])
    
    while queue:
        node = queue.popleft()  # Queue'dan çıkar (FIFO)
        print(node.value, end=" ")
        
        for child in node.children:
            queue.append(child)  # Queue'ya ekle


def dfs(root):
    """Depth-First Search - Derinlik öncelikli arama"""
    stack = [root]
    
    while stack:
        node = stack.pop()  # Stack'ten çıkar (LIFO)
        print(node.value, end=" ")
        
        for child in reversed(node.children):
            stack.append(child)  # Stack'e ekle


# Ağaç oluşturma
#     1
#    / \
#   2   3
#  / \
# 4   5

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]


if __name__ == "__main__":
    print("BFS (Genişlik öncelikli):")
    bfs(root)
    print()  # Yeni satır
    
    print("DFS (Derinlik öncelikli):")
    dfs(root)
    print()  # Yeni satır
