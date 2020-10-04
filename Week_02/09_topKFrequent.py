class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 小根堆法：
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            if len(heap) == k:
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else:
                hq.heappush(heap, (freq, num))
        while heap:
            res.append(hq.heappop(heap)[1])
        return res
