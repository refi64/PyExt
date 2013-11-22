Tutorial
========

Function overloading
********************

PyExt lets you use funtion overloading with one limitation: all keyword arguments are ignored and not counted towards the argument count. Function overloading can be done either by argument count or argument count and argument types.

Here is an example on function overloading with `overload.argc`:

.. code-block:: python
   
   @overload.argc() # Automatically deduce argument count
   def x(a, b):
      print 'Function 1 called'
   
   @overload.argc(3) # Manually specified the argument count
   def x(a, b, c):
      print 'Function 2 called'
   
   x(1, 2)
   x(1, 2, 3)

And here is an example using `overload.args` (types and arg count):

.. code-block:: python
   
   @overload.args
   # TO BE CONTINUED!!

Runtime modules
***************

Runtime modules are complete module objects created at `runtime`. This means one important factor:

* ``inspect.getsource`` **will fail**!! This is do to the fact that the module file is set to ``<runtime_module>``, a (presumably) nonexistent file.

Note to self: need to add to horrible tutorial!
