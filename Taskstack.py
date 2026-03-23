from Node import Node
class TaskStack:
    def __init__(self):
        self.head = None 

    def push_task(self,task):
        new_node=Node(task)
        new_node.next=self.head
        self.head=new_node

    def pop_task(self):
        self.head=self.head.next


    def display_task(self):
        current = self.head
        while current is not None:
            print(current.data)
            current=current.next 
      




