'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

 

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
 

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


'''
暴力求解，耗时不通过
'''
# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
#         A_len = len(A)
#         B_len = len(B)
#         max_len = 0
#         for i in range(A_len):
#             for j in range(B_len):
#                 tmp_i = i
#                 tmp_j = j
#                 tmp_len = 0
#                 while(B[tmp_j] == A[tmp_i]):
#                     tmp_len += 1
#                     tmp_j += 1
#                     tmp_i += 1
#                     if tmp_i >= A_len or tmp_j >= B_len:
#                         break
#                 if max_len < tmp_len:
#                     max_len = tmp_len
#         return max_len
        





class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n-i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m-i)
            ret = max(ret, maxLength(0, i, length))
        return ret
