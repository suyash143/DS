class BST:
    def __init__(self, data):
        self.key = data
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:return
        if data<self.key:
            if self.lchild :
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    
    def search(self,data):
        if self.key ==data:
            print("Node Found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node Not Found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("nNOde not found")

    def preorder(self):
        print(self.key,end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()


    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key,end=' ')

    def delete(self,data):
        if self.key is None:
            print("BTree is Empty")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print('Node not found')
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print('Node not found')
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self




root=BST(10)
list1=[1,32,4,6,7,8,8,650]
for i in list1:
    root.insert(i)

print('preorder')
root.preorder()
root.delete(10)
print()
root.preorder()
