# demo5

# Green + Green + Yellow + Red + Yellow

from nanoleaf2 import setPanel
N = 5

color_tier = [(43,201,27),(113,214,20),(184,228,13),(255,242,7),(248,181,16),(242,121,25),(235,60,34),(229,0,43)]

setPanel(0,color_tier[7])
setPanel(1,color_tier[0])
setPanel(2,color_tier[0])
setPanel(3,color_tier[7])
setPanel(4,color_tier[7])
