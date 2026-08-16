class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        minheap = []
        for num in count.keys():
            heapq.heappush(minheap, (count[num], num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res

  