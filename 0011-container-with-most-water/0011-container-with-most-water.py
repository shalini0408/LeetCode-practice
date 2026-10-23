class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area= 0
        i=0
        j=len(height)-1
        while i<j:
            length = min(height[i],height[j])
            breadth = j-i
            area = length * breadth
            max_area = max(area,max_area)
            if (height[i] < height[j]):
                i+=1
            else:
                j-=1
        return max_area

            

                
        