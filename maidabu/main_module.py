import io
import os
from . import sub_module_a
from utils import raise_error
from sub_module_a import test_module_b


class TestModule:
    def __init__(self):
        self.a = 1
    
    def test_1(self):
        raise_error("test_1")

    def test_2(self):
        test_module_b.b_func()

