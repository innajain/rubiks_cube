from vpython import *
from time import sleep
from random import randint

from cube_class import Cube


class methods(Cube):
    def move(self, char):
        if char=="U":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "e1", "c2"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c2", "e1", "c1"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        elif char=="U_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "e1"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "e1", "c2"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="D":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c3", "c4", "e4"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=a
            a=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="D_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c3", "c4", "e4"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=a
            a=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        elif char=="R":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c2", "c4", "e3"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=a
            a=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c2", "e3", "c4"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=a
        elif char=="R_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c2", "c4", "e3"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=a
            a=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c2", "e3", "c4"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=a
        elif char=="L":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c3", "e2"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=a
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "e2", "c3"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=a
        elif char=="L_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c3", "e2"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=a
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "e2", "c3"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=a
        elif char=="F":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    self.f1.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=a
            for item in [self.f1]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="F_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    self.f1.dicto[cb].rotate(pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=a
            for item in [self.f1]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        elif char=="B":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    self.f3.dicto[cb].rotate(pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=a
            a=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=a
            for item in [self.f3]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        elif char=="B_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    self.f3.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=a
            a=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=a
            for item in [self.f3]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="M1u":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["e1", "ct", "e4"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["e1", "ct", "e4"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=a
        elif char=="M1d":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["e1", "ct", "e4"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["e1", "ct", "e4"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=a
        elif char=="M2r":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["e2", "ct", "e3"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["e2", "ct", "e3"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="M2l":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["e2", "ct", "e3"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["e2", "ct", "e3"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        elif char=="M3":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    self.f2.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=a
            a=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=a
            for item in [self.f2]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="M3_":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    self.f2.dicto[cb].rotate(pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=a
            a=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=a
            for item in [self.f2]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a

    def rotate(self, char):
        if char=="u":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=a
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=a
            a=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=a
            a=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=a
        elif char=="d":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(1,0,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=a
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=a
            a=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=a
            a=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=a
        elif char=="r":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=a
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=a
            a=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=a
            a=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="l":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,1,0), vector(0,0,0))
            a=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=a
            a=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=a
            a=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=a
            a=self.f1.dicto["ct"]
            self.f1.dicto["ct"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=self.f3.dicto["ct"]
            self.f3.dicto["ct"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=a
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                    a=item.dicto[cb].dicto["front"]
                    item.dicto[cb].dicto["front"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["back"]
                    item.dicto[cb].dicto["back"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        elif char=="cw":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                        item.dicto[cb].rotate(-pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=a
            a=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=a
            a=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=a
            a=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=a
            a=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=a
        elif char=="acw":
            for i in range(self.smoothness):
                sleep(self.time/self.smoothness)
                for item in [self.f1, self.f2, self.f3]:
                    for cb in ["c1", "c2", "c3", "c4", "e1", "e2", "e3", "e4", "ct"]:
                        item.dicto[cb].rotate(pi/2/self.smoothness, vector(0,0,1), vector(0,0,0))
            a=self.f1.dicto["c1"]
            self.f1.dicto["c1"]=self.f1.dicto["c2"]
            self.f1.dicto["c2"]=self.f1.dicto["c4"]
            self.f1.dicto["c4"]=self.f1.dicto["c3"]
            self.f1.dicto["c3"]=a
            a=self.f1.dicto["e1"]
            self.f1.dicto["e1"]=self.f1.dicto["e3"]
            self.f1.dicto["e3"]=self.f1.dicto["e4"]
            self.f1.dicto["e4"]=self.f1.dicto["e2"]
            self.f1.dicto["e2"]=a
            a=self.f2.dicto["c1"]
            self.f2.dicto["c1"]=self.f2.dicto["c2"]
            self.f2.dicto["c2"]=self.f2.dicto["c4"]
            self.f2.dicto["c4"]=self.f2.dicto["c3"]
            self.f2.dicto["c3"]=a
            a=self.f2.dicto["e1"]
            self.f2.dicto["e1"]=self.f2.dicto["e3"]
            self.f2.dicto["e3"]=self.f2.dicto["e4"]
            self.f2.dicto["e4"]=self.f2.dicto["e2"]
            self.f2.dicto["e2"]=a
            a=self.f3.dicto["c1"]
            self.f3.dicto["c1"]=self.f3.dicto["c2"]
            self.f3.dicto["c2"]=self.f3.dicto["c4"]
            self.f3.dicto["c4"]=self.f3.dicto["c3"]
            self.f3.dicto["c3"]=a
            a=self.f3.dicto["e1"]
            self.f3.dicto["e1"]=self.f3.dicto["e3"]
            self.f3.dicto["e3"]=self.f3.dicto["e4"]
            self.f3.dicto["e4"]=self.f3.dicto["e2"]
            self.f3.dicto["e2"]=a
            for item in [self.f1, self.f2, self.f3]:
                for cb in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]:
                    a=item.dicto[cb].dicto["top"]
                    item.dicto[cb].dicto["top"]=item.dicto[cb].dicto["right"]
                    item.dicto[cb].dicto["right"]=item.dicto[cb].dicto["bottom"]
                    item.dicto[cb].dicto["bottom"]=item.dicto[cb].dicto["left"]
                    item.dicto[cb].dicto["left"]=a
        else:
            raise Exception

    def scramble(self, num:int=20, history:bool=False, fast:bool=False):
        if history: fp=open("scramble.txt", 'w')
        if fast:
            org=(self.time, self.smoothness)
            self.time=0.1
            self.smoothness=15
        lst=["U", "U_", "D", "D_", "F", "F_", "B", "B_", "L", "L_", "R", "R_", "M1u", "M1d", "M2r", "M2l", "M3", "M3_"]
        for _ in range(num):
            i=randint(0,17)
            self.move(lst[i])
            if history: fp.writelines(lst[i]+"\n")
        if fast:
            self.time=org[0]
            self.smoothness=org[1]
            fp.close()

    def commander(self):
        lst=["U", "U_", "D", "D_", "F", "F_", "B", "B_", "L", "L_", "R", "R_", "M1u", "M1d", "M2r", "M2l", "M3", "M3_"]
        while True:
            a=input("Give command: ")

            if a=="solve":
                self.solve()
            elif a in lst:
                self.move(a)
            elif a[0:4]=="rot ":
                self.rotate(a[4:])
            elif a=="scramble":
                self.scramble()
            elif a=="exit":
                break
            else:
                print("Wrong command")

    
    def show(self, name:str = "image"):
        import cv2
        import numpy

        rows=900
        cols=1600
        size_face=270
        top_gap=(rows-3*size_face)//2
        side_gap=(cols-4*size_face)//2
        
        white=[255,255,255]
        orange=[0,112,232]
        green=[84,157,0]
        blue=[246, 129, 61]
        red=[47, 66, 220]
        yellow=[0, 255, 255]
        black=[0,0,0]

        def get_color(char: str):
            if char== vector(1,1,1):
                return white
            elif char==vector(1,0.6,0):
                return orange
            elif char==vector(0,1,0):
                return green
            elif char==vector(0,0,1):
                return blue
            elif char==vector(1,0,0):
                return red
            elif char==vector(1,1,0):
                return yellow
            elif char==vector(0,0,0):
                return black
            else:
                raise Exception(f"{char}")
        
        arr=numpy.array([[[0]*3]*cols]*rows)
        # front
        lst=["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]
        for k in range(9):
            color =  get_color(self.f1.dicto[lst[k]].dicto["front"].color)
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face + size_face//3 * (k%3), side_gap + size_face + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # top
        lst1=[self.f3, self.f2, self.f1]
        lst2=["c1", "e1", "c2"]
        for k in range(9):
            color =  get_color(lst1[k//3].dicto[lst2[k%3]].dicto["top"].color)
            for i in range(top_gap + size_face//3*(k//3), top_gap + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face + size_face//3 * (k%3), side_gap + size_face + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # left
        lst1=[self.f3, self.f2, self.f1]
        lst2=["c1", "e2", "c3"]
        for k in range(9):
            color =  get_color(lst1[k%3].dicto[lst2[k//3]].dicto["left"].color)
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face//3 * (k%3), side_gap + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # right
        lst1=[self.f1, self.f2, self.f3]
        lst2=["c2", "e3", "c4"]
        for k in range(9):
            color =  get_color(lst1[k%3].dicto[lst2[k//3]].dicto["right"].color)
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face*2 + size_face//3 * (k%3), side_gap + size_face*2 + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # bottom
        lst1=[self.f1, self.f2, self.f3]
        lst2=["c3", "e4", "c4"]
        for k in range(9):
            color =  get_color(lst1[k//3].dicto[lst2[k%3]].dicto["bottom"].color)
            for i in range(top_gap + size_face*2 + size_face//3*(k//3), top_gap + size_face*2 + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face + size_face//3 * (k%3), side_gap + size_face + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # back
        lst=["c2", "e1", "c1", "e3", "ct", "e2", "c4", "e4", "c3"]
        for k in range(9):
            color =  get_color(self.f3.dicto[lst[k]].dicto["back"].color)
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face*3 + size_face//3 * (k%3), side_gap + size_face*3 + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color

        # edges
        for i in range(0, rows):
            for j in range(13):
                arr[i][side_gap + j * size_face//3] = [0]*3
                arr[i][side_gap + j * size_face//3+1] = [0]*3
        for i in range(10):
            for j in range(cols):
                arr[top_gap + i*size_face//3][j]=[0]*3
                arr[top_gap + i*size_face//3+1][j]=[0]*3
        # borders
        try:
            img=cv2.imread("spectrum.png")
            a=min(top_gap, side_gap)//2
            for j in range(cols):
                if j%20==0: b=[randint(0,255), randint(0,255), randint(0,255)]
                for i in range(abs(int(a*numpy.sin(0.01965*j)))):
                    arr[i][j]=img[180][90+j//2]
            for j in range(cols):
                if j%20==0: b=[randint(0,255), randint(0,255), randint(0,255)]
                for i in range(rows-1-abs(int(a*numpy.sin(0.01965*j))), rows):
                    arr[i][j]=img[180][1000-90-j//2]
            for i in range(rows):
                if i%20==0: b=[randint(0,255), randint(0,255), randint(0,255)]
                for j in range(abs(int(a*numpy.sin(0.01965*i+0.6)))):
                    arr[i][j]=img[180][800-90-i//2]
            for i in range(rows):
                if i%20==0: b=[randint(0,255), randint(0,255), randint(0,255)]
                for j in range(cols-1-abs(int(a*numpy.sin(0.01965*i+0.6))), cols):
                    arr[i][j]=img[180][150+i//2]
        except:
            pass
        cv2.imwrite(f"{name}.jpg", arr)
