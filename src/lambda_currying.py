import math

"""


Q
https://stackoverflow.com/questions/46029578/list-of-lambda-functions-in-python-applies-lambda-to-final-value-of-iterator


What's happening is that your lambdas are being bound to the loop
variable k rather than the value associated with it. The loop
variable k persists even after the loop, and so those lambdas have
access to it.

"""

print 'git check'

# explaination
# https://mtomassoli.wordpress.com/2012/03/18/currying-in-python/

fx_lst = []
for k in range(1,3,1):
    print k
    func = (lambda k=k: lambda x_: k * x_)(k)
    fx_lst.append(func)

xlst = range(1,10,1)
for fx in fx_lst:
    ylst = []
    for xin_ in xlst:
        ylst.append(fx(xin_))
    print ylst


# functional line from slope and y-intercept
# https://stackoverflow.com/questions/24881604/when-should-i-use-function-currying-in-python
def simple_function(a):
    def line(b=0):
        def compute(x):
            return [a + b * xi for xi in x]
        return compute
    return line

x = range(-4, 4, 1)
print('x {}'.format(list(x)))
print('constant {}'.format(simple_function(3)()(x)))
print('line {}'.format(simple_function(3)(-2)(x)))
# gives

# x [-4, -3, -2, -1, 0, 1, 2, 3]
# constant [3, 3, 3, 3, 3, 3, 3, 3]
# line [11, 9, 7, 5, 3, 1, -1, -3]
# Now this was not yet that exciting. It only replaced functions calls of type f(a,b,c) with calls of type  f(a)(b)(c) which might even be seen as the less elegant style in Python.

# But it allows you to do:

line_through_zero = simple_function(0)
print('line through zero {}'.format(line_through_zero(1)(x))) # only slope and x

# which gives
# line through zero [-4, -3, -2, -1, 0, 1, 2, 3]