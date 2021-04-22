# Given a binary tree and a key, insert the
# key into the binary tree at the first position available in level order.
class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Do level order traversal until we find
# an empty place
def insert(root, key):

    if not root:
        root = TreeNode(key)
        return 

    q = []
    q.append(root)

    while len(q):
        root = q[0]
        q.pop(0)

        if not root.left:
            root.left = TreeNode(key)
            break
        else:
            q.append(root.left)
        if not root.right:
            root.right = TreeNode(key)
            break
        else:
            q.append(root.right)

# Driver Code
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)

    print("Inorder traversal before insertion: ")
    inorder(root)
    key = 12
    insert(root, key)
    print("**********")
    print("Inorder traversal after insertion: ")
    inorder(root)