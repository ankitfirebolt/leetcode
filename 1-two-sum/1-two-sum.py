class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i,n in enumerate(nums):
            if target-n in seen_dict:
                return [seen_dict[target-n], i]
            else:
                seen_dict[n] = i