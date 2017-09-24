class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        root = {}
        tree = {}
        for (p, c) in edges:
            if c not in root:
                root[c] = root.setdefault(p, p)
                tree.setdefault(root[p], {p}).add(c)
                continue
            if c in tree:
                if p in tree:
                    if c != p:
                        for node in tree[c]:
                            root[node] = p
                            tree[p].add(node)
                        del tree[c]
                        continue
                    return (p, c)
                if p in root:
                    if root[p] == c:
                        return (p, c)
                    tree.setdefault(root[p], {root[p]})
                    for node in tree[c]:
                        root[node] = root[p]
                        tree[root[p]].add(node)
                    del tree[c]
                    continue
                tree.setdefault(p, {p})
                for node in tree[c]:
                    root[node] = p
                    tree[p] = {p}
                    tree[p].add(node)
                del tree[c]
                continue
            return (p, c)
