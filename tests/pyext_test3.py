from pyext import *
import pyext_test

class TestPyExt3(test.TestPyExt):
    def test_overload_args_annot(self):
        @overload.args(None)
        def x(a:int, b:str): return 0
        self.AssertEquals(x(1, 's'), 0)
        self.AssertRaises(TypeError, x, 1, 2)

