class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # check if new is before current
            # e.g. new END is LESS than current START 
            # NEW comes BEFORE current
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new START BIGGER than current END
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res



#others
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_I = newInterval
        I = intervals
        res = []
        
        for i in range(len(I)):
            if new_I[1] < I[i][0]:
                res.append(new_I)
                return res + I[i:]
            elif new_I[0] > I[i][1]:
                res.append(I[i])
            else:
                 new_I = [min(new_I[0],I[i][0]),max(new_I[1],I[i][1])]
        res.append(new_I)
        return res 