# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        self.l1 = self._node_to_list(l1)
        self.l2 = self._node_to_list(l2)
        self.l1_num = self._list_to_num(self.l1)
        self.l2_num = self._list_to_num(self.l2)
        self.sum = self.l1_num + self.l2_num
        self.l_res = self._num_to_rev_list(self.sum)
        return self._list_to_list_nodes(self.l_res)

    def __repr__(self):
        return f"{self.l1}, {self.l2}, {self.l1_num}, {self.l2_num}, sum:{self.sum}, {self.l_res}"

    def _list_to_num(self, l):
        num = ""
        for e in reversed(l):
            num += str(e)
        return int(num)

    def _node_to_list(self, n):
        if n is None:
            return None
        ln = n
        l = []
        l.append(ln.val)
        while ln.next is not None:
            ln = ln.next
            l.append(ln.val)
        return l

    def _num_to_rev_list(self, n):
        l = []
        for e in str(n):
            l += e
        r_l = list(reversed(l))

        r_l = [int(e) for e in r_l]

        return r_l

    def _num_to_list(self, n):
        l = []
        for e in str(n):
            l += e
        r_l = list(l)

        r_l = [int(e) for e in r_l]

        return r_l

    def _list_to_list_nodes(self, l):
        if l is None:
            return None

        ln = ListNode(l[0])
        ln_0 = ln
        for i in range(1, len(l)):
            ln.next = ListNode(l[i])
            ln = ln.next
        return ln_0


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    def print(self):
        ln = self
        print(ln.val)
        while ln.next is not None:
            ln = ln.next
            print(ln.val)


l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l11.next = l12
l12.next = l13

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)
l21.next = l22
l22.next = l23

s = Solution()
ln = s.addTwoNumbers(l11, l21)
ln.print()

l11 = ListNode(0)
l21 = ListNode(0)

ln = s.addTwoNumbers(l11, l21)
ln.print()


# now program it to with use of ListNode
