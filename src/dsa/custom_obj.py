from functools import total_ordering
from typing import Any

@total_ordering
class CustomObj:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"[Key: {self.key}, value: {self.value}]"    
    
    def __str__(self) -> str:
        return f"[Key: {self.key}, value: {self.value}]"

    def __lt__(self, other):
        return self.key < other.key  

    def __eq__(self, other):
        return self.key == other.key  
    
    def __get