
from nanoleaf import Aurora
from nanoleaf import setup

import nanoleaf1
from nanoleaf1 import setHue


IP = "192.168.0.199"
TOKEN = "fVMeVawqyiquFcIn7fDKN4bZNz0BnhUS"
PANEL_ID = ["1 141 1 ","1 242 1 ", "1 223 1 ", "1 91 1 ", "1 228 1 "]


my_aurora = Aurora(IP,TOKEN)

my_aurora.on = True




T = 20
def testFuntion():
    R1 = 255
    G1 = 0
    B1 = 0

    R2 = 0
    G2 = 255
    B2 = 0

    R3 = 0
    G3 = 0
    B3 = 255

    R4 = 255
    G4 = 255
    B4 = 0

    R5 = 0
    G5 = 255
    B5 = 255


    data1 = "5 141 1 " + str(R1) + " " + str(G1) + " " + str(B1) + " 0 " + str(T)
    data2 = "5 242 1 " + str(R2) + " " + str(G2) + " " + str(B2) + " 0 " + str(T)
    data3 = "5 223 1 " + str(R3) + " " + str(G3) + " " + str(B3) + " 0 " + str(T)
    data4 = "5 91 1 " + str(R4) + " " + str(G4) + " " + str(B4) + " 0 " + str(T)
    data5 = "5 228 1 " + str(R5) + " " + str(G5) + " " + str(B5) + " 0 " + str(T)


    effect_data = {
        "command" : "add",
        "animName" : "My Static Animation1",
        "animType" : "static",
        "animData" : data1+data2+data3+data4+data5,
        "loop" : False}

    my_aurora.on = True
    my_aurora.effect_set_raw(effect_data)


def setPanel(panelID, RGB):
    animData = PANEL_ID[panelID] + str(RGB[0]) + " " + str(RGB[1]) + " " + str(RGB[2]) + " 0 " + str(T)

    effect_data = {
        "command" : "add",
        "animName" : "The Matrix",
        "animType" : "static",
        "animData" : animData,
        "loop" : False}
    my_aurora.on = True
    my_aurora.effect_set_raw(effect_data)


def turnOff():
    setPanel(0,(0,0,0))
    setPanel(1,(0,0,0))
    setPanel(2,(0,0,0))
    setPanel(3,(0,0,0))
    setPanel(4,(0,0,0))
    my_aurora.on = False



setPanel(0,(255,255,255))
setPanel(1,(255,255,255))
setPanel(2,(255,255,255))
setPanel(3,(255,255,255))
setPanel(4,(255,255,255))
