


rr = lambda x: reduce(lambda i,j:i+j,[x[i-1] for i in xrange(len(x),0,-1)])
csplit = lambda s: rr(reduce(lambda a,b: a+b, [rr(str(s))[i]+"," if (i+1)%3==0 else rr(str(s))[i] for i in xrange(len(str(s)))] ))

if __name__ == "__main__":
    print "from cpslitter import csplit\n\npp(1000000)\n>>> {}".format(csplit(1000000))
