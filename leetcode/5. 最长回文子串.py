'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = len(s)

        if l == 0:
            return s

        out = ""
        # maxlen = 0 

        '''
        "ab"这样的case没有考虑到
        '''
        out = s[0]
        maxlen = 1#记录长度

        '''
        回文子串为奇数长度
        '''
        for i in range(l):
            tmpl = 1
            step = 0 #描述左右跨度
            # while s[i - step] == s[i + step] and i - step > 0 and i + step < l:###这里把python的判断先后位置替换了之后会先判断是否满足前面的条件再判断是否满足后面的条件。
            while i - step >= 0 and i + step < l and  s[i - step] == s[i + step]:
                step += 1
            tmpl = tmpl + 2* (step - 1)
            if maxlen < tmpl:
                maxlen = tmpl
                out = s[i-(step-1) : i+(step-1)+1]
            # maxlen = max(maxlen, tmpl)

        '''
        回文子串为偶数长度
        '''
        for i in range(l):
            tmpl = 0
            step = 0 #描述左右跨度
            while i - step >= 0 and i - 1 + step < l and s[i - step] == s[i - 1 + step] :
                step += 1
            tmpl = tmpl + 2* (step - 1)
            if maxlen < tmpl:
                maxlen = tmpl
                out = s[i-(step-1) : i+step-2+1]
            # maxlen = max(maxlen, tmpl)

        return out
