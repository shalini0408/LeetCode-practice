class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        lengthA = 0
        lengthB = 0
        tempA = headA
        tempB = headB

        while tempA:
            lengthA += 1
            tempA = tempA.next

        while tempB:
            lengthB += 1
            tempB = tempB.next


        tempa = headA
        tempb = headB
        diff = abs(lengthA - lengthB)

        if lengthA > lengthB:
            for _ in range(diff):
                tempa = tempa.next
        else:
            for _ in range(diff):
                tempb = tempb.next

       
        while tempa and tempb:
            if tempa == tempb:
                return tempa     
            tempa = tempa.next
            tempb = tempb.next

        return None
