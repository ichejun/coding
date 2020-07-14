'''
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
通过次数119,582提交次数231,985

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        '''
        rule 1
        '''
        '''
        defaultdict接受一个工厂函数作为参数，如下来构造：
        dict =defaultdict( factory_function)
        这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0

        set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
        '''
        dic1 = defaultdict(int)
        for i in nums1:
            dic1[i] += 1

        dic2 = defaultdict(int)
        for i in nums2:
            dic2[i] += 1

        print (dic1)
        print (dic2)

        jiaoji = set(dic1) & set(dic2)
        print (jiaoji)

        print ('.....')
        print (dic1[9], dic2[9])

        dic3 = {i: min(dic1[i], dic2[i]) for i in jiaoji}

        print (dic3)

        for key, val in dic3.items():
            print (key, val)

        return sum([[key]*val for key, val in dic3.items()], [])        
        # return  [[key]*val for key, val in dic3.items()]


        '''
        rule 2
        collections --- 容器数据类型
        Counter  字典的子类，提供了可哈希对象的计数功能
        https://docs.python.org/zh-cn/3/library/collections.html
        '''
        # num1 = collections.Counter(nums1)
        # num2 = collections.Counter(nums2)
        # num = num1 & num2
        # return num.elements()
