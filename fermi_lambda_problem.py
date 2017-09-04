import math

"""
https://stackoverflow.com/questions/31340781/list-argument-for-a-lambda-function-in-python
https://stackoverflow.com/questions/36181317/python-specify-lambda-arguments-as-a-function-argument
https://stackoverflow.com/questions/24403774/pass-list-as-one-of-functions-arguments


What you've done there is create a function object which references a variable,
it does not create its own copy, so that when you go to execute that function,
it looks up the variable, which now has the last value from the loop.

@Holt closure is probably the safest way to a accomplish the task, albeit a bit
more convoluted. I would change the name of my variable within the closure to
make it clearer what is happening.

What this does is create a separate scope, so that once execution leaves the
outer lambda function (having called it and returned a value which is the function
object you actually want) the count variable in your function object and the count
variable in your loop no longer reference the same place in memory, and you can
increment the counter without affecting the variable referenced by the function.

Q
https://stackoverflow.com/questions/46029578/list-of-lambda-functions-in-python-applies-lambda-to-final-value-of-iterator


"""


fx_lst = []
for k in range(1,3,1):
    print k
    func = lambda x_: k * x_
    fx_lst.append(func)

xlst = range(1,10,1)
for fx in fx_lst:
    ylst = map(lambda xin_: fx(xin_), xlst)
    print i, ylst
