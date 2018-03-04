from nanoleaf1 import setHue
import nanoleaf2
import time

setHue(0,100,255)

time.sleep(0.5)

setHue(150,100,255)

time.sleep(0.5)

setHue(255, 100, 255)

time.sleep(0.5)

nanoleaf2.turnOff()
