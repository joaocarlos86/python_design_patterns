# Strategy Design Pattern

This is the first commit of a try to implement the Strategy design
pattern using Python. This implementation is derived of previous
implementations in Java language. Maybe I'm not using all the resources
that I could use in Python, but I think it is good enough.

To add a new Strategy the user needs to create a new Class (hopefully a
new file as well), subclass the ABC Strategy and implement at least two methods:

* supports
* execute

The support methods will be called be the Executor to check if this
strategy is suitable to process the desired input, if yes then the
executor will call the execute method.

At the Executor file, we need to import the new module and the class
created and then add the strategy to the list of strategies.

