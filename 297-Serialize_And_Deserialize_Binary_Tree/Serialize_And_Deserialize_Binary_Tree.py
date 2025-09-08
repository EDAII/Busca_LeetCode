class Codec:
    def serialize(self, root):
        if not root: return ""
        q = [root]
        res = []
        while q:
            node = q.pop(0)
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        while res[-1] == "null":
            res.pop()
        return ",".join(res)

    def deserialize(self, data):
        if not data: return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = [root]
        i = 1
        while q:
            node = q.pop(0)
            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root