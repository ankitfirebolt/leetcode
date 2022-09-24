class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        sorted_intervals = sorted(intervals, key = lambda k : k[0])
        
        new_list = []
        
        for k in sorted_intervals:
            new_list += k
            
        return new_list == sorted(new_list)