'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class CQueue:

    def __init__(self):
        self.in_stack = []
        tmp = self.in_stack
        self.out_stack = []
        tmp2 = self.out_stack

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)
        tmp3 = self.in_stack

    def deleteHead(self) -> int:
        tmp3 = self.in_stack
        tmp4 = self.out_stack

        if not self.out_stack:
            if not self.in_stack:
                return -1
            else:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
                return self.out_stack.pop()
        else:
            return self.out_stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
