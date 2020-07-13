'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 or len(s) == 1:
            return len(s)

        valueSet = set()
        winStart = 0
        winEnd = 1
        length = 0
        maxlen = 0
        valueSet.add(s[0])
        for winStart in range(len(s)):
            while( winEnd < len(s) and (s[winEnd] not in valueSet) ):
                valueSet.add(s[winEnd])
                winEnd += 1 #end右移
            length = winEnd - winStart # 这里其实应该是 （winEnd - 1） - winStart + 1 才是正确的index对应的序号。
            valueSet.remove(s[winStart])
            maxlen = max(maxlen, length)

        return maxlen



