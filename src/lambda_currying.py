import math

"""


Q
https://stackoverflow.com/questions/46029578/list-of-lambda-functions-in-python-applies-lambda-to-final-value-of-iterator


What's happening is that your lambdas are being bound to the loop
variable k rather than the value associated with it. The loop
variable k persists even after the loop, and so those lambdas have
access to it.

Currying means decomposing a function that takes multiple arguments
into a function that takes the first argument and returns a function
that takes the next argument, and so forth for all the arguments.

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
