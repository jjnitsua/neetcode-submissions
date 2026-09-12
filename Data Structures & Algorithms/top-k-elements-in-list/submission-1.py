class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
                freq[n]=freq.get(n,0)+1
        
        groups={}
        for key,value in freq.items():
            if value not in groups:
                groups[value]=[]
            groups[value].append(key)
        
        sorted_items = sorted(groups.items(), key=lambda x: x[0], reverse=True)
        output=[]

        for freq, nums_with_freq in sorted_items:
            output.extend(nums_with_freq)

            if len(output) >= k:
                 return output[:k]


            