def foo():
    pass

function_name_as_string = 'foo'

globals()[function_name_as_string]() # foo().

"""
What if the function has many parameters like, def foo(a, b, c=false). How would you pass those parameters to globals() – ksooklall Sep 13 '17 at 16:19
@ksooklall You pass it to the function as usual: with def foo(*args): print("hw", *args) you can do: globals()['foo']() or globals()['foo']('reason', 42)
"""
