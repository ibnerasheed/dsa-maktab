import unittest
from dsa.stack.fixed_size_stack import FixedSizeStack
from dsa.common.exceptions import OverflowException,UnderflowException

class TestFixedSizeStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = FixedSizeStack(5)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_stack_is_empty_on_creation(self):
        self.assertTrue(self.stack.empty())

    def test_stack_push_operation(self):
        self.stack.push(6)
        observedData = self.stack.peek()
        self.assertEqual(observedData,6)
        self.assertEqual(len(self.stack),1)
        self.stack.push(7)
        observedData = self.stack.peek()
        self.assertEqual(observedData,7)
        self.assertFalse(self.stack.empty())
        self.assertEqual(len(self.stack),2)

    def test_stack_pop_operation(self):
        self.stack.push(7)
        self.stack.push(8)
        popElement = self.stack.pop()
        self.assertEqual(popElement,8)
        observedData = self.stack.peek()
        self.assertEqual(observedData,7)

    def test_stack_overflow(self):
        self.stack.push(1)  
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)  
        with self.assertRaises(OverflowException) as ste:
            self.stack.push(6)  
        self.assertEqual('Stack Overflow',ste.exception.getMessage())
        
    def test_stack_underflow(self):
        with self.assertRaises(UnderflowException) as suf:
            popElement = self.stack.pop()
        self.assertEqual('Stack Underflow',suf.exception.getMessage())
  
if __name__== "__main__":
    unittest.main()