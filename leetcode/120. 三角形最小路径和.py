'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是三角形的行数。

空间复杂度：O(n^2)O(n 
2
 )。我们需要一个 n*nn∗n 的二维数组存放所有的状态。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        #准备dp二维矩阵
        n = len(triangle)
        f = [[0] * n for _ in range(n)]

        #初始条件
        f[0][0] = triangle[0][0]

        #递推关系--ij的转移方程
        for i in range(1, n):
            f[i][0] = f[i-1][0] + triangle[i][0] #最左侧数值
            for j in range(1, i): #1 ~ i-1
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]
            f[i][i] = f[i-1][i-1] + triangle[i][i]#最右侧数值

        return min(f[n-1])



'''
思考倒叙的写法
'''
