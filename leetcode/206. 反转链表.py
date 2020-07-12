'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Nullnode = ListNode(None)
        Nullnode = (None)
        cur = Nullnode
        while head != None:
            tmp = head.next
            head.next = cur #head.next指向cur
            cur = head #将cur放在head的位置  这里需要理解的是，这里的所有的都是类似指针，不是实例。实例只有用类声明的时候才有。
            head = tmp
        return cur

        # pre = None
        # cur = head
        # while cur:
        #     temp = cur.next   # 先把原来cur.next位置存起来
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return pre
        


            









