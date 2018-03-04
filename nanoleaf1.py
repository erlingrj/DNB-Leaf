from nanoleaf import Aurora
from nanoleaf import setup

IP = "192.168.0.199"
TOKEN = "fVMeVawqyiquFcIn7fDKN4bZNz0BnhUS"


my_aurora = Aurora(IP,TOKEN)


my_aurora.on = True



def setHue(hue,sat,bright):
    effect_data = {
        "command": "add",
        "animName": "My Random Animation1",
        "animType": "solid",
        "colorType": "HSB",
        "animeData": None,
        "palette": [
            {
                "hue": hue,
                "saturation": sat,
                "brightness": bright
            },
        ],

    }

    my_aurora.effect_set_raw(effect_data)



    my_aurora.effect = "My Random Animation1"
