'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] #存放高度堆栈
        n = len(height)
        out = 0
        for i in range(n):
            if len(stack) == 0 or height[i] < height[stack[-1]]: #如果新增的高度比栈顶的高度低 或者 栈为空 则将位置入栈
                stack.append(i)
            else: #如果高，则往回溯到栈内高度更高的点为止,并记录高度
                s = 0
                while(height[i] > height[stack[-1]]): #不断与之前的堆栈中记录的进行比较
                    last_top = stack[-1-s] #记录栈顶元素 即pop出去的序号
                    stack.pop()
                    if len(stack) == 0:
                        break
                    width = i - stack[-1] - 1
                    height_ = min(height[i], height[stack[-1]]) - height[last_top]
                    out += width * height_
                stack.append(i)
                
        return out







