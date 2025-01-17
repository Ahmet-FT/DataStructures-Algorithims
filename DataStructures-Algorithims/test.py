class SinglyNode :
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

curr = Head



def display(head):
    curr = head
    elements = []


    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(elements))

display(Head)
#this is a comment