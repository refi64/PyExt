PyExt
=====

.. image:: https://travis-ci.org/kirbyfan64/PyExt.png
    :target: https://travis-ci.org/kirbyfan64/PyExt

Several simple extensions that add some nifty features to Python.

Some features:

- Function overloading
- Switch statement
- Runtime module creation
- Tail recursion removal
- Python 2 function annotations

Examples:

Function overloading::
   
   @overload.argc(1)
   def f(a): print 'Function 1 called'
   @overload.argc(2)
   def f(a, b): print 'Function 2 called'
   
   f(1)
   f(1, 2)

Switch statement::
   
   with switch(1) as case:
       if case(0): print 'Awkward...'
       if case(2): print '???'
       if case(1): print 'Phew! It works!'

Function annotations::
   
   @annotate(a=1, b=2, ret='return annotation')
   def x(a, b):
       return 0
