# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = dummy.next

        # find the position
        for i in range(1,m):
            cur = cur.next
            pre=pre.next
        
        print(pre.val)

        # reverse
        for i in range(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next  = pre.next
            pre.next = temp

        return dummy.next
        """
        x=[]
        def calculate(head):
            while head!=None:
                x.append(head.val)
                head=head.next
        ptr=head
        calculate(ptr)
        l1=x[:left-1]
        l2=x[left-1:right]
        l2=l2[::-1]
        l3=x[right:]
        list1=l1+l2+l3
        new=ListNode(list1[0])
        head=new
        for i in list1[1:]:
            x=ListNode(i)
            new.next=x
            new=x
        return head
        """