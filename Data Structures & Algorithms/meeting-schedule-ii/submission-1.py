"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        l = 0
        r = 0
        rooms = 0
        max_rooms = 0

        while l < len(start):
            if start[l] < end[r]:
                l+=1
                rooms +=1
            else:
                r+=1
                rooms -=1
            max_rooms = max(max_rooms, rooms)
        return max_rooms
