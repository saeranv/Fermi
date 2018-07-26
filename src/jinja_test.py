from loadenv import *
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

from osm_points_to_html import get_html

CURR_DIR = os.path.abspath(os.path.dirname("__file__"))


#t = Template("Hello {{ something }}")
#out = t.render(something = "world")

#print(type(out))

#t = Template("My favorite numbers: {% for n in range(1,10) %} {{n}} " "{% endfor %}")
#out = t.render()

#print(out)

N = 10
df = pd.DataFrame(index=range(N))
df['x'] = np.random.randn(N)
df['y'] = np.random.randn(N)
df['z'] = np.random.randn(N)

htmlfile = get_html(df,N)

#f = open(htmlfile,'r')
#htmllst = f.readlines()
#print(f.readlines.__doc__)
#f.close()
#html = reduce(lambda a,b: a+b, htmllst)

#t = Template(html)
#out = t.render()
#print(out)

templatedir = os.path.join(CURR_DIR,"src","templates")
env = Environment(loader=FileSystemLoader(templatedir))
template = env.get_template("trnco_fe.html")
output = template.render()

fh = open(os.path.join(CURR_DIR,"src","trnco_fe","trnco_fe.html"), "w")
fh.writelines(output)
fh.close()
