from __future__ import print_function
from loadenv import *

#mpld3path = "C:\\Users\\kta_anypc\\Documents\\GitHub\\mpld3"
#if mpld3path not in sys.path:
#    sys.path.insert(0,mpld3path)

import mpld3
from mpld3 import plugins

import os

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

CURR_DIR = os.path.abspath(os.path.dirname("__file__"))
RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"), "src", "trnco_fe"))

def get_html(df,N):

    #width = 5 #pixels
    width = 400-20 #pixels
    height = 360-20 # pixels

    fig, ax = plt.subplots()#figsize=(width,height))

    width *= 1./fig.dpi
    height *= 1./fig.dpi

    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax.grid(True, alpha=0.3)

    #print("pixels", height, width)

    labels = []
    for i in range(N):
        label = df.ix[[i], :].T
        label.columns = ['Row {0}'.format(i)]
        # .to_html() is unicode; so make leading 'u' go away with str()
        labels.append(str(label.to_html()))

    labelcolor = 'red'
    bgcolor = 'white'
    ax.spines['bottom'].set_color(labelcolor)
    ax.spines['top'].set_color(labelcolor)
    ax.xaxis.label.set_color(labelcolor)
    ax.yaxis.label.set_color(labelcolor)
    ax.tick_params(axis='x', color = labelcolor)
    ax.tick_params(axis='y', color = labelcolor)

    points = ax.plot(df.x, df.y, 'o', color='red',
                     mec='k', ms=15, mew=1, alpha=.6)

    ax.grid(color=labelcolor)

    ax.set_facecolor(bgcolor)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    #ax.set_title('qxt test', size=10, color=labelcolor)


    tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                       voffset=10, hoffset=10)#, css=css)

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

def get_temp_osm_data():

    N = 50
    df = pd.DataFrame(index=range(N))
    df['x'] = np.random.randn(N)
    df['y'] = np.random.randn(N)
    df['z'] = np.random.randn(N)

    return df, N

def to_frontend(htmlfilename):

    templatedir = os.path.join(CURR_DIR,"src","templates")
    env = Environment(loader=FileSystemLoader(templatedir))
    template = env.get_template(htmlfilename)
    output = template.render()

    fh = open(os.path.join(CURR_DIR,"src","trnco_fe",htmlfilename), "w")
    fh.writelines(output)
    fh.close()


if __name__ == "__main__":

    df,N = get_temp_osm_data()
    htmlfile = get_html(df,N)
    to_frontend(htmlfile)
