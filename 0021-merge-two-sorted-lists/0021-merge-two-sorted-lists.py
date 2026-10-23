# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        if list1==None:
            return list2
        if list2==None:
            return list1
        head=list1
        if list1.val >=list2.val:
            head=list2
            list2=list2.next
        else:
            list1=list1.next
        curr=head
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1==None:
            curr.next=list2
        else:
            curr.next=list1
        return head
                
                
                
                
                
        
        