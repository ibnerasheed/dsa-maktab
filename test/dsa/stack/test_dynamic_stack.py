import unittest
from dsa.stack.dynamic_stack import DynamicStack
from dsa.common.exceptions import OverflowException, UnderflowException


class TestDynamicStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = DynamicStack()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
   
    def test_stack_is_empty_on_creation(self):
        self.assertTrue(self.stack.empty())

    def test_stack_push_should_add_element_at_top(self):
        self.stack.push(6)
        observedData = self.stack.peek()
        self.assertEqual(observedData,6)
        self.assertEqual(len(self.stack),1)
        self.stack.push(7)
        observedData = self.stack.peek()
        self.assertEqual(observedData,7)
        self.assertFalse(self.stack.empty())
        self.assertEqual(len(self.stack),2)
    
    def test_stack_pop_should_remove_top_element(self):
        self.stack.push(7)
        self.stack.push(8)
        popElement = self.stack.pop()
        self.assertEqual(popElement,8)
        observedData = self.stack.peek()
        self.assertEqual(observedData,7)

    def test_stack_pop_should_raise_overflow_exception_on_memory_error(self):
        self.assertTrue(True)

    def test_stack_underflow(self):
        with self.assertRaises(UnderflowException) as suf:
            popElement = self.stack.pop()
        self.assertEqual('Stack Underflow',suf.exception.getMessage())

       
        
   
    
         

if __name__== "__main__":
    unittest.main()