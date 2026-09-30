class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = {}
        for num in nums: 
            if num in f_dict:
                f_dict[num] += 1
            else: 
                f_dict[num] = 1

        sorted_nums = sorted(f_dict, key=f_dict.get, reverse=True)
        #sorted_nums = sorted(f_dict, key=lambda num: f_dict[num], reverse=True)
        print (sorted_nums)
        return sorted_nums[0:k]
    
