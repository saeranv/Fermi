


rr = lambda x: reduce(lambda i,j:i+j,[x[i-1] for i in xrange(len(x),0,-1)])
csplit = lambda s: rr(reduce(lambda a,b: a+b, [rr(str(s))[i]+"," if ((i+1)%3==0 and i<len(str(s))-1) else rr(str(s))[i] for i in xrange(len(str(s)))] ))

if __name__ == "__main__":
    gJ2kWh = lambda gJ : gJ*1e6/3600
    print "#usage\nfrom cpslitter import csplit\n\ngJ2kWh = lambda gJ:gJ*1e6/3600\ncsplit(int(gJ2kWh(1000)))\n>>> {}".format(csplit(int(gJ2kWh(1000))))
