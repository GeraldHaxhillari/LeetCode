# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_number = int(self.get_sequencial_number(l1)) + int(self.get_sequencial_number(l2))
        return self.number_to_list(None, sum_number)
        
    def get_sequencial_number(self, node):
        if node.next is None:
            return str(node.val)
        else:
            return self.get_sequencial_number(node.next) + str(node.val)
    
    def number_to_list(self, prev_node, number):
        if prev_node is None:
            cur_node = ListNode(number % 10)
            self.number_to_list(cur_node, number // 10)
            return cur_node
        elif number <= 0:
            pass
        else:
            cur_node = ListNode(number % 10)
            prev_node.next = cur_node
            self.number_to_list(cur_node, number // 10)
