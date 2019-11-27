# Binary tree paths # 257

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        
def dfs(root,path,paths):

    #paths=[]

    if root:
        path+=str(root.value)

        if not root.left and not root.right:
            paths.append(path)

        else:
            path+='->'
            dfs(root.left,path,paths)
            dfs(root.right, path,paths)


def get_paths(root):
    paths=[]
    dfs(root,'',paths)
    return paths


a=Node(1)
a.right=Node(3)
a.left=Node(2)
a.left.right=Node(5)


def dfsuma(root,cumsuma,sumas):

    if root:
        cumsuma+=root.value

        if not root.left and not root.right:
            sumas.append(cumsuma)

        else:
            dfsuma(root.left,cumsuma,sumas)
            dfsuma(root.right,cumsuma,sumas)

def get_sumas(root):
    sumas=[]
    dfsuma(root,0,sumas)
    return sumas



