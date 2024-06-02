class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degree = [0] * n
        # Calculate in-degree for each node
        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                in_degree[rightChild[i]] += 1

        # Find the root (node with in-degree 0)
        root_count = 0
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                root_count += 1
                root = i
        
        # There should be exactly one root
        if root_count != 1:
            return False
        
        # DFS to check for cycles and connectivity
        visited = [False] * n

        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            if leftChild[node] != -1:
                if not dfs(leftChild[node]):
                    return False
            if rightChild[node] != -1:
                if not dfs(rightChild[node]):
                    return False
            return True

        if not dfs(root):
            return False

        # Check if all nodes are visited
        for i in range(n):
            if not visited[i]:
                return False

        return True