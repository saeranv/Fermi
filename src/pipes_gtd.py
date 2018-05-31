# coding: utf-8
print np
get_ipython().magic(u'load "fermi/scratch.py"')
# %load "fermi/scratch.py"
import pandas as pd
import numpy as np
import pprint
pp = lambda x: pprint.pprint(x)
print np
print pp(range(1,10))
writer = pd.ExcelWriter("bash.xlsx")
f = open("bash3.txt","r")
L = []
for line in f: L.append(line)
f.close()
pp(L)
gtdmtx = df.DataFrame(np.array(L), columns="Task")
gtdmtx = pd.DataFrame(np.array(L), columns="Task")
gtdmtx = pd.DataFrame(np.array(L), columns=["Task"])
gtdmtx
gtdmtx.head()
get_ipython().magic(u'save "pipes_gtd" 1-17')
gtdmtx
gtdmtx.to_excel(pd.ExcelWriter("bash.xlsx")
)
writer = pd.ExcelWriter("bash2.xlsx")
gtdmtx.to_excel(writer,"A")
writer.save()
get_ipython().magic(u'save "pipes_gtd" 1-23')
