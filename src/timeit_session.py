# coding: utf-8
a = "L=range(100)"
b = "for i in xrange(100): i"
timeit.timeit(a+b)
a = "L=range(100)\n"
timeit.timeit(a+b)
c = "for i in L: i"
timeit.timeit(a+c)
