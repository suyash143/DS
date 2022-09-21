class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class LinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node = Node(data)

        new_node.ref=self.head
        self.head=new_node


    def show(self):
        if self.head is None:
            print("empty List")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

LL=LinkedList()
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)

LL.show()