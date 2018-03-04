from nanoleaf2 import setPanel
from nanoleaf1 import setHue
from time import sleep


N= 5
color_tier = [(43,201,27),(113,214,20),(184,228,13),(255,242,7),(248,181,16),(242,121,25),(235,60,34),(229,0,43)]

setHue(255,0,100)

# Initial spending:
setPanel(0,color_tier[3])
setPanel(1,color_tier[4])
setPanel(2,color_tier[3])
setPanel(3,color_tier[2])
setPanel(4,color_tier[2])

# Initialize nanoleaf

wait = input('1')


#Spening on Transportation
setPanel(0,color_tier[3])
setPanel(1,color_tier[4])
setPanel(2,color_tier[3])
setPanel(3,color_tier[5])
setPanel(4,color_tier[2])


wait = input('2')

#Relax 3 days
setPanel(0,color_tier[2])
setPanel(1,color_tier[3])
setPanel(2,color_tier[2])
setPanel(3,color_tier[3])
setPanel(4,color_tier[1])

wait = input('3')

#Food
setPanel(0,color_tier[3])
setPanel(1,color_tier[3])
setPanel(2,color_tier[2])
setPanel(3,color_tier[3])
setPanel(4,color_tier[1])


wait = input('Stock market')

setPanel(0,color_tier[7])
setPanel(1,color_tier[7])
setPanel(2,color_tier[0])
setPanel(3,color_tier[7])
setPanel(4,color_tier[0])

wait = input('Go to IOT White-nr 3')

setPanel(0,(0,0,0))
setPanel(1,(0,0,0))
setPanel(2,(255,255,255))
setPanel(3,(0,0,0))
setPanel(4,(0,0,0))

wait = input('Go to slide 4')

setPanel(0,(0,0,0))
setPanel(1,(0,0,0))
setPanel(2,(0,0,0))
setPanel(3,(255,255,255))
setPanel(4,(0,0,0))

wait = input('Go to slide 5')

setPanel(0,(0,0,0))
setPanel(1,(0,0,0))
setPanel(2,(0,0,0))
setPanel(3,(0,0,0))
setPanel(4,(255,255,255))

wait = input('End of presentation')

setPanel(0,(0,0,0))
setPanel(1,(0,0,0))
setPanel(2,(0,0,0))
setPanel(3,(0,0,0))
setPanel(4,(0,0,0))
