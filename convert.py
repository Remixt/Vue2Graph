import sys
from bs4 import BeautifulSoup
import re
import os
import graphconv  
filename = ""
try:
    filename = sys.argv[1]
except:
    print("USAGE: python convert.py 'path/to/your/file/filename.vue'")

if '.vue' in filename:
    with open(os.path.join(filename)) as file:
        xml = file.read()
    xml = re.sub("<child ID", "<child identity", xml, 0, re.I | re.M | re.DOTALL)
    soup = BeautifulSoup(xml,'lxml')
    G = graphconv.Graph()
    ids = soup.findAll("child")
    edgestart = soup.findAll("id1")
    edgefinish = soup.findAll("id2")
    for item in ids:
        font_info = item.font.text.split("-")
        if item.attrs['xsi:type'] == "node":
           node_shape = item.shape.attrs['xsi:type']
           if node_shape == "roundRect":
              node_shape = "roundrectangle"
           G.add_node(item.attrs['identity'], label = item.attrs['label'], width = item.attrs['width'], height = item.attrs['height'],
             edge_width = item.attrs['strokewidth'], x = item.attrs['x'], y = item.attrs['y'], shape = node_shape,
             shape_fill = item.fillcolor.text, edge_color = item.strokecolor.text, font_family = font_info[0], font_style = font_info[1], font_size = font_info[2]
             )
        elif item.attrs['xsi:type'] == "link":
            G.add_edge(item.id1.text, item.id2.text, label = item.attrs['label'])
    print G.get_graph()