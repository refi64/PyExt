Tutorial
========

Function overloading
********************

PyExt function overloading is simple:

.. code-block:: python
   
   @overload.argc(1)
   def x(a): print 'Function 1 called'
   
   @overload.argc(2)
   def x(a, b): print 'Function 2 called'
   
   x(1)
   x(1, 2)

Easy, no? Now, if we wanted to overload by types also, we could do this:

.. code-block:: python
   
   @overload.args(int)
   def x(a): print 'Function 1 called'
   
   @overload.args(str)
   def x(a): print 'Function 2 called'
   
   x(1)
   x('s')

If you're in Python 3, you can also use function annotations by passing ``None`` as the parameter:

.. code-block:: python
   
   @overload.args(None)
   def x(a:int): print 'Function 1 called'
   
   @overload.args(None)
   def x(a:str): print 'Function 2 called'
   
   x(1)
   x('s')

Runtime Modules
***************

Runtime modules let you create a full module object at runtime. Here's an example:

.. code-block:: python
   
   mymodule = RuntimeModule.from_objects('module_name', 'module_docstring', a=1, b=2)
   import mymodule # Module object is added to sys.path
   print mymodule.a, mymodule.b

We can also create our module object from a string:

.. code-block:: python
   
   mystr = '''
   a = 1
   b = 2
   def do_nothing(x): return 'Nothing'
   '''
   RuntimeModule.from_string('module_name', 'module_docstring', mystr)
   import mymodule
   print mymodule.a, mymodule.b, mymodule.do_nothing(1)

Switch statement
****************

Switch statements are just as easy as everything else:

.. code-block:: python
   
   with switch('myval') as case:
       if case(1): print 'Huh?'
       if case(2): print 'What the...'
       if case('myval'): print "That's better!"

Tail recursion removal
**********************

Have you ever had a function that went way over the recursion limit? PyExt has a feature that eliminates that problem:

.. code-block:: python
   
   @tail_recurse()
   def add(a, b):
       if a == 0: return b
       return add(a-1, b+1)
   
   add(1000000, 1) # Doesn't max the recursion limit!

Function annotations
********************

PyExt lets you use Python 3's function annotations...on Python 2! Here is an example:

.. code-block:: python
   
   @annotate('a', b=1, ret='ret')
   def x(a, b):
      return 0

This is equilavent to:

.. code-block:: python3
   
   def x(a:'a', b:1) -> 'ret':
      return 0

Notice that, in the PyExt example, the first argument isn't a keyword arg. This is because PyExt automatically maps varargs to the equilavent function arguments.

Safe unpacking
**************

Say you have a string whose value is ``'a:b'``. Now, say you want to split this string at the colon. You'll probably do this:

.. code-block:: python
   
   a, b = my_string.split(':')

But what if ``my_string`` doesn't have a colon? You'll have to do this:

.. code-block:: python
   
   a, b = my_string.split(':') if ':' in my_string else (my_string, None)

Python 3 lets you simply do this:

.. code-block:: python3
   
   a, *b = my_string.split(':')

Also, with string partitioning, you can do this:

.. code-block:: python
   
   a, _, b = my_string.partition(':')

But say you're not working on a string. Say you're using a tuple:

.. code-block:: python
   
   a, b = my_tuple

If my_tuple isn't big enough or is too big, it'll throw an error. As stated above, Python 3 fixes this. But what if you're using Python 2? PyExt comes with a nifty function called ``safe_unpack`` that lets you do this:

.. code-block:: python
   
   a, b = safe_unpack(my_tuple, 2)

The first parameter is the sequence to unpack, while the second is the expected length. If the sequence is too large, the excess values are ignored. If it's too small, ``None`` is substituted in for the extra values.

You can also specify a value other than ``None`` to fill in the extra spaces:

.. code-block:: python
   
   a, b = safe_unpack(my_tuple, 2, fill='')
