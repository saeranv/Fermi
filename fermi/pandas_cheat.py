import pandas as pd
import numpy as np
import pdb

def main():
    """ numpy cheat """
    vec = np.array([1.,2.,3.])
    mat = np.array([[1.,2.,3.],[4.,5.,6.]])
    vec2 = np.arange(3)
    mat2 = np.arange(12).reshape(4,3)
    pdb.set_trace()
    # We can perform vectorized functions on this!
    vec *= 2
    #print vec
    vecdot = vec.dot(vec2)
    #print vecdot

    """ pandas cheat """
    # panda series: 1d labeled array
    data = np.array([1,3,5,np.nan,6,8])
    labels = ["ex-"+str(x) for x in range(len(data))]
    s = pd.Series(data,labels)
    #print s

    # panda dataframe: 2d labeled data structure
    data = np.arange(12).reshape(2,6)
    pdf = pd.DataFrame(data, \
        index=["ex-"+str(x) for x in xrange(2)], \
        columns=["cx-"+str(x) for x in xrange(6)])
    #print pdf

    # define colums via dictionary
    pdf = pd.DataFrame({"one": np.arange(6),\
                        "two": np.arange(6)})
    print pdf

if __name__ == "__main__":
    main()
