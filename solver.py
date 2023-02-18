from vpython import *

from methods import methods


class rubiks_cube(methods):
    def solve(self):
        
        def rotate_to_correct_position():
            if self.f1.dicto["ct"].dicto['front'].color==color.white:
                pass
            elif self.f2.dicto["e1"].dicto['top'].color==color.white:
                self.rotate("d")
            elif self.f2.dicto["e2"].dicto['left'].color==color.white:
                self.rotate("r")
            elif self.f2.dicto["e3"].dicto['right'].color==color.white:
                self.rotate("l")
            elif self.f2.dicto["e4"].dicto['bottom'].color==color.white:
                self.rotate("u")
            elif self.f3.dicto["ct"].dicto['back'].color==color.white:
                self.rotate("r")
                self.rotate("r")
            
            while self.f2.dicto["e1"].dicto['top'].color!=color.orange:
                self.rotate("cw")

        def mid_whites():
            def big(f:rubiks_cube.cubies):
                for item in ["front", "back", "top", "bottom", "left", "right"]:
                    f.dicto[item].pos*=1.5
                    f.dicto[item].size*=1.5
            def small(temp_color:vector):
                if temp_color==color.orange: cub = self.f1.dicto["e1"]
                elif temp_color==color.green: cub = self.f1.dicto["e2"]
                elif temp_color==color.blue: cub = self.f1.dicto["e3"]
                elif temp_color==color.red: cub = self.f1.dicto["e4"]
                else: raise Exception
                for item in ["front", "back", "top", "bottom", "left", "right"]:
                    cub.dicto[item].pos/=1.5
                    cub.dicto[item].size/=1.5
            def mid_white_helper(temp_color: vector):
                if temp_color==color.orange:
                    self.move("B_")
                    self.move("B_")
                    self.move("U_")
                    self.move("U_")
                elif temp_color==color.green:
                    self.move("B_")
                    self.move("L_")
                    self.move("L_")
                elif temp_color==color.red:
                    self.move("D")
                    self.move("D")
                elif temp_color==color.blue:
                    self.move("B")
                    self.move("R")
                    self.move("R")

            def mid_white_main(check_face=None):

                if check_face=="front":
                    if self.f1.dicto["e1"].dicto["front"].color==color.white:
                        if self.f1.dicto["e1"].dicto["top"].color!=color.orange:
                            big(self.f1.dicto["e1"])
                            temp_color=self.f1.dicto["e1"].dicto["top"].color
                            self.move("U_")
                            self.move("U_")
                            self.move("B_")
                            self.move("B_")
                            return temp_color
                    if self.f1.dicto["e2"].dicto["front"].color==color.white:
                        if self.f1.dicto["e2"].dicto["left"].color!=color.green:
                            big(self.f1.dicto["e2"])
                            temp_color=self.f1.dicto["e2"].dicto["left"].color
                            self.move("L_")
                            self.move("L_")
                            self.move("B")
                            return temp_color
                    if self.f1.dicto["e3"].dicto["front"].color==color.white:
                        if self.f1.dicto["e3"].dicto["right"].color!=color.blue:
                            big(self.f1.dicto["e3"])
                            temp_color=self.f1.dicto["e3"].dicto["right"].color
                            self.move("R")
                            self.move("R")
                            self.move("B_")
                            return temp_color
                    if self.f1.dicto["e4"].dicto["front"].color==color.white:
                        if self.f1.dicto["e4"].dicto["bottom"].color!=color.red:
                            big(self.f1.dicto["e4"])
                            temp_color=self.f1.dicto["e4"].dicto["bottom"].color
                            self.move("D")
                            self.move("D")
                            return temp_color

                elif check_face=="top":
                    if self.f3.dicto["e1"].dicto["top"].color==color.white:
                        temp_color=self.f3.dicto["e1"].dicto["back"].color
                        big(self.f3.dicto["e1"])
                        self.move("U")
                        self.move("R")
                        self.move("B_")
                        self.move("R_")
                        self.move("U_")
                        return temp_color
                    if self.f2.dicto["c1"].dicto["top"].color==color.white:
                        temp_color=self.f2.dicto["c1"].dicto["left"].color
                        big(self.f2.dicto["c1"])
                        self.move("L_")
                        self.move("B")
                        self.move("L")
                        return temp_color
                    if self.f2.dicto["c2"].dicto["top"].color==color.white:
                        temp_color=self.f2.dicto["c2"].dicto["right"].color
                        big(self.f2.dicto["c2"])
                        self.move("R")
                        self.move("B_")
                        self.move("R_")
                        return temp_color
                    if self.f1.dicto["e1"].dicto["top"].color==color.white:
                        temp_color=self.f1.dicto["e1"].dicto["front"].color
                        big(self.f1.dicto["e1"])
                        self.move("U_")
                        self.move("R")
                        self.move("B_")
                        self.move("R_")
                        return temp_color

                elif check_face=="back":
                    if self.f3.dicto["e1"].dicto["back"].color==color.white:
                        temp_color=self.f3.dicto["e1"].dicto["top"].color
                        big(self.f3.dicto["e1"])
                        self.move("B_")
                        self.move("B_")
                        return temp_color
                    if self.f3.dicto["e3"].dicto["back"].color==color.white:
                        temp_color=self.f3.dicto["e3"].dicto["right"].color
                        big(self.f3.dicto["e3"])
                        self.move("B_")
                        return temp_color
                    if self.f3.dicto["e2"].dicto["back"].color==color.white:
                        temp_color=self.f3.dicto["e2"].dicto["left"].color
                        big(self.f3.dicto["e2"])
                        self.move("B")
                        return temp_color
                    if self.f3.dicto["e4"].dicto["back"].color==color.white:
                        temp_color=self.f3.dicto["e4"].dicto["bottom"].color
                        big(self.f3.dicto["e4"])
                        return temp_color

            def done():
                return self.f1.dicto["e1"].dicto["front"].color==self.f1.dicto["e2"].dicto["front"].color==self.f1.dicto["e3"].dicto["front"].color==self.f1.dicto["e4"].dicto["front"].color==color.white and self.f1.dicto["e1"].dicto["top"].color==color.orange and self.f1.dicto["e2"].dicto["left"].color==color.green and self.f1.dicto["e3"].dicto["right"].color==color.blue and self.f1.dicto["e4"].dicto["bottom"].color==color.red
            while not done():
                # front
                while True:
                    temp_color = mid_white_main("front")
                    if temp_color==None:
                        break
                    mid_white_helper(temp_color)
                    small(temp_color)
                if done(): break
                # top
                while True:
                    temp_color = mid_white_main("top")
                    if temp_color==None:
                        break
                    mid_white_helper(temp_color)
                    small(temp_color)

                if done(): break
                # left            
                while True:
                    self.rotate("cw")
                    temp_color = mid_white_main("top")
                    self.rotate("acw")
                    if temp_color==None:
                        break
                    self.move("B_")
                    mid_white_helper(temp_color)
                    small(temp_color)

                if done(): break
                # right            
                while True:
                    self.rotate("acw")
                    temp_color = mid_white_main("top")
                    self.rotate("cw")
                    if temp_color==None:
                        break
                    self.move("B")
                    mid_white_helper(temp_color)
                    small(temp_color)
                    
                if done(): break
                # bottom
                while True:
                    self.rotate("cw")
                    self.rotate("cw")
                    temp_color = mid_white_main("top")
                    self.rotate("acw")
                    self.rotate("acw")
                    if temp_color==None:
                        break
                    self.move("B_")
                    self.move("B_")
                    mid_white_helper(temp_color)
                    small(temp_color)

                if done(): break
                # back
                while True:
                    temp_color = mid_white_main("back")
                    if temp_color==None:
                        break
                    mid_white_helper(temp_color)
                    small(temp_color)

        def big(f:rubiks_cube.cubies):
            for item in ["front", "back", "top", "bottom", "left", "right"]:
                f.dicto[item].pos*=1.5
                f.dicto[item].size*=1.5
        def small(f:rubiks_cube.cubies):
            for item in ["front", "back", "top", "bottom", "left", "right"]:
                f.dicto[item].pos/=1.5
                f.dicto[item].size/=1.5
        
        def corner_whites():
            def on_front():
                def helper():
                    if self.f1.dicto["c1"].dicto["front"].color==color.white and self.f1.dicto["c1"].dicto["top"].color!=color.orange:
                            big(self.f1.dicto["c1"])
                            self.move("L_")
                            self.move("B_")
                            self.move("L")
                            self.move("B")
                            final_placing(2)
                    elif self.f1.dicto["c2"].dicto["front"].color==color.white and self.f1.dicto["c2"].dicto["top"].color!=color.orange:
                            big(self.f1.dicto["c2"])
                            self.move("R")
                            self.move("B")
                            self.move("R_")
                            self.move("B_")
                            final_placing(1)
                    elif self.f1.dicto["c3"].dicto["front"].color==color.white and self.f1.dicto["c3"].dicto["bottom"].color!=color.red:
                            big(self.f1.dicto["c3"])
                            self.move("L")
                            self.move("B")
                            self.move("L_")
                            self.move("B")
                            final_placing(1)
                    elif self.f1.dicto["c4"].dicto["front"].color==color.white and self.f1.dicto["c4"].dicto["bottom"].color!=color.red:
                            big(self.f1.dicto["c4"])
                            self.move("R_")
                            self.move("B_")
                            self.move("R")
                            self.move("B_")
                            final_placing(2)
                    else:
                        return False

                while True:
                    if helper()==False:
                        break
            def on_back():
                def helper():
                    if self.f3.dicto["c2"].dicto["back"].color==color.white:
                        big(self.f3.dicto["c2"])
                        self.move("R")
                        self.move("B_")
                        self.move("R_")
                        self.move("B_")
                        final_placing(2)
                    elif self.f3.dicto["c1"].dicto["back"].color==color.white:
                        big(self.f3.dicto["c1"])
                        self.move("L_")
                        self.move("B")
                        self.move("L")
                        self.move("B")
                        final_placing(1)
                    elif self.f3.dicto["c4"].dicto["back"].color==color.white:
                        big(self.f3.dicto["c4"])
                        self.move("R_")
                        self.move("B")
                        self.move("R")
                        self.move("B_")
                        final_placing(1)
                    elif self.f3.dicto["c3"].dicto["back"].color==color.white:
                        big(self.f3.dicto["c3"])
                        self.move("L")
                        self.move("B_")
                        self.move("L_")
                        self.move("B")
                        final_placing(2)
                    else: return False

                while True:
                    if helper()==False:
                        break
            def on_sides_up():
                def helper(n:int):
                    if n==1:
                        if self.f1.dicto["c1"].dicto["top"].color==color.white:
                            self.move("L_")
                            self.move("B_")
                            self.move("L")
                            self.move("R")
                            self.move("B_")
                            self.move("R_")
                            self.move("B_")
                        else: raise Exception
                    elif n==2:
                        if self.f1.dicto["c2"].dicto["top"].color==color.white:
                            self.move("R")
                            self.move("B")
                            self.move("R_")
                            self.move("L_")
                            self.move("B")
                            self.move("L")
                            self.move("B")
                        else: raise Exception
                    else: raise Exception
                
                def helper2():
                    if self.f1.dicto["c1"].dicto["top"].color==color.white:
                        big(self.f1.dicto["c1"])
                        helper(1)
                        final_placing(2)
                    elif self.f1.dicto["c2"].dicto["top"].color==color.white:
                        big(self.f1.dicto["c2"])
                        helper(2)
                        final_placing(1)
                    elif self.f1.dicto["c1"].dicto["left"].color==color.white:
                        big(self.f1.dicto["c1"])
                        self.move("F")
                        helper(2)
                        self.move("F_")
                        final_placing(1)
                    elif self.f1.dicto["c2"].dicto["right"].color==color.white:
                        big(self.f1.dicto["c2"])
                        self.move("F_")
                        helper(1)
                        self.move("F")
                        final_placing(2)
                    elif self.f1.dicto["c3"].dicto["bottom"].color==color.white:
                        big(self.f1.dicto["c3"])
                        self.move("F_")
                        self.move("F_")
                        helper(2)
                        self.move("F")
                        self.move("F")
                        final_placing(1)
                    elif self.f1.dicto["c4"].dicto["bottom"].color==color.white:
                        big(self.f1.dicto["c4"])
                        self.move("F_")
                        self.move("F_")
                        helper(1)
                        self.move("F")
                        self.move("F")
                        final_placing(2)
                    elif self.f1.dicto["c3"].dicto["left"].color==color.white:
                        big(self.f1.dicto["c3"])
                        self.move("F")
                        helper(1)
                        self.move("F_")
                        final_placing(2)
                    elif self.f1.dicto["c4"].dicto["right"].color==color.white:
                        big(self.f1.dicto["c4"])
                        self.move("F_")
                        helper(2)
                        self.move("F")
                        final_placing(1)
                    else: return False

                while True:
                    if helper2()==False:
                        break
            def on_sides_down():
                def helper():
                    if self.f3.dicto["c2"].dicto["top"].color==color.white:
                        big(self.f3.dicto["c2"])
                        final_placing(1)
                    elif self.f3.dicto["c2"].dicto["right"].color==color.white:
                        big(self.f3.dicto["c2"])
                        self.move("B")
                        final_placing(2)
                    elif self.f3.dicto["c1"].dicto["top"].color==color.white:
                        big(self.f3.dicto["c1"])
                        final_placing(2)
                    elif self.f3.dicto["c1"].dicto["left"].color==color.white:
                        big(self.f3.dicto["c1"])
                        self.move("B_")
                        final_placing(1)
                    elif self.f3.dicto["c4"].dicto["bottom"].color==color.white:
                        big(self.f3.dicto["c4"])
                        self.move("B")
                        self.move("B")
                        final_placing(2)
                    elif self.f3.dicto["c4"].dicto["right"].color==color.white:
                        big(self.f3.dicto["c4"])
                        self.move("B")
                        final_placing(1)
                    elif self.f3.dicto["c3"].dicto["bottom"].color==color.white:
                        big(self.f3.dicto["c3"])
                        self.move("B")
                        self.move("B")
                        final_placing(1)
                    elif self.f3.dicto["c3"].dicto["left"].color==color.white:
                        big(self.f3.dicto["c3"])
                        self.move("B_")
                        final_placing(2)
                    else: return False

                while True:
                    if helper()==False: break
            
            def final_placing(n:int):
                if n==1:
                    if self.f3.dicto["c2"].dicto["top"].color==color.white:
                        a=self.f3.dicto["c2"]
                        if self.f3.dicto["c2"].dicto["right"].color==color.red:
                            self.move("D")
                            self.move("B_")
                            self.move("D_")
                        elif self.f3.dicto["c2"].dicto["right"].color==color.green:
                            self.move("B_")
                            self.move("L")
                            self.move("B_")
                            self.move("L_")
                        elif self.f3.dicto["c2"].dicto["right"].color==color.orange:
                            self.move("B")
                            self.move("B")
                            self.move("U")
                            self.move("B_")
                            self.move("U_")
                        elif self.f3.dicto["c2"].dicto["right"].color==color.blue:
                            self.move("B")
                            self.move("R")
                            self.move("B_")
                            self.move("R_")
                        else: raise Exception
                        small(a)
                    else:
                        raise Exception
                if n==2:
                    if self.f3.dicto["c1"].dicto["top"].color==color.white:
                        a=self.f3.dicto["c1"]
                        if self.f3.dicto["c1"].dicto["left"].color==color.red:
                            self.move("D_")
                            self.move("B")
                            self.move("D")
                        elif self.f3.dicto["c1"].dicto["left"].color==color.green:
                            self.move("B_")
                            self.move("L_")
                            self.move("B")
                            self.move("L")
                        elif self.f3.dicto["c1"].dicto["left"].color==color.orange:
                            self.move("B_")
                            self.move("B_")
                            self.move("U_")
                            self.move("B")
                            self.move("U")
                        elif self.f3.dicto["c1"].dicto["left"].color==color.blue:
                            self.move("B")
                            self.move("R_")
                            self.move("B")
                            self.move("R")
                        else: raise Exception
                        small(a)
                    else:
                        raise Exception
            
            def done():
                return self.f1.dicto["c1"].dicto["front"].color==self.f1.dicto["c2"].dicto["front"].color==self.f1.dicto["c3"].dicto["front"].color==self.f1.dicto["c4"].dicto["front"].color==color.white and self.f1.dicto["c1"].dicto["top"].color==self.f1.dicto["c2"].dicto["top"].color==color.orange and self.f1.dicto["c3"].dicto["bottom"].color==self.f1.dicto["c4"].dicto["bottom"].color==color.red
            while not done():
                on_front()
                if done(): break
                on_back()
                if done(): break
                on_sides_up()
                if done(): break
                on_sides_down()

        def middle_layer():
            def algo_right():
                self.move("U")
                self.move("R")
                self.move("U_")
                self.move("R_")
                self.move("U_")
                self.move("F_")
                self.move("U")
                self.move("F")
            def algo_left():
                self.move("U_")
                self.move("L_")
                self.move("U")
                self.move("L")
                self.move("U")
                self.move("F")
                self.move("U_")
                self.move("F_")

            self.rotate("d")

            def done():
                return self.f1.dicto["e2"].dicto["front"].color==color.orange and self.f1.dicto["e2"].dicto["left"].color==color.green and self.f1.dicto["e3"].dicto["front"].color==color.orange and self.f1.dicto["e3"].dicto["right"].color==color.blue and self.f3.dicto["e2"].dicto["back"].color==color.red and self.f3.dicto["e3"].dicto["back"].color==color.red and self.f3.dicto["e2"].dicto["left"].color==color.green and self.f3.dicto["e3"].dicto["right"].color==color.blue

            def condition():
                return self.f1.dicto["e1"].dicto["front"].color==color.yellow or self.f1.dicto["e1"].dicto["top"].color==color.yellow
            while not done():
                i=1
                while condition() and i<=4:
                    self.move("U_")
                    i+=1
                if condition():
                    while self.f1.dicto["ct"].dicto["front"].color==self.f1.dicto["e2"].dicto["front"].color and self.f2.dicto["e2"].dicto["left"].color==self.f1.dicto["e2"].dicto["left"].color:
                        self.rotate("l")
                    algo_left()
                    continue
                a=self.f1.dicto["e1"]
                big(self.f1.dicto["e1"])
                if self.f1.dicto["e1"].dicto["front"].color==color.orange:
                    if self.f1.dicto["e1"].dicto["top"].color==color.green:
                        algo_left()
                    elif self.f1.dicto["e1"].dicto["top"].color==color.blue:
                        algo_right()
                    else: raise Exception
                elif self.f1.dicto["e1"].dicto["front"].color==color.green:
                    self.move("U")
                    self.rotate("r")
                    if self.f1.dicto["e1"].dicto["top"].color==color.red:
                        algo_left()
                    elif self.f1.dicto["e1"].dicto["top"].color==color.orange:
                        algo_right()
                    else: raise Exception
                elif self.f1.dicto["e1"].dicto["front"].color==color.blue:
                    self.move("U_")
                    self.rotate("l")
                    if self.f1.dicto["e1"].dicto["top"].color==color.orange:
                        algo_left()
                    elif self.f1.dicto["e1"].dicto["top"].color==color.red:
                        algo_right()
                    else: raise Exception
                elif self.f1.dicto["e1"].dicto["front"].color==color.red:
                    self.move("U_")
                    self.move("U_")
                    self.rotate("r")
                    self.rotate("r")
                    if self.f1.dicto["e1"].dicto["top"].color==color.blue:
                        algo_left()
                    elif self.f1.dicto["e1"].dicto["top"].color==color.green:
                        algo_right()
                    else: raise Exception
                else: raise Exception
                small(a)
                while self.f1.dicto["ct"].dicto["front"].color!=color.orange:
                    self.rotate("r")
        
        def yellow_plus():

            def algo():
                self.move("F")
                self.move("R")
                self.move("U")
                self.move("R_")
                self.move("U_")
                self.move("F_")

            def algo2():
                self.move("R")
                self.move("U")
                self.move("R_")
                self.move("U")
                self.move("R")
                self.move("U")
                self.move("U")
                self.move("R_")
                self.move("U")

            def curr_orient():
                if self.f3.dicto["e1"].dicto["top"].color==color.yellow and self.f2.dicto["c1"].dicto["top"].color==color.yellow and self.f2.dicto["c2"].dicto["top"].color==color.yellow and self.f1.dicto["e1"].dicto["top"].color==color.yellow:
                    return "plus"
                elif self.f3.dicto["e1"].dicto["top"].color!=color.yellow and self.f2.dicto["c1"].dicto["top"].color!=color.yellow and self.f3.dicto["c2"].dicto["top"].color!=color.yellow and self.f1.dicto["e1"].dicto["top"].color!=color.yellow:
                    return "dot"
                else:
                    while self.f1.dicto["e1"].dicto["top"].color==color.yellow:
                        self.move("U")
                    if self.f3.dicto["e1"].dicto["top"].color!=color.yellow:
                        return "danda"
                    else:
                        if self.f2.dicto["c1"].dicto["top"].color!=color.yellow:
                            self.move("U_")
                        return "J"

            while curr_orient()!="plus":
                algo()
            while self.f3.dicto["e1"].dicto["back"].color!=self.f3.dicto["ct"].dicto["back"].color:
                self.move("U")
            if self.f2.dicto["c1"].dicto["left"].color!=self.f2.dicto["e2"].dicto["left"].color:
                if self.f2.dicto["c2"].dicto["right"].color!=self.f2.dicto["e3"].dicto["right"].color:
                    if self.f1.dicto["e1"].dicto["front"].color!=self.f1.dicto["ct"].dicto["front"].color:
                        self.rotate("r")
                        yellow_plus()
                    else:
                        algo2()
                        yellow_plus()
                else:
                    algo2()
                    return
            elif self.f2.dicto["c2"].dicto["right"].color!=self.f2.dicto["e3"].dicto["right"].color:
                self.rotate("l")
                algo2()
                return
            else:
                return
            
        def yellow_corners():
            
            def algo1():
                self.move("U")
                self.move("R")
                self.move("U_")
                self.move("L_")
                self.move("U")
                self.move("R_")
                self.move("U_")
                self.move("L")

            def algo2():
                self.move("R")
                self.move("F_")
                self.move("R_")
                self.move("F")
                self.move("R")
                self.move("F_")
                self.move("R_")
                self.move("F")


            lst=[0,0,0,0]   
            for item in [self.f1.dicto["c1"], self.f1.dicto["c2"], self.f3.dicto["c1"], self.f3.dicto["c2"]]:
                for fc1 in item.dicto:
                    for fc2 in item.dicto:
                        if (item.dicto[fc1].color, item.dicto[fc2].color)==(color.orange, color.green):
                            lst[0]=item
                        elif (item.dicto[fc1].color, item.dicto[fc2].color)==(color.orange, color.blue):
                            lst[1]=item
                        elif (item.dicto[fc1].color, item.dicto[fc2].color)==(color.red, color.green):
                            lst[2]=item
                        elif (item.dicto[fc1].color, item.dicto[fc2].color)==(color.red, color.blue):
                            lst[3]=item
                        else:
                            pass
            def all_correct_pos():
                if self.f1.dicto["c1"] is lst[0] and self.f1.dicto["c2"] is lst[1] and self.f3.dicto["c1"] is lst[2] and self.f3.dicto["c2"] is lst[3]:
                    return True
                return False
            while all_correct_pos()==False:
                if self.f1.dicto["c2"] is lst[1]:
                    algo1()
                elif self.f1.dicto["c1"] is lst[0]:
                    self.rotate("r")
                    algo1()
                    self.rotate("l")
                elif self.f3.dicto["c1"] is lst[2]:
                    self.rotate("r")
                    self.rotate("r")
                    algo1()
                    self.rotate("l")
                    self.rotate("l")
                elif self.f3.dicto["c2"] is lst[3]:
                    self.rotate("l")
                    algo1()
                    self.rotate("r")
                else:
                    algo1()
                    yellow_corners()

            while self.f1.dicto["ct"].dicto["front"].color!=color.orange:
                self.rotate("r")
            def complete():
                return self.f1.dicto["c1"].dicto["top"].color==self.f1.dicto["c2"].dicto["top"].color==self.f3.dicto["c1"].dicto["top"].color==self.f3.dicto["c2"].dicto["top"].color==color.yellow
            while not complete():
                while self.f1.dicto["c2"].dicto["top"].color!=color.yellow:
                    big(self.f1.dicto["c2"])
                    algo2()
                    small(self.f1.dicto["c2"])
                self.move("U_")
            while self.f1.dicto["e1"].dicto["front"].color!=self.f1.dicto["ct"].dicto["front"].color:
                self.move("U_")

        
        rotate_to_correct_position()
        mid_whites()
        corner_whites()
        middle_layer()
        yellow_plus()
        rotate_to_correct_position()
        self.rotate("d")
        yellow_corners()
        rotate_to_correct_position()

