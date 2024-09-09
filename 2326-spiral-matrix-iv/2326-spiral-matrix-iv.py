# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix=[[-1 for _ in range(n)]for i in range(m)]
        
        topRow=0
        leftCol=0
        bottomRow=m
        rightCol=n
        
        while (leftCol<rightCol and topRow<bottomRow):
            
            for col in range(leftCol,rightCol):
                if head:
                    matrix[topRow][col]=head.val
                    head=head.next
                else:
                    return matrix
            
            topRow+=1
            
            for row in range(topRow,bottomRow):
                if head:
                    matrix[row][rightCol-1]=head.val
                    head=head.next
                else:
                    return matrix
                
            rightCol-=1
            
            for col in range(rightCol-1,leftCol-1,-1):
                if head:
                    matrix[bottomRow-1][col]=head.val
                    head=head.next
                else:
                    return matrix

            bottomRow-=1
                
            for row in range(bottomRow-1,topRow-1,-1):
                if head:
                    matrix[row][leftCol]=head.val
                    head=head.next
                else:
                    return matrix
            leftCol+=1
        
        return matrix
                
            