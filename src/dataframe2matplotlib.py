from __future__ import print_function
from loadenv import *
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
import parse_osm

# set background style

CURR_DIR = os.path.abspath(os.path.dirname("__file__"))
RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"), "src", "trnco_fe"))

def set_style():
    """
    ref:
    'seaborn-darkgrid',
    'Solarize_Light2',
    'seaborn-notebook',
    'classic',
    'seaborn-ticks',
    'grayscale',
    'bmh',
    'seaborn-talk',
    'dark_background',
    'ggplot',
    'fivethirtyeight',
    '_classic_test',
    'seaborn-colorblind',
    'seaborn-deep',
    'seaborn-whitegrid',
    'seaborn-bright',
    'seaborn-poster',
    'seaborn-muted',
    'seaborn-paper',
    'seaborn-white',
    'fast',
    'seaborn-pastel',
    'seaborn-dark',
    'tableau-colorblind10',
    'seaborn',
    'seaborn-dark-palette'
    """
    plt.style.use('dark_background')
    #plt.style.use('fivethirtyeight')

def scatterplot(df):

    set_style()

    N = df.shape[1]
    #width = 5 #pixels
    width = 670  #400-20 #pixels
    height = 580 #360-20 # pixels

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

    """
    labelcolor = 'red'
    bgcolor = 'black'
    ax.spines['bottom'].set_color(labelcolor)
    ax.spines['top'].set_color(labelcolor)
    ax.xaxis.label.set_color(labelcolor)
    ax.yaxis.label.set_color(labelcolor)
    ax.tick_params(axis='x', color = labelcolor)
    ax.tick_params(axis='y', color = labelcolor)
    """
    points = ax.plot(df.x, df.y, 'o', color='red',
                     mec='k', ms=15, mew=1, alpha=.6)

    #ax.grid(color=labelcolor)
    #ax.set_facecolor(bgcolor)
    #ax.set_facecolor("black")
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    #plt.show()

    save_as_static_img()

def save_as_static_img():
    img_dir = os.path.join(CURR_DIR,"src","trnco_fe","img")
    img_path = os.path.join(img_dir, "matplotlib.png")

    plt.savefig(img_path, bbox_inches='tight')


def save_as_canvas():
    # To make html-embedded pyqt widgets:
    #https://wiki.python.org/moin/PyQt/Embedding%20Widgets%20in%20Web%20Pages

    # To add mpl to pyqt widget
    #https://stackoverflow.com/questions/12459811/how-to-embed-matplotlib-in-pyqt-for-dummies

    pass


if __name__ == "__main__":

    df,osm,ops = parse_osm.main()
    scatterplot(df)
    #to_frontend()
