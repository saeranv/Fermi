# coding: utf-8
import pydoc
pg = lambda x: pydoc.pager(x)
get_ipython().magic(u'save "fermi//paginate.py"')
get_ipython().magic(u'save "fermi//paginate.py" 1-4')
