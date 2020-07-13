'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        暴力
        '''
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []


        '''
        哈希
        '''
        # dic = {}#利用字典完善哈希列表功能
        # for k,v in enumerate(nums):
        #     if target-v in dic:#写之前判断，避免了重复元素的覆盖
        #         return [dic[target-v], k]
        #     dic[v] = k

        '''
        哈希-2
        ''' 
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]





