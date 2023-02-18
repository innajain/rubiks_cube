from vpython import *
from time import sleep
from random import randint

class base:
    class cube:
        def __init__(self, pos, color_dict) -> None:
            self.pos=pos
            self.dicto:dict[str, box]=dict()
            '''"front", "back", "left", "right", "top", "bottom"'''

            self.dicto["front"]=box(pos=pos+vector(0,0,0.5), size=vector(1,1,0.02), color=color_dict["front"])
            self.dicto["back"]=box(pos=pos+vector(0,0,-0.5), size=vector(1,1,0.02), color=color_dict["back"])
            self.dicto["left"]=box(pos=pos+vector(-0.5,0,0), size=vector(0.02,1,1), color=color_dict["left"])
            self.dicto["right"]=box(pos=pos+vector(0.5,0,0), size=vector(0.02,1,1), color=color_dict["right"])
            self.dicto["top"]=box(pos=pos+vector(0,0.5,0), size=vector(1,0.02,1), color=color_dict["top"])
            self.dicto["bottom"]=box(pos=pos+vector(0,-0.5,0), size=vector(1,0.02,1), color=color_dict["bottom"])
        def rotate(self, angle, axis, origin):
            for item in self.dicto:
                self.dicto[item].rotate(angle, axis, origin)
    class face:
        def __init__(self, pos, dict_temp) -> None:
            self.pos=pos
            self.dicto:dict[str, base.cube]=dict()
            '''"c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"'''
            self.dicto["c1"]=base.cube(pos+vector(-1.01, 1.01, 0), dict_temp["c1"])
            self.dicto["c2"]=base.cube(pos+vector(1.01, 1.01, 0), dict_temp["c2"])
            self.dicto["c3"]=base.cube(pos+vector(-1.01, -1.01, 0), dict_temp["c3"])
            self.dicto["c4"]=base.cube(pos+vector(1.01, -1.01, 0), dict_temp["c4"])
            self.dicto["e1"]=base.cube(pos+vector(0, 1.01, 0), dict_temp["e1"])
            self.dicto["e2"]=base.cube(pos+vector(-1.01, 0, 0), dict_temp["e2"])
            self.dicto["e3"]=base.cube(pos+vector(1.01, 0, 0), dict_temp["e3"])
            self.dicto["e4"]=base.cube(pos+vector(0, -1.01, 0), dict_temp["e4"])
            self.dicto["ct"]=base.cube(pos+vector(0, 0, 0), dict_temp["ct"])
    
    def __init__(self, smoothness=60, time=1) -> None:
        
        dict_temp=dict()
        dict_temp["c1"]={"front":color.white, "back":color.black, "left": color.green, "right": color.black, "top": color.orange, "bottom": color.black}
        dict_temp["c2"]={"front":color.white, "back":color.black, "left": color.black, "right": color.blue, "top": color.orange, "bottom": color.black}
        dict_temp["c3"]={"front":color.white, "back":color.black, "left": color.green, "right": color.black, "top": color.black, "bottom": color.red}
        dict_temp["c4"]={"front":color.white, "back":color.black, "left": color.black, "right": color.blue, "top": color.black, "bottom": color.red}
        dict_temp["e1"]={"front":color.white, "back":color.black, "left": color.black, "right": color.black, "top": color.orange, "bottom": color.black}
        dict_temp["e2"]={"front":color.white, "back":color.black, "left": color.green, "right": color.black, "top": color.black, "bottom": color.black}
        dict_temp["e3"]={"front":color.white, "back":color.black, "left": color.black, "right": color.blue, "top": color.black, "bottom": color.black}
        dict_temp["ct"]={"front":color.white, "back":color.black, "left": color.black, "right": color.black, "top": color.black, "bottom": color.black}
        dict_temp["e4"]={"front":color.white, "back":color.black, "left": color.black, "right": color.black, "top": color.black, "bottom": color.red}
        self.f1=base.face(vector(0,0,1.01), dict_temp)
        dict_temp=dict()
        dict_temp["c1"]={"front":color.black, "back":color.black, "left": color.green, "right": color.black, "top": color.orange, "bottom": color.black}
        dict_temp["c2"]={"front":color.black, "back":color.black, "left": color.black, "right": color.blue, "top": color.orange, "bottom": color.black}
        dict_temp["c3"]={"front":color.black, "back":color.black, "left": color.green, "right": color.black, "top": color.black, "bottom": color.red}
        dict_temp["c4"]={"front":color.black, "back":color.black, "left": color.black, "right": color.blue, "top": color.black, "bottom": color.red}
        dict_temp["e1"]={"front":color.black, "back":color.black, "left": color.black, "right": color.black, "top": color.orange, "bottom": color.black}
        dict_temp["e2"]={"front":color.black, "back":color.black, "left": color.green, "right": color.black, "top": color.black, "bottom": color.black}
        dict_temp["e3"]={"front":color.black, "back":color.black, "left": color.black, "right": color.blue, "top": color.black, "bottom": color.black}
        dict_temp["e4"]={"front":color.black, "back":color.black, "left": color.black, "right": color.black, "top": color.black, "bottom": color.red}
        dict_temp["ct"]={"front":color.black, "back":color.black, "left": color.black, "right": color.black, "top": color.black, "bottom": color.black}
        self.f2=base.face(vector(0,0,0), dict_temp)
        dict_temp["c1"]={"front":color.black, "back":color.yellow, "left": color.green, "right": color.black, "top": color.orange, "bottom": color.black}
        dict_temp["c2"]={"front":color.black, "back":color.yellow, "left": color.black, "right": color.blue, "top": color.orange, "bottom": color.black}
        dict_temp["c3"]={"front":color.black, "back":color.yellow, "left": color.green, "right": color.black, "top": color.black, "bottom": color.red}
        dict_temp["c4"]={"front":color.black, "back":color.yellow, "left": color.black, "right": color.blue, "top": color.black, "bottom": color.red}
        dict_temp["e1"]={"front":color.black, "back":color.yellow, "left": color.black, "right": color.black, "top": color.orange, "bottom": color.black}
        dict_temp["e2"]={"front":color.black, "back":color.yellow, "left": color.green, "right": color.black, "top": color.black, "bottom": color.black}
        dict_temp["e3"]={"front":color.black, "back":color.yellow, "left": color.black, "right": color.blue, "top": color.black, "bottom": color.black}
        dict_temp["e4"]={"front":color.black, "back":color.yellow, "left": color.black, "right": color.black, "top": color.black, "bottom": color.red}
        dict_temp["ct"]={"front":color.black, "back":color.yellow, "left": color.black, "right": color.black, "top": color.black, "bottom": color.black}
        self.f3=base.face(vector(0,0,-1.01), dict_temp)
        self.smoothness=smoothness
        self.time=time
 