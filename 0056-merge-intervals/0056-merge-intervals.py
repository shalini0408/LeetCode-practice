class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res =[]
        sorted_data = sorted(intervals, key=lambda x: (x[0],x[1]))
        for i in range(len(intervals)):
            start = sorted_data[i][0]
            end = sorted_data[i][1]
            if res!=[] and end <= res[-1][1]:
                continue
            for j in range(i+1,len(intervals)):
                if sorted_data[j][0] <= end:
                    end = max(end,sorted_data[j][1])
                else:
                    break
            res.append([start,end])
        return res
                 
        