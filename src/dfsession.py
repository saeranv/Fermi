# coding: utf-8
get_ipython().magic(u'load "fermi//scratch.py"')
# %load "fermi//scratch.py"
import pandas as pd
import numpy as np
import pprint
pp = lambda x: pprint.pprint(x)
get_ipython().magic(u'load "pipes_gtd.py"')
# %load "pipes_gtd.py"
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
# %load "fermi/scratch.py"
import pandas as pd
import numpy as np
import pprint
pp = lambda x: pprint.pprint(x)
# %load "pipes_gtd.py"
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
# %load "fermi/scratch.py"
import pandas as pd
import numpy as np
import pprint
pp = lambda x: pprint.pprint(x)
print gtdmtx
gtdmtx = pd.DataFrame(np.array(L), columns=["Task"])
gtdmtx.head
gtdmtx.head()
get_ipython().magic(u'cls ')
gtdmtx.head()
gtmtx.tail()
gtdmtx.tail()
get_ipython().magic(u'cls ')
gtdmtx.head()
gtdmtx.tail()
pp(dir(pd))
pp(pd.__doc__)
pd.ExcelWrite.__doc__
pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__ | less
print pd.ExcelWriter.__doc__ less
less print pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__
print pd.ExcelWriter.__doc__ | more
import pydoc
pydoc.pager(pd.ExcelWriter.__doc__)
get_ipython().magic(u'save dfsession')
get_ipython().magic(u'save dfsession 1-35')
