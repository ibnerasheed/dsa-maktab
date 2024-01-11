import unittest
from dsa.queue.static_queue import FixedSizeQueue

class TestStaticQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = FixedSizeQueue(5)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_queue_is_empty_on_creation(self):
        self.assertTrue(self.queue.empty())

    def test_    


if __name__ == "__main__":
    unittest.main()
