'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        out = p = ListNode(None) # out为首地址用于输出，p用在内部轮询
        jinwei = 0
        # print (l1)
        # print (l1.val)
        # print (l1.next)

        # print (p)

        while l1 or l2 or jinwei:
            he = jinwei + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # p.val = he%10 # 这里对之前定义的ListNode类的理解不够，ListNode包含两个变量一个是val是值，另一个next用于指向下一个ListNode
            #一开始定义时p就是空的，也就val和next都是none的listnode
            #后面新加节点的时候需要保证 要么next指向none，要么指向下一个listnode实例，也就是要新奇一个listnode实例。
            p.next = ListNode(he%10) #向p.next里面放东西

            # print ()
            # print (p)

            jinwei = he//10 
            p = p.next #链表进到下一个节点。

            # print(l1)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # print(l1)
        
        return out.next

 
 
        # lenl1 = len(l1)
        # lenl2 = len(l2)
        # maxlen = max(lenl1, lenl2)
        # minlen = max(lenl1, lenl2)
        # out = []
        # for i in range(minlen):
        #     tmp = l1[i] + l2[i] + jinwei
        #     jinwei = tmp // 10
        #     out[i] = tmp % 10
