'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:



 

示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明:

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next


'''
将当前节点的值和指针都修改为下一个节点的值和指针即可，相当于让当前节点冒充下一个节点，那么远离啊的当前节点被修改消除，原来节点的下一位节点因为没有被指针连接而失去意义
此题考查python函数的传参形式为“传对象引用”，相当于浅拷贝（对于可变对象来说）

细节补充
node = node.next是不行的，因为这里只是改了函数参数引用的对象，而原来传进来的 node 没有任何改变
详细说明：如果Python的函数得到的参数是可变对象（比如list，set，这样的，内部属性可以改变的），那么我们实际得到的是这个对象的浅拷贝。比如这个函数刚刚开始的时候题目传进来一个参数node，我们设这个节点为A，那么实际上得到的参数node是一个对于A的一个浅拷贝，你可以想象node是一把钥匙，它可以打开真正的节点A的门，如果我们现在让node = node.next，那么我们只是换了钥匙，变成了打开 A.next 的门的对应的钥匙，因此链表没有被修改， A没有被修改，只是我们手里的钥匙变了。而如果我们直接写node.val, node.next = node.next.val, node.next.next，就相当于我们先用钥匙找到 A 的门，然后修改了 A 的属性，链表发生变化

作者：QQqun902025048
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list/solution/1-xing-python-xiang-jie-by-knifezhu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
