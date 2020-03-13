# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        s = t = ListNode()
        current_node = None
        
        while not (l1 is None or l2 is None):
            if l1.val < l2.val:
                #remember current low-node
                current_node = l1
                l1 = l1.next
            else:
                current_node = l2
                l2 = l2.next
            
            #only mutate after we have followed -> next
            t.next = current_node
            t = t.next
            
        t.next = l1 or l2
        
        return s.next
        
        
        """
        ##First one
        def insert(root, item): 
            temp = ListNode(item) 

            if (root == None): 
                root = temp 
            else : 
                ptr = root 
                while (ptr.next != None): 
                    ptr = ptr.next
                ptr.next = temp 

            return root 
  
        def arrayToList(arr, n): 
            root = None
            for i in range(0, n, 1): 
                root = insert(root, arr[i]) 

            return root 
        
        if l1 is None and l2 is None:
            print("l1 and l2 is none")
            return
        else:
            container = []
            while l1 is not None:
                container.append(l1.val)
                l1 = l1.next
                
            while l2 is not None:
                container.append(l2.val)
                l2 = l2.next

            container.sort()
            print(container)
            
            return arrayToList(container, len(container))
        """

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()