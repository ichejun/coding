'''
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        '''
        220ms
        19.7M
        '''
        # # a = [matrix.reshape([-1])]
        # a = []
        # # a = [a.append(x) for x in matrix ]
        # for x in matrix:
        #     for i in x:
        #         a.append(i)

        # a =(lambda x: x % 3 == 0, [2, 18, 9, 22, 17, 24, 8, 12, 27])
        # a =(lambda x: a.append([i for i in x]), [i for i in matrix]  ) #[[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        # a =(lambda x: a.append(x), [i for i in matrix]  ) #[[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        # a =(lambda x: a.append(x), [i for l in matrix for i in l]  ) #[[1, 5, 9], [10, 11, 13], [12, 13, 15]] tuple
        a =[i for l in matrix for i in l] #[[1, 5, 9], [10, 11, 13], [12, 13, 15]]


        print (a)
        a.sort()
        return a[k-1]

