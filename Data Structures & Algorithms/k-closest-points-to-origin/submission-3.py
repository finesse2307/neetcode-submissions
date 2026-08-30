class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)

        for x, y in points:
            dist = (x**2) + (y**2)
            heapq.heappush(minheap, (dist, x, y))
        
        closest = []
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            closest.append([x,y])
            k-=1
        return closest

