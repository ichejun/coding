'''

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        '''
        执行用时：44 ms, 在所有 Python3 提交中击败了80.23%的用户
        内存消耗：13.7 MB, 在所有 Python3 提交中击败了7.14%的用户
        '''
        # p = out = ListNode(None)
        # while l1 and l2:
        #     # out.next = l1 if l1.val <= l2.val else l2
        #     if l1.val <= l2.val:
        #         out.next = l1
        #         l1 = l1.next
        #         out = out.next
        #     else:
        #         out.next = l2
        #         l2 = l2.next
        #         out = out.next
        # out.next = l1 if l1 else l2
        # return p.next

        '''
        这里想的有问题。。。。。。
        '''
        # #以l1为存放的目标对象
        # out = l1
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         pre = l1
        #         l1 = l1.next
        #     else:
        #         pre.next = l2
        #         l2 = l2.next
        #         pre = pre.next
        #         pre.next = l1

        # out.next = l1 if l1 else l2
        # return out

        '''
        递归
        '''
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2




            








