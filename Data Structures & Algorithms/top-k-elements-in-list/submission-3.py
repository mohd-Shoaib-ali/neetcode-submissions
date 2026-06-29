class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}
        new_list=[]
        for num in nums:
            if num in group:
                group[num]+=1
            else:
                group[num]=1
        new_dict=dict(sorted(group.items(),
                          key=lambda x :x[1] ,reverse=True))        
        for key,value in new_dict.items():
                new_list.append(key)     
        return new_list[:k]          

