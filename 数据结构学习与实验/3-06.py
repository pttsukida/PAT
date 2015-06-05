import sys

class node():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data,left):
        if left=True:
            self.left=node(data)
        else:
            self.right=node(data)
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print self.data,
op=['+','-','*','/']
root=node('+')
#def insert(node,data,left):
