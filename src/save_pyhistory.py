# coding: utf-8
print doc
import readline
print 'hello test'
import datetime
print datetime.datetime.now
print datetime.datetime.now()
readline.write_history_file()
get_ipython().magic(u'save save_pyhistory')
get_ipython().magic(u'save save_pyhistory 1-9')
