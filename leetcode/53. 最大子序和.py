'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        j->
        * - - - i
        * * - - |
        * * * - 
        * * * *
        '''

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]


        '''
        暴力解法O^3 时间爆炸了
        '''
        # dp = [[0] for _ in range(n)]
        # maxsum = nums[0]
        # for i in range(n):
        #     dp[i][0] = nums[i]
        #     maxsum = max(maxsum, dp[i][0]) 
        #     for j in range(1, i + 1): # j < i   sum from j to i
        #         dp[i][j] = nums[j] + dp[i][j - 1]
        #         maxsum = max(maxsum, dp[i][j]) 
        # return maxsum

        '''
        动态规划 s[i] = s[i] if s[i - 1] < 0;
                       s[i] + s[i - 1] if s[i - 1] > 0
        '''
        s = nums[:]
        for i in range(1,n):
            if s[i-1] <= 0:
                s[i] = s[i]
            else:
                s[i] = s[i] + s[i-1]
        return max(s)
            











