# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return "X"
        return str(root.val) + "(" + self.serialize(root.left) + "),(" + self.serialize(root.right) + ")"

    def deserialize(self, data):
        if data == "X":
            return None
        data = data.split("(", 1)
        n = TreeNode(int(data[0]))
        data = "(" + data[1]
    
        i = 0
        count = 0
        
        for i in range(len(data)):
            c = data[i]
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count == 0:
                    n.left = self.deserialize(data[1:i])
                    n.right = self.deserialize(data[i+3:-1])
                    return n
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))