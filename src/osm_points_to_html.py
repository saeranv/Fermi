#from __future__ import print_function
#import pprint
#pp = lambda p: pprint.pprint(p)

from loadenv import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins


# Define some CSS to control our custom labels
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

def get_html(df,N):
    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)

    labels = []
    for i in range(N):
        label = df.ix[[i], :].T
        label.columns = ['Row {0}'.format(i)]
        # .to_html() is unicode; so make leading 'u' go away with str()
        labels.append(str(label.to_html()))

    points = ax.plot(df.x, df.y, 'o', color='b',
                     mec='k', ms=15, mew=1, alpha=.6)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('HTML tooltips', size=20)

    tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                       voffset=10, hoffset=10, css=css)
    plugins.connect(fig, tooltip)
    #print(tooltip.javascript())
    #pp(dir(plugins))
    html = mpld3.fig_to_html(fig)
    #mpld3.show()
    #return html
    htmlname = "mpl3test.html"
    CURR_DIR = os.path.abspath(os.path.dirname("__file__"))
    fname = os.path.join(CURR_DIR,"src","templates",htmlname)
    f = open(fname,'w')
    f.writelines(html)
    f.close()

    return htmlname

if __name__ == "__main__":
    N = 50
    df = pd.DataFrame(index=range(N))
    df['x'] = np.random.randn(N)
    df['y'] = np.random.randn(N)
    df['z'] = np.random.randn(N)

    get_html(df,N)
