class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def get_count(head):
            count = 0
            while head is not None:
                count = count + 1
                head = head.next
                
            return count
        
        if head is not None:
            n_from_start =  get_count(head)-n
            counter = 0
            temp = head
            
            if n_from_start is 0:
                head = temp.next
                temp = None
                
                return head
            
            for i in range(n_from_start-1):
                temp = temp.next
                if temp is None:
                    break
                
            next = temp.next.next
            temp.next = None
            temp.next = next
                    
        return head