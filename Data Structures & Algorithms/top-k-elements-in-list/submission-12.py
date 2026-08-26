class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        heap = []
        heapq.heapify(heap)
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(k):
            item = heapq.heappop(heap)[1]
            res.append(item)
        return res