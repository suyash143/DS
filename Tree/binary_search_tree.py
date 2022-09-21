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
                


root=BST(10)
list1=[1,32,4,6,7,8,8,650]
for i in list1:
    root.insert(i)
    
root.search(18)