"""
#https://docs.python.org/3/howto/functional.html
Functional programming decomposes a problem into a set of functions.
Ideally, functions only take inputs and produce outputs, and don’t have any
internal state that affects the output produced for a given input.
Well-known functional languages include the ML family (Standard ML, OCaml,
and other variants) and Haskell.
"""


"""
# Nested loop procedural style for finding big products
xs = (1,2,3,4)
ys = (10,15,3,22)
bigmuls = []
# ...more stuff...
for x in xs:
    for y in ys:
        # ...more stuff...
        if x*y > 25:
            bigmuls.append((x,y))
            # ...more stuff...
# ...more stuff...
print bigmuls
"""

from pprint import pprint
pp = pprint


def dupelms_(lst,n):
    # N.B we can add additional variables to lambda with = operator
    L = map(lambda l,n_=n,g=0: [l]*n_, lst)
    G = reduce(lambda s,t: s+t, L)
    return G

def combine_(xs,ys):
    L = dupelms_(ys,len(xs))
    # Confusing, but map iterator to another iterator
    # basically == zipping two lists
    # i.e
    # map(None, [1,2], 'kk')    >> [(1, 'k'), (2, 'k')]
    # zip([1,2],'kk')           >> [(1, 'k'), (2, 'k')]
    G = map(None, xs*len(ys), L)
    return G

def bigmuls_(xs,ys):
    L = combine_(xs,ys)
    G = filter(lambda (x,y):x*y>25,L)
    return G

#dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
#combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
#bigmuls = lambda xs,ys: filter(lambda (x,y):x*y > 25, combine(xs,ys))
#print bigmuls((1,2,3,4),(10,15,3,22))

# decompose as def functions
#bigmuls_((1,2,3,4),(10,15,3,22))

# How it looks without nested functions
xs = (1,2,3,4)
ys = (10,15,3,22)
n = len(xs)

L = map(lambda l,n_=n: [l]*n_, ys)
L = reduce(lambda s,t: s+t, L)
L = map(None,xs*len(ys), L)
L = filter(lambda (x,y):x*y>25, L)
#print L


#>> [(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]
