


rr = lambda x: reduce(lambda i,j:i+j,[x[i-1] for i in xrange(len(x),0,-1)])
pp = lambda s: rr(reduce(lambda a,b: a+b, [rr(str(s))[i]+"," if (i+1)%3==0 else rr(str(s))[i] for i in xrange(len(str(s)))] ))

if __name__ == "__main__":
    print "from add_comma import pp\n\npp(1000000)\n>>> {}".format(pp(1000000))
