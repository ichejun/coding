'''
32. 最长有效括号

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        tmplen = 0

        '''
        bad case 没有考虑到的情况 "()(()" 左边非法括弧出现时(第3个)，在现有的逻辑中无法处理 堆栈中需要记录最近一次没有匹配成功的左括弧的index。然后用i跟其之间的距离来做。
        '''
        # stack = [] #使用list来实现堆栈
        # for i in s:
        #     if i == '(':
        #         stack.append('(')
        #     elif len(stack) > 0:
        #         stack.pop()
        #         tmplen += 1
        #     else:
        #         tmplen = 0
        #     maxlen = max(maxlen, tmplen)
        # return maxlen * 2


        # stack = [0] #使用list来实现堆栈
        stack = [-1] #使用list来实现堆栈  stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i,ch in enumerate(s):
            if ch == '(':           #如果是左括弧
                stack.append(i)     #记录最近的左括弧的index
            elif len(stack) > 1:    #如果是右括弧且堆栈中有未匹配的左括弧
                stack.pop()         #将左括弧的位置出栈
                maxlen = max(maxlen, i - stack[-1])
                # tmplen += 1
            # else:                   #如果是右括弧且堆栈中无未匹配的左括弧  不做处理？
                # tmplen = 0
            else:                   #如果是右括弧且堆栈中无未匹配的左括弧  不做处理？
                stack[0] = i

            # maxlen = max(maxlen, tmplen)
        return maxlen







