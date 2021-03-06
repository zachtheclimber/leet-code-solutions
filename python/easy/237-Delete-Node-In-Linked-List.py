import unittest
from models.linkedList import ListNode


# O(n) time, O(1) space solution
def del_node(node: ListNode):
    while node.next.next:
        node.val = node.next.val
        node = node.next
    node.val = node.next.val
    node.next = None


class TestDeleteNode(unittest.TestCase):

    def test_4519_5(self):
        head = ListNode.build([4, 5, 1, 9])
        node = head.next
        del_node(node)
        out_list = ListNode.build([4, 1, 9])
        self.assertEqual(head, out_list)

    def test_4519_1(self):
        head = ListNode.build([4, 5, 1, 9])
        node = head.next.next
        del_node(node)
        out_list = ListNode.build([4, 5, 9])
        self.assertEqual(head, out_list)

    def test_45_4(self):
        head = ListNode.build([4, 5])
        node = head
        del_node(node)
        out_list = ListNode.build([5])
        self.assertEqual(head, out_list)


if __name__ == "__main__":
    unittest.main()
