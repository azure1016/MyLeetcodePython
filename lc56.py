# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = intervals[:]
        #Always think about the weird input
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = self.sort_by_start)
        res = []
        i = 0
        for i in range(0, len(intervals)): #and intervals[i].start <= intervals[len(intervals) - 1].end:
            #you shall process the last element at first, especially when you have i+1 logic
            if i == len(intervals) - 1:
                res.append(intervals[i])
                break
                #if we always care about i+1 rather than modify i, then our lives easier. Like a grinding wheel!
                #we know we'd never look back. If not for sorting, the time complexity will be O(n)
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i + 1].start = intervals[i].start
                if intervals[i].end > intervals[i + 1].end:
                    intervals[i + 1].end = intervals[i].end
            else:
                res.append(intervals[i])
        return res
    # if i.end < j.start, then must i.end < ()j+1).start



    def sort_by_start(self, l):
        return l.start

    def pr(self, li):
        for x in li:
            print("[" + str(x.start) +  ',' + str(x.end) + "],")
if __name__ == '__main__':
    test = Solution()
    case = [[5,5],[1,1],[5,7],[5,7],[1,1],[3,4],[4,4],[0,1],[5,5],[1,2],[5,5],[0,2]]
    #case = [[1,4],[4,5]]
    #case = [[1,3], [2,6], [8, 10], [15, 18]]
    intervals = []
    for i in case:
        intervals.append(Interval(i[0], i[1]))

    test.pr(test.merge(intervals))