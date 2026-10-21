class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for n in nums:
            count[n] = count.get(n,0) +1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(nums),0,-1):
            for a in freq[i]:
                res.append(a)
                if len(res)== k :
                    return res