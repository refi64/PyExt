import sys, inspect, types, unittest
from pyext import *

class TestPyExt(unittest.TestCase):
    def test_overload_argc(self):
        @overload.argc(1)
        def f(a): return 1
        @overload.argc(2)
        def f(a, b): return 2
        @overload.argc()
        def f(): return 0
        self.assertEqual(f(), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(1, 2), 2)
        self.assertRaises(TypeError, f, 1, 2, 3)
        self.assertEqual(len(inspect.getargspec(f).args), 0)
    def test_overload_args(self):
        @overload.args(str, int)
        def f(a, b): return str, int
        @overload.args(int)
        def f(a): return int
        @overload.args(str)
        def f(a): return str
        @overload.args()
        def f(): return
        self.assertEqual(f(), None)
        self.assertEqual(f(0), int)
        self.assertEqual(f('s'), str)
        self.assertEqual(f('s', 0), (str, int))
        self.assertRaises(TypeError, f, 0, 's')
        self.assertEqual(len(inspect.getargspec(f).args), 0)
    def test_module(self):
        m = RuntimeModule('s', 'doc', x=1, f=2)
        self.assertEqual(m.x, 1)
        self.assertEqual(m.f, 2)
        self.assertTrue(isinstance(m, types.ModuleType))
        self.assertEqual(m.__doc__, 'doc')
    def test_switch(self):
        with switch('x'):
            if case('a'): x = 1
            if case('b'): x = 2
            if case(1): x = 3
            if case('x'): x = 4
        self.assertEqual(x, 4)
    def test_annot(self):
        @fannotate('r', a='a' b=1, c=2)
        def x(a, b, c): pass
        self.assertEqual(x.__annotations__, {'a': 'a', 'b': 1, 'c': 2, 'return': 'r'})
    def test_unpack(self):
        t = (1, 2, 3)
        self.assertEqual(safe_unpack(t,2), (1,2))
        self.assertEqual(safe_unpack(t,4), (1,2,3,None))
        self.assertEqual(safe_unpack(t,4,fill=0), (1,2,3,0))
    def test_assign(self):
        self.assertEqual(assign('x', 7), 7)
        self.assertEqual(globals().get('x'), 7)
    if sys.version_info.major == 3:
        def test_overload_args_annot(self):
            def x(a, b): return 0
            x.__annotations__ = {'a': int, 'b': str}
            x = overload.args(None)(x)
            self.assertEqual(x(1, 's'), 0)
            self.assertRaises(TypeError, x, 1, 2)

if __name__ == '__main__':
    unittest.main()
