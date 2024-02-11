import unittest
from dsa.queue.static_queue import FixedSizeQueue
from dsa.common.exceptions import OverflowException, UnderflowException

class TestStaticQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = FixedSizeQueue(4)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_queue_is_empty_on_creation(self):
        self.assertTrue(self.queue.empty())

    def test_queue_enque_operation(self):
        
        self.assertTrue(self.queue.empty())
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
        self.assertEqual(8 , dequeued_element)

        dequeued_element = self.queue.dequeue()
        self.assertEqual(9 , dequeued_element)

        dequeued_element = self.queue.dequeue()
        self.assertEqual(11 , dequeued_element)

    def test_enqueue_operation_when_queue_has_space(self):
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.queue.enqueue(9)
        self.assertEqual("[5, 6, 7, 9]", str(self.queue))

        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()

        self.queue.enqueue(11)
        self.assertEqual("[9, 11]", str(self.queue))

    def test_enqueue_should_throw_overflow_when_queue_is_full(self):
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.queue.enqueue(9)

        with self.assertRaises(OverflowException) as ste:
            self.queue.enqueue(11)  
        self.assertEqual('Queue Overflow',ste.exception.getMessage())

    def test_dequeue_should_throw_underflow_when_queue_is_empty(self):
        with self.assertRaises(UnderflowException) as ste:
            self.queue.dequeue()  
        self.assertEqual('Queue Underflow',ste.exception.getMessage())



if __name__ == "__main__":
    unittest.main()
