
# vue2graph
# Clayton Brant, November 2018
# convert.py utilizes the graphconv.py file to convert a .vue format into a .graphml format (including custom yED elements for visual graphs)

import sys
import re
import os
import graphconv
from bs4 import BeautifulSoup

try:
    filename = sys.argv[1] #get the .vue file location from the command line

except:
    print("USAGE: python convert.py 'path/to/your/file/filename.vue'") #provide example usage to the user if they don't use the program properly

if '.vue' in filename: #only open the file if it has the .vue file type
    with open(os.path.join(filename)) as file:

        xml = file.read() # read the file as an xml document and parse with the beautiful soup library
    xml = re.sub("<child ID", "<child identity", xml, 0, re.I | re.M | re.DOTALL)
    soup = BeautifulSoup(xml,'lxml')

    G = graphconv.Graph() # instantiate the graphconvert.py class to begin creating valid graphml elements

    ids = soup.findAll("child") # the .vue format uses the "child" xml tag for each graph object. We only need these elements, everything else is discarded.

    for item in ids: # for each "child" element found in the .vue file we do this:

        font_info = item.font.text.split("-") # split the font tag in .vue using a hypen delimitter. .vue files combine the font style, family, and size into one tag, while graphml uses 3 seperate tags.

        if item.attrs['xsi:type'] == "node": # each graph node is makred as a 'node' tag in .vue file.
           node_shape = item.shape.attrs['xsi:type']

           if node_shape == "roundRect": # .vue files have nearly identicle shape names as graphml (yED) names, but rounded rectangles do not. Make the change here.
              node_shape = "roundrectangle"

           # add a node to the graphml file identicle to the one found in the .vue file. attributes are self explanitory.
           G.add_node (
           	item.attrs['identity'],
            label = item.attrs['label'],
            width = item.attrs['width'],
            height = item.attrs['height'],
            edge_width = item.attrs['strokewidth'],
            edge_color = item.strokecolor.text,
            x = item.attrs['x'],
            y = item.attrs['y'],
            shape = node_shape,
            shape_fill = item.fillcolor.text,
            font_family = font_info[0],
            font_style = font_info[1],
            font_size = font_info[2]
            )

        elif item.attrs['xsi:type'] == "link":
            G.add_edge(item.id1.text, item.id2.text, label = item.attrs['label'])

            #TODO
            #currently the edges are only simple arrows in the grapml file. Styles need to be added to the edges in the graphconv.py to change this.
    print G.get_graph()