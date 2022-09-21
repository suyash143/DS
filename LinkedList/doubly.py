class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None


class LinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            self.head.pref = new_node
            new_node.nref=self.head
            self.head = new_node

    def show(self):
        if self.head is None:
            print("empty List")
        else:
            n=self.head
            while n is not None:
                print(n.data,f"({n.nref})","-->",end=' ')
                n=n.nref

    def show_reverse(self):
        if self.head is None:
            print("empty List")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,f"({n.nref})", '-->', end=' ')
                n=n.pref

    def delete_start(self):
        if self.head is None:
            print('LL empty')
            return
        if self.head.nref is None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_end(self):
        if self.head is None:
            print('LL empty')
        else:
            n=self.head
            if n.nref is not None:
                while n.nref.nref is not None:
                    n=n.nref

                n.nref=None
            else:
                self.head=None


LL=LinkedList()
LL.add_begin(20)


LL.delete_start()
LL.show()