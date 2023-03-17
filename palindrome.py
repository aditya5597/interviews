# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        count=0
        currnode = head
        while currnode is not None:
            if currnode.val>=9 and currnode.val<=0:
                return False
            a.append(currnode.val)
            currnode = currnode.next
            count+=1
            
        if 1 <= count <= 10**6:
            for i in range(count//2):
                if a[i] != a[count-i-1]:
                    return False
            return True
        else:
            return False

b = [8,0,7,1,7,7,9,7,5,2,9,1,7,3,7,0,6,5,1,7,7,9,3,8,1,5,7,7,8,4,0,9,3,7,3,4,5,7,4,8,8,5,8,9,8,5,8,8,4,7,5,4,3,7,3,9,0,4,8,7,7,5,1,8,3,9,7,7,1,5,6,0,7,3,7,1,9,2,5,7,9,7,7,1,7,0,8]
head = ListNode(b[0],None)
prevnode = head
for i in b[1:]:
    currnode = ListNode(i,None)
    prevnode.next = currnode
    prevnode = currnode
    
obj = Solution()
result = obj.isPalindrome(head)
print(result)