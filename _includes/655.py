def height(r, n=0):
    if r:
        return max(height(r.left,n+1), height(r.right,n+1))
    return n

def draw(buf, r, top, left, right):
    if r is None:
        return
    mid = (left+right)//2
    buf[top][mid] = str(r.val)
    draw(buf, r.left, top+1, left, mid-1)
    draw(buf, r.right, top+1, mid+1, right)

class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = height(root)
        buffer = []
        for i in range(h):
            buffer.append([''] * (2 ** h - 1))
        draw(buffer, root, 0, 0, 2**h-2)
        return buffer
