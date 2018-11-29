# Vue2Graph
Vue2Graph is a Python based tool that will convert a [Visual Understanding Environment](https://vue.tufts.edu/) file (.VUE) to a valid Graphml file for use in the [yED](https://yed.yworks.com/).

**Dependencies:**

 - [Python](https://www.python.org/) 2.7 or later
 - [Beautifulsoup4](https://pypi.org/project/bs4/) 

**Usage**
You can simply clone the repository and use it from the command line. 
(Please ensure you have installed any dependencies)

**Example 1:**

    python converter.py 'filename.vue'
This will print the converted file to the console. You can copy and paste it into an existing graphml file.

**Example 2:**

    python converter.py 'filename.vue' > newfile.graphml
This will save output to a valid graphml file for use in yED
