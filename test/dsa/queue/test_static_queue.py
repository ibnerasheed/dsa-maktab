import unittest
from dsa.queue.static_queue import FixedSizeQueue

class TestStaticQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = FixedSizeQueue(4)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_queue_is_empty_on_creation(self):
        self.assertTrue(self.queue.empty())

    def test_queue_enque_operation(self):
        self.queue.enqueue(3)
        self.assertEqual("[3]", str(self.queue))
        self.queue.enqueue(6)
        self.assertEqual("[3, 6]", str(self.queue))
        self.queue.enqueue(9)
        self.assertEqual("[3, 6, 9]", str(self.queue))
        self.queue.enqueue(10)
        self.assertEqual("[3, 6, 9, 10]", str(self.queue))
        self.assertFalse(self.queue.empty())

    def test_queue_dequeue_operation(self):
        self.queue.enqueue(8)
        self.queue.enqueue(9)
        self.queue.enqueue(11)

        dequeued_element = self.queue.dequeue()
        self.assertEqual("[9, 11]", str(self.queue))

        dequeued_element = self.queue.dequeue()
        self.assertEqual("[11]", str(self.queue))

        dequeued_element = self.queue.dequeue()
        self.assertEqual("[]", str(self.queue))






if __name__ == "__main__":
    unittest.main()
