'''
315. 计算右侧小于当前元素的个数

给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:


        # '''
        # 暴力解法，由于数据没有限定范围，所以时间会爆掉 时间复杂度O(n2),超时
        # '''
        # n = len(nums) #nums数组长度
        # ans = [0] * n
        # for i in range(n):
        #     j = i
        #     for j in range(n-i):
        #         if nums[i+j] < nums[i]:
        #             ans[i] += 1
        # return ans


        '''
        二分查找  时间复杂度O(nlog2n)
        https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/er-fen-cha-zhao-wei-hu-you-xu-shu-zu-python3-by-dz/
        '''
        ans = []
        sorted_nums = []
        for i in range(len(nums)-1, -1, -1):#降序轮询
            idx = bisect.bisect_left(sorted_nums, nums[i]) #取nums[i]以二分查找法的方式寻找其在 排序序列中的 序列号
            ans.append(idx) #将序列号放入输出数组中
            sorted_nums.insert(idx, nums[i]) #将数据插入排序数列中
        return reversed(ans) #将结果倒叙输出