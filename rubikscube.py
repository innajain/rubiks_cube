class cube:
    class face:
        sidelength: int
        data: list

        def __init__(self) -> None:
            self.data=[]
        def setface(self, lst: list) -> None:
            def correctlist(lst: list):
                for item in lst:
                    if item not in ['w', 'y', 'r', 'o', 'b', 'g']:
                        return False
                return True

            if len(lst) == self.sidelength**2 and correctlist(lst):
                self.data = lst.copy()
            else:
                raise Exception("problem with parameter")

        def setitem(self, row: int, col: int, val) -> None:
            if row in range(1,self.sidelength+1) and col in range(1,self.sidelength+1) and val in ['w', 'y', 'r', 'o', 'b', 'g']:
                self.data[(row-1)*self.sidelength+col-1] = val
            else:
                raise Exception("problem with parameters")

        def setrow(self, i: int, lst: list) -> None:
            if len(lst) == self.sidelength and i in range(1,self.sidelength+1):
                n = self.sidelength*(i-1)
                for k in range(self.sidelength):
                    self.data[n+k] = lst[k]
            else:
                raise Exception("problem with parameters")

        def setcolumn(self, i: int, lst: list) -> None:
            if len(lst) == self.sidelength and i in range(1,self.sidelength+1):
                for k in range(self.sidelength):
                    self.data[i-1+k*self.sidelength] = lst[k]
            else:
                raise Exception("problem with parameters")

        def getrow(self, i: int) -> list:
            if i not in range(1,self.sidelength+1):
                raise Exception("problem with parameter")
            lst = [0]*self.sidelength
            n = (i-1)*self.sidelength
            for k in range(self.sidelength):
                lst[k] = self.data[n + k]
            return lst

        def getcolumn(self, i: int) -> list:
            if i not in range(1,self.sidelength+1):
                raise Exception("problem with parameter")
            lst = [0]*self.sidelength
            for k in range(self.sidelength):
                lst[k] = self.data[(i-1) + k*self.sidelength]
            return lst

        def rotate(self, char: str) -> None:
            if char == 'r':
                lst = []
                for k in range(self.sidelength):
                    lst.append((self.getrow(k+1)).copy())
                for k in range(self.sidelength):
                    self.setcolumn(self.sidelength-k, lst[k])
            elif char == 'l':
                lst = []
                for k in range(self.sidelength):
                    lst.append((self.getcolumn(k+1)).copy())
                for k in range(self.sidelength):
                    self.setrow(self.sidelength-k, lst[k])
            else:
                raise Exception("problem with parameter")

        def printface(self) -> None:
            for i in range(self.sidelength):
                n = i*self.sidelength
                for j in range(self.sidelength):
                    print(self.data[n+j], end=" ")
                print()
            print()


    def __init__(self, n: int = 3) -> None:
        self.face.sidelength=n
        self.front=cube.face()
        self.back=cube.face()
        self.top=cube.face()
        self.bottom=cube.face()
        self.left=cube.face()
        self.right=cube.face()
        self.dicto={"w": self.front, "y": self.back, "g": self.left, "b": self.right, "o": self.top, "r": self.bottom}
        self.dict_temp={"front": self.front, "back": self.back, "left": self.left, "right": self.right, "top": self.top, "bottom": self.bottom}

        for item in self.dicto:
            self.dicto[item].setface([item]*self.face.sidelength**2)
        
    def setface(self, char: str, val_list: list) -> None:
        self.dict_temp[char].setface(val_list)

    def printface(self, char: str):
        self.dict_temp[char].printface()
        
    def move(self, char: str, i: int, char2: str) -> None:
        
        def reverse(lst: list) -> list:
            lst.reverse()
            return lst
        if char == "wall":
            if i == 1:
                self.front.rotate(char2)
            elif i == self.face.sidelength:
                if char2 == 'r':
                    self.back.rotate('l')
                elif char2 == 'l':
                    self.back.rotate('r')

            if char2 == 'r':
                a = self.top.getrow(self.face.sidelength-i+1)
                self.top.setrow(self.face.sidelength-i+1, reverse(self.left.getcolumn(self.face.sidelength-i+1)))
                self.left.setcolumn(self.face.sidelength-i+1, self.bottom.getrow(i))
                self.bottom.setrow(i, reverse(self.right.getcolumn(i)))
                self.right.setcolumn(i, a)
            elif char2 == 'l':
                a = self.top.getrow(self.face.sidelength-i+1)
                self.top.setrow(self.face.sidelength-i+1, self.right.getcolumn(i))
                self.right.setcolumn(i, reverse(self.bottom.getrow(i)))
                self.bottom.setrow(i, self.left.getcolumn(self.face.sidelength-i+1))
                self.left.setcolumn(self.face.sidelength-i+1, reverse(a))
        elif char == "horz":
            if i == 1:
                if char2 == 'r':
                    self.top.rotate('l')
                elif char2 == 'l':
                    self.top.rotate('r')
            elif i == self.face.sidelength:
                self.bottom.rotate(char2)

            if char2 == 'r':
                a = self.front.getrow(i)
                self.front.setrow(i, self.left.getrow(i))
                self.left.setrow(i, self.back.getrow(i))
                self.back.setrow(i, self.right.getrow(i))
                self.right.setrow(i, a)
            elif char2 == 'l':
                a = self.front.getrow(i)
                self.front.setrow(i, self.right.getrow(i))
                self.right.setrow(i, self.back.getrow(i))
                self.back.setrow(i, self.left.getrow(i))
                self.left.setrow(i, a)
        elif char == "side":
            if i == 1:
                if char2 == 'u':
                    self.left.rotate('l')
                elif char2 == 'd':
                    self.left.rotate('r')
            elif i == self.face.sidelength:
                if char2 == 'u':
                    self.right.rotate('r')
                elif char2 == 'd':
                    self.right.rotate('l')

            if char2 == 'u':
                a = self.front.getcolumn(i)
                self.front.setcolumn(i, self.bottom.getcolumn(i))
                self.bottom.setcolumn(i, reverse(self.back.getcolumn(self.face.sidelength-i+1)))
                self.back.setcolumn(self.face.sidelength-i+1, reverse(self.top.getcolumn(i)))
                self.top.setcolumn(i, a)
            elif char2 == 'd':
                a = self.front.getcolumn(i)
                self.front.setcolumn(i, self.top.getcolumn(i))
                self.top.setcolumn(i, reverse(self.back.getcolumn(self.face.sidelength-i+1)))
                self.back.setcolumn(self.face.sidelength-i+1, reverse(self.bottom.getcolumn(i)))
                self.bottom.setcolumn(i, a)
        else:
            raise Exception("problem with char")

    def moveS(self, char: str):
        if char == "U":
            self.move("horz", 1, "l")
        elif char == "U_":
            self.move("horz", 1, "r")
        elif char == "B":
            self.move("horz", 3, "r")
        elif char == "B_":
            self.move("horz", 3, "l")
        elif char == "R":
            self.move("side", 3, "u")
        elif char == "R_":
            self.move("side", 3, "d")
        elif char == "L":
            self.move("side", 1, "d")
        elif char == "L_":
            self.move("side", 1, "u")
        else:
            raise Exception("problem with char")

    def rotate_cube(self, char: str):
        if char == "u":
            self.move("side", 1, "u")
            self.move("side", 2, "u")
            self.move("side", 3, "u")
        elif char == "d":
            self.move("side", 1, "d")
            self.move("side", 2, "d")
            self.move("side", 3, "d")
        elif char == "r":
            self.move("horz", 1, "r")
            self.move("horz", 2, "r")
            self.move("horz", 3, "r")
        elif char == "l":
            self.move("horz", 1, "l")
            self.move("horz", 2, "l")
            self.move("horz", 3, "l")
        elif char == "cw":
            self.move("wall", 1, "r")
            self.move("wall", 2, "r")
            self.move("wall", 3, "r")
        elif char == "acw":
            self.move("wall", 1, "l")
            self.move("wall", 2, "l")
            self.move("wall", 3, "l")

    def show(self, name:str = "image"):
        import cv2
        import numpy
        from random import randint

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
        yellow=[0, 180, 245]

        def get_color(char: str):
            if char=='w':
                return white
            elif char=='o':
                return orange
            elif char=='g':
                return green
            elif char=='b':
                return blue
            elif char=='r':
                return red
            elif char=='y':
                return yellow
        
        arr=numpy.array([[[0]*3]*cols]*rows)
        # front
        for k in range(9):
            color =  get_color(self.front.data[k])
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face + size_face//3 * (k%3), side_gap + size_face + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # top
        for k in range(9):
            color =  get_color(self.top.data[k])
            for i in range(top_gap + size_face//3*(k//3), top_gap + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face + size_face//3 * (k%3), side_gap + size_face + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # left
        for k in range(9):
            color =  get_color(self.left.data[k])
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face//3 * (k%3), side_gap + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # right
        for k in range(9):
            color =  get_color(self.right.data[k])
            for i in range(top_gap + size_face + size_face//3*(k//3), top_gap + size_face + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face*2 + size_face//3 * (k%3), side_gap + size_face*2 + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # bottom
        for k in range(9):
            color =  get_color(self.bottom.data[k])
            for i in range(top_gap + size_face*2 + size_face//3*(k//3), top_gap + size_face*2 + size_face//3*(k//3) + size_face//3+1):
                for j in range(side_gap + size_face + size_face//3 * (k%3), side_gap + size_face + size_face//3 * (k%3) + size_face//3+1):
                    arr[i][j]=color
        # back
        for k in range(9):
            color =  get_color(self.back.data[k])
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
        a=min(top_gap, side_gap)//2
        img=cv2.imread("data/spectrum.png")
        try:
            if img.all()!=None:
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
        except: pass
        cv2.imwrite(f"output/{name}.jpg", arr)


    def solve_cube_size3(self):

        def rotate_cube_to_correct_position(obj: cube):
            if 'w' in [obj.front.data[4], obj.left.data[4], obj.right.data[4], obj.back.data[4]]:
                while obj.front.data[4]!='w':
                    obj.rotate_cube("r")
            else:
                while obj.front.data[4]!='w':
                    obj.rotate_cube("u")
            while obj.top.data[4]!='o':
                obj.rotate_cube('cw')

        def making_white_plus(obj: cube) -> None:
            def move(pos1:tuple, pos2:tuple):
                pass
            def color_int(char:str) -> int:
                lst=['o', 'g', 'b', 'r']
                for i in range(4):
                    if lst[i]==char:
                        break
                else:
                    return 2*i+1
            def opposite(pos:tuple) -> str:
                if pos[0]=="front":
                    if pos[1]==1:
                        return ("top", 7)
                    elif pos[1]==3:
                        return ("left", 5)
                    elif pos[1]==5:
                        return ("right", 3)
                    elif pos[1]==7:
                        return ("bottom", 1)
                if pos[0]=="top":
                    if pos[1]==1:
                        return ("back", 1)
                    elif pos[1]==3:
                        return ("left", 1)
                    elif pos[1]==5:
                        return ("right", 1)
                    elif pos[1]==7:
                        return ("front", 1)
                if pos[0]=="bottom":
                    if pos[1]==1:
                        return ("front", 7)
                    elif pos[1]==3:
                        return ("left", 7)
                    elif pos[1]==5:
                        return ("right", 7)
                    elif pos[1]==7:
                        return ("back", 7)
                if pos[0]=="left":
                    if pos[1]==1:
                        return ("top", 3)
                    elif pos[1]==3:
                        return ("back", 5)
                    elif pos[1]==5:
                        return ("front", 3)
                    elif pos[1]==7:
                        return ("bottom", 3)
                if pos[0]=="right":
                    if pos[1]==1:
                        return ("top", 5)
                    elif pos[1]==3:
                        return ("front", 5)
                    elif pos[1]==5:
                        return ("back", 3)
                    elif pos[1]==7:
                        return ("bottom", 5)
                if pos[0]=="BACK":
                    if pos[1]==1:
                        return ("top", 1)
                    elif pos[1]==3:
                        return ("right", 5)
                    elif pos[1]==5:
                        return ("left", 3)
                    elif pos[1]==7:
                        return ("bottom", 7)
                    
            def find_and_correct_mid_white(obj: cube, face: str):
                for item in ["front", "top", "left", "right", "bottom", "back"]:
                    for i in range(4):
                        if obj.get_face(item).data[2*i+1]=='w':
                            move((item, 2*i+1), ("front", color_int(opposite(item, 2*i+1))))




                if face == 'front':

                    if obj.front.data[1] == 'w':
                        if obj.top.data[7] == 'b':
                            pass
                        else:
                            obj.move('horz', 1, 'r')
                            obj.move('horz', 1, 'r')

                            if obj.top.data[1] == 'r':
                                obj.move('wall', 3, 'r')
                                obj.move('side', 3, 'u')
                                obj.move('side', 3, 'u')
                            elif obj.top.data[1] == 'g':
                                obj.move('wall', 3, 'r')
                                obj.move('wall', 3, 'r')
                                obj.move('horz', 3, 'r')
                                obj.move('horz', 3, 'r')
                            elif obj.top.data[1] == 'o':
                                obj.move('wall', 3, 'l')
                                obj.move('side', 1, 'u')
                                obj.move('side', 1, 'u')
                            return

                    if obj.front.data[3] == 'w':
                        if obj.left.data[5] == 'o':
                            pass
                        else:
                            obj.move('side', 1, 'u')
                            obj.move('side', 1, 'u')

                            if obj.top.data[3] == 'b':
                                obj.move('wall', 3, 'r')
                                obj.move('side', 3, 'u')
                                obj.move('side', 3, 'u')
                            elif obj.top.data[3] == 'r':
                                obj.move('wall', 3, 'r')
                                obj.move('wall', 3, 'r')
                                obj.move('horz', 3, 'r')
                                obj.move('horz', 3, 'r')
                            elif obj.top.data[3] == 'g':
                                obj.move('wall', 3, 'l')
                                obj.move('side', 1, 'u')
                                obj.move('side', 1, 'u')
                            return

                    if obj.front.data[5] == 'w':
                        if obj.right.data[3] == 'r':
                            pass
                        else:
                            obj.move('side', 3, 'u')
                            obj.move('side', 3, 'u')

                            if obj.right.data[5] == 'g':
                                obj.move('wall', 3, 'r')
                                obj.move('side', 3, 'u')
                                obj.move('side', 3, 'u')
                            elif obj.right.data[5] == 'o':
                                obj.move('wall', 3, 'r')
                                obj.move('wall', 3, 'r')
                                obj.move('horz', 3, 'r')
                                obj.move('horz', 3, 'r')
                            elif obj.right.data[5] == 'b':
                                obj.move('wall', 3, 'l')
                                obj.move('side', 1, 'u')
                                obj.move('side', 1, 'u')
                            return

                    if obj.front.data[7] == 'w':
                        if obj.bottom.data[1] == 'g':
                            pass
                        else:
                            obj.move('horz', 3, 'r')
                            obj.move('horz', 3, 'r')

                            if obj.bottom.data[7] == 'o':
                                obj.move('wall', 3, 'r')
                                obj.move('side', 3, 'u')
                                obj.move('side', 3, 'u')
                            elif obj.bottom.data[7] == 'b':
                                obj.move('wall', 3, 'r')
                                obj.move('wall', 3, 'r')
                                obj.move('horz', 3, 'r')
                                obj.move('horz', 3, 'r')
                            elif obj.bottom.data[7] == 'r':
                                obj.move('wall', 3, 'l')
                                obj.move('side', 1, 'u')
                                obj.move('side', 1, 'u')
                            return
                    return True

                elif face == 'back':

                    if obj.back.data[1] == 'w':
                        if obj.top.data[1] == 'b':
                            obj.move('horz', 1, 'r')
                            obj.move('horz', 1, 'r')
                        elif obj.top.data[1] == 'r':
                            obj.move('wall', 3, 'r')
                            obj.move('side', 3, 'u')
                            obj.move('side', 3, 'u')
                        elif obj.top.data[1] == 'g':
                            obj.move('wall', 3, 'r')
                            obj.move('wall', 3, 'r')
                            obj.move('horz', 3, 'r')
                            obj.move('horz', 3, 'r')
                        elif obj.top.data[1] == 'o':
                            obj.move('wall', 3, 'l')
                            obj.move('side', 1, 'u')
                            obj.move('side', 1, 'u')
                        return
                    if obj.back.data[3] == 'w':
                        if obj.right.data[5] == 'b':
                            obj.move('wall', 3, 'l')
                            obj.move('horz', 1, 'r')
                            obj.move('horz', 1, 'r')
                        elif obj.right.data[5] == 'r':
                            obj.move('side', 3, 'u')
                            obj.move('side', 3, 'u')
                        elif obj.right.data[5] == 'g':
                            obj.move('wall', 3, 'r')
                            obj.move('horz', 3, 'r')
                            obj.move('horz', 3, 'r')
                        elif obj.right.data[5] == 'o':
                            obj.move('wall', 3, 'r')
                            obj.move('wall', 3, 'r')
                            obj.move('side', 1, 'u')
                            obj.move('side', 1, 'u')
                        return
                    if obj.back.data[5] == 'w':
                        if obj.left.data[3] == 'b':
                            obj.move('wall', 3, 'r')
                            obj.move('horz', 1, 'r')
                            obj.move('horz', 1, 'r')
                        elif obj.left.data[3] == 'r':
                            obj.move('wall', 3, 'r')
                            obj.move('wall', 3, 'r')
                            obj.move('side', 3, 'u')
                            obj.move('side', 3, 'u')
                        elif obj.left.data[3] == 'g':
                            obj.move('wall', 3, 'l')
                            obj.move('horz', 3, 'r')
                            obj.move('horz', 3, 'r')
                        elif obj.left.data[3] == 'o':
                            obj.move('side', 1, 'u')
                            obj.move('side', 1, 'u')
                        return
                    if obj.back.data[7] == 'w':
                        if obj.bottom.data[7] == 'b':
                            obj.move('wall', 3, 'r')
                            obj.move('wall', 3, 'r')
                            obj.move('horz', 1, 'r')
                            obj.move('horz', 1, 'r')
                        elif obj.bottom.data[7] == 'r':
                            obj.move('wall', 3, 'l')
                            obj.move('side', 3, 'u')
                            obj.move('side', 3, 'u')
                        elif obj.bottom.data[7] == 'g':
                            obj.move('horz', 3, 'r')
                            obj.move('horz', 3, 'r')
                        elif obj.bottom.data[7] == 'o':
                            obj.move('wall', 3, 'r')
                            obj.move('side', 1, 'u')
                            obj.move('side', 1, 'u')
                        return
                    return True

                elif face == 'top':

                    if obj.top.data[1] == 'w':
                        obj.move('horz', 1, 'l')
                        obj.move('side', 3, 'u')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 3, 'd')
                        obj.move('horz', 1, 'r')
                        obj.move('wall', 3, 'l')
                        obj.move('wall', 3, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.top.data[3] == 'w':
                        obj.move('side', 1, 'u')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 1, 'd')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.top.data[5] == 'w':
                        obj.move('side', 3, 'u')
                        obj.move('wall', 3, 'l')
                        obj.move('side', 3, 'd')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.top.data[7] == 'w':
                        obj.move('horz', 1, 'r')
                        obj.move('side', 3, 'u')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 3, 'd')
                        obj.move('horz', 1, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('wall', 3, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    return True

                elif face == 'right':

                    if obj.right.data[1] == 'w':
                        obj.move('horz', 1, 'r')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 1, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.right.data[3] == 'w':
                        obj.move('side', 3, 'd')
                        obj.move('horz', 3, 'r')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 3, 'l')
                        obj.move('side', 3, 'u')
                        obj.move('wall', 3, 'r')
                        obj.move('wall', 3, 'r')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.right.data[5] == 'w':
                        obj.move('side', 3, 'u')
                        obj.move('horz', 3, 'r')
                        obj.move('side', 3, 'd')
                        obj.move('horz', 3, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.right.data[7] == 'w':
                        obj.move('horz', 3, 'r')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 3, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    return True

                elif face == 'left':

                    if obj.left.data[1] == 'w':
                        obj.move('horz', 1, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 1, 'r')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.left.data[3] == 'w':
                        obj.move('side', 1, 'u')
                        obj.move('horz', 3, 'l')
                        obj.move('side', 1, 'd')
                        obj.move('wall', 3, 'r')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.left.data[5] == 'w':
                        obj.move('side', 1, 'd')
                        obj.move('horz', 3, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 3, 'r')
                        obj.move('side', 3, 'u')
                        obj.move('wall', 3, 'r')
                        obj.move('wall', 3, 'r')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.left.data[7] == 'w':
                        obj.move('horz', 3, 'l')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 3, 'r')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    return True

                elif face == 'bottom':

                    if obj.bottom.data[1] == 'w':
                        obj.move('horz', 3, 'l')
                        obj.move('side', 1, 'd')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 1, 'u')
                        obj.move('horz', 1, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('wall', 3, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.bottom.data[3] == 'w':
                        obj.move('side', 1, 'd')
                        obj.move('wall', 3, 'l')
                        obj.move('side', 1, 'u')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.bottom.data[5] == 'w':
                        obj.move('side', 3, 'd')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 3, 'u')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    if obj.bottom.data[7] == 'w':
                        obj.move('horz', 1, 'l')
                        obj.move('side', 3, 'd')
                        obj.move('wall', 3, 'l')
                        obj.move('side', 3, 'u')
                        obj.move('horz', 1, 'r')
                        obj.move('wall', 3, 'l')
                        obj.move('wall', 3, 'l')
                        find_and_correct_mid_white(obj, 'back')
                        return
                    return True

            for item in ['front', 'back', 'top', 'right', 'left', 'bottom']:
                while True:
                    if find_and_correct_mid_white(obj, item) == True:
                        break

        def corners(obj: cube):
            def helper_lateral(obj: cube):
                if obj.top.data[0] == 'w':
                    if obj.left.data[0] == 'o':
                        obj.move('wall', 3, 'r')
                        obj.move('side', 1, 'u')
                        obj.move('wall', 3, 'l')
                        obj.move('side', 1, 'd')
                    elif obj.left.data[0] == 'b':
                        obj.move('wall', 3, 'r')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 1, 'r')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 1, 'l')
                    elif obj.left.data[0] == 'r':
                        obj.move('wall', 3, 'l')
                        obj.move('side', 3, 'd')
                        obj.move('wall', 3, 'l')
                        obj.move('side', 3, 'u')
                    elif obj.left.data[0] == 'g':
                        obj.move('horz', 3, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 3, 'r')
                # if obj.left.data[6] == 'w':
                #     if obj.bottom.data[6] == 'g':
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 3, 'l')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 3, 'r')
                #     elif obj.bottom.data[6] == 'o':
                #         obj.move('wall', 3, 'r')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 1, 'u')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 1, 'd')
                #     elif obj.bottom.data[6] == 'b':
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 1, 'r')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 1, 'l')
                #     elif obj.bottom.data[6] == 'r':
                #         obj.move('side', 3, 'd')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 3, 'u')
                # if obj.bottom.data[8] == 'w':
                #     if obj.right.data[8] == 'r':
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 3, 'd')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 3, 'u')
                #     elif obj.right.data[8] == 'g':
                #         obj.move('wall', 3, 'r')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 3, 'l')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 3, 'r')
                #     elif obj.right.data[8] == 'o':
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 1, 'u')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 1, 'd')
                #     elif obj.right.data[8] == 'b':
                #         obj.move('horz', 1, 'r')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 1, 'l')
                # if obj.right.data[2] == 'w':
                #     if obj.top.data[2] == 'b':
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 1, 'r')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 1, 'l')
                #     elif obj.top.data[2] == 'r':
                #         obj.move('wall', 3, 'r')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 3, 'd')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 3, 'u')
                #     elif obj.top.data[2] == 'g':
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 3, 'l')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 3, 'r')
                #     elif obj.top.data[2] == 'o':
                #         obj.move('side', 1, 'u')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 1, 'd')
                elif obj.top.data[2] == 'w':
                    if obj.right.data[2] == 'o':
                        obj.move('wall', 3, 'l')
                        obj.move('side', 1, 'd')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 1, 'u')
                    elif obj.right.data[2] == 'b':
                        obj.move('wall', 3, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 1, 'l')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 1, 'r')
                    elif obj.right.data[2] == 'r':
                        obj.move('wall', 3, 'l')
                        obj.move('side', 3, 'u')
                        obj.move('wall', 3, 'r')
                        obj.move('side', 3, 'd')
                    elif obj.right.data[2] == 'g':
                        obj.move('horz', 3, 'r')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 3, 'l')
                # if obj.right.data[8] == 'w':
                #     if obj.bottom.data[8] == 'g':
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 3, 'r')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 3, 'l')
                #     elif obj.bottom.data[8] == 'o':
                #         obj.move('side', 1, 'd')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 1, 'u')
                #     elif obj.bottom.data[8] == 'b':
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 1, 'l')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 1, 'r')
                #     elif obj.bottom.data[8] == 'r':
                #         obj.move('wall', 3, 'l')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 3, 'u')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 3, 'd')
                # if obj.bottom.data[6] == 'w':
                #     if obj.left.data[6] == 'r':
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 3, 'u')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 3, 'd')
                #     elif obj.left.data[6] == 'g':
                #         obj.move('wall', 3, 'l')
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 3, 'r')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 3, 'l')
                #     elif obj.left.data[6] == 'o':
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 1, 'd')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 1, 'u')
                #     elif obj.left.data[6] == 'b':
                #         obj.move('horz', 1, 'l')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 1, 'r')
                # if obj.left.data[0] == 'w':
                #     if obj.top.data[0] == 'b':
                #         obj.move('wall', 3, 'l')
                #         obj.move('horz', 1, 'l')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 1, 'r')
                #     elif obj.top.data[0] == 'r':
                #         obj.move('side', 3, 'u')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 3, 'd')
                #     elif obj.top.data[0] == 'g':
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 3, 'r')
                #         obj.move('wall', 3, 'r')
                #         obj.move('horz', 3, 'l')
                #     elif obj.top.data[0] == 'o':
                #         obj.move('wall', 3, 'l')
                #         obj.move('wall', 3, 'l')
                #         obj.move('side', 1, 'd')
                #         obj.move('wall', 3, 'r')
                #         obj.move('side', 1, 'u')
                else: return True
            def helper_back(obj: cube):
                if obj.back.data[0] == 'w':
                    if obj.front.data[2] == 'w':
                        obj.move('wall', 3, 'r')
                    else:
                        obj.move('horz', 1, 'r')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 1, 'l')
                    corners(obj)
                elif obj.back.data[2] == 'w':
                    if obj.front.data[0] == 'w':
                        obj.move('wall', 3, 'r')
                    else:
                        obj.move('horz', 1, 'l')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 1, 'r')
                    corners(obj)
                elif obj.back.data[6] == 'w':
                    if obj.front.data[8] == 'w':
                        obj.move('wall', 3, 'r')
                    else:
                        obj.move('horz', 3, 'r')
                        obj.move('wall', 3, 'r')
                        obj.move('horz', 3, 'l')
                    corners(obj)
                elif obj.back.data[8] == 'w':
                    if obj.front.data[6] == 'w':
                        obj.move('wall', 3, 'r')
                    else:
                        obj.move('horz', 3, 'l')
                        obj.move('wall', 3, 'l')
                        obj.move('horz', 3, 'r')
                    corners(obj)
                elif (obj.top.data[6] == 'w' or obj.left.data[2] == 'w' or (obj.front.data[0] == 'w' and (obj.top.data[6] != 'b' or obj.left.data[2] != 'o'))) == True:
                    obj.move("horz", 1, 'l')
                    obj.move("wall", 3, 'l')
                    obj.move("horz", 1, 'r')
                elif (obj.top.data[8] == 'w' or obj.right.data[0] == 'w' or (obj.front.data[2] == 'w' and (obj.top.data[8] != 'b' or obj.right.data[0] != 'r'))) == True:
                    obj.move("horz", 1, 'r')
                    obj.move("wall", 3, 'r')
                    obj.move("horz", 1, 'l')
                elif (obj.bottom.data[0] == 'w' or obj.left.data[8] == 'w' or (obj.front.data[6] == 'w' and (obj.bottom.data[0] != 'g' or obj.left.data[8] != 'o'))) == True:
                    obj.move("horz", 3, 'l')
                    obj.move("wall", 3, 'r')
                    obj.move("horz", 3, 'r')
                elif (obj.bottom.data[2] == 'w' or obj.right.data[6] == 'w' or (obj.front.data[8] == 'w' and (obj.bottom.data[2] != 'g' or obj.right.data[6] != 'r'))) == True:
                    obj.move("horz", 3, 'r')
                    obj.move("wall", 3, 'l')
                    obj.move("horz", 3, 'l')
                else:
                    return True
            for _ in range(4):
                helper_lateral(obj)
                obj.move("wall", 3, )

        def mids(obj: cube) -> None:
            def helper(obj: cube):
                if obj.top.data[1] != 'y' and obj.back.data[1] != 'y':
                    if obj.top.data[1] == 'b':
                        if obj.back.data[1] == 'o':
                            obj.move("wall", 3, 'r')
                            obj.move("side", 1, 'u')
                            obj.move("wall", 3, 'r')
                            obj.move("side", 1, 'd')
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 1, 'l')
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 1, 'r')
                        elif obj.back.data[1] == 'r':
                            obj.move("wall", 3, 'l')
                            obj.move("side", 3, 'u')
                            obj.move("wall", 3, 'l')
                            obj.move("side", 3, 'd')
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 1, 'r')
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 1, 'l')
                    else:
                        obj.move("wall", 3, 'r')
                        mids(obj)
                elif obj.left.data[3] != 'y' and obj.back.data[5] != 'y':
                    if obj.left.data[3] == 'o':
                        if obj.back.data[5] == 'g':
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 3, 'l')
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 3, 'r')
                            obj.move("wall", 3, 'l')
                            obj.move("side", 1, 'd')
                            obj.move("wall", 3, 'l')
                            obj.move("side", 1, 'u')
                        elif obj.back.data[5] == 'b':
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 1, 'l')
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 1, 'r')
                            obj.move("wall", 3, 'r')
                            obj.move("side", 1, 'u')
                            obj.move("wall", 3, 'r')
                            obj.move("side", 1, 'd')
                    else:
                        obj.move("wall", 3, 'r')
                        mids(obj)
                elif obj.right.data[5] != 'y' and obj.back.data[3] != 'y':
                    if obj.right.data[5] == 'r':
                        if obj.back.data[3] == 'b':
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 1, 'r')
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 1, 'l')
                            obj.move("wall", 3, 'l')
                            obj.move("side", 3, 'u')
                            obj.move("wall", 3, 'l')
                            obj.move("side", 3, 'd')
                        elif obj.back.data[3] == 'g':
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 3, 'r')
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 3, 'l')
                            obj.move("wall", 3, 'r')
                            obj.move("side", 3, 'd')
                            obj.move("wall", 3, 'r')
                            obj.move("side", 3, 'u')

                    else:
                        obj.move("wall", 3, 'r')
                        mids(obj)
                elif obj.bottom.data[7] != 'y' and obj.back.data[7] != 'y':
                    if obj.bottom.data[7] == 'b':
                        if obj.back.data[7] == 'r':
                            obj.move("wall", 3, 'r')
                            obj.move("side", 3, 'd')
                            obj.move("wall", 3, 'r')
                            obj.move("side", 3, 'u')
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 3, 'r')
                            obj.move("wall", 3, 'l')
                            obj.move("horz", 3, 'l')
                        elif obj.back.data[1] == 'o':
                            obj.move("wall", 3, 'l')
                            obj.move("side", 1, 'd')
                            obj.move("wall", 3, 'l')
                            obj.move("side", 1, 'u')
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 3, 'l')
                            obj.move("wall", 3, 'r')
                            obj.move("horz", 3, 'r')
                    else:
                        obj.move("wall", 3, 'r')
                        mids(obj)
                else:
                    if obj.front.data == ['w']*9:
                        if obj.top.getrow(2) == obj.top.getrow(3) == ['b']*3:
                            if obj.left.getcolumn(2) == obj.left.getcolumn(3) == ['o']*3:
                                if obj.right.getcolumn(1) == obj.right.getcolumn(2) == ['r']*3:
                                    if obj.bottom.getrow(1) == obj.bottom.getrow(2) == ['g']*3:
                                        return True
                                    else:
                                        raise Exception
            while helper(obj) != True:
                pass

        rotate_cube_to_correct_position(self)
        making_white_plus(self)
        corners(self)
        mids(self)


    def solve(self):
        # 1. rotate cube to correct orientation
        # 2. on the front face search for edgewhites
        # 3. move them to back and then rotate back wall to correctly orient them and move it to front
        # 4. repeat it for other faces

        def rotate_to_correct_orientation():
            count=0
            while self.front.data[4]!='w' and count<4:
                self.rotate_cube("r")
                count+=1
            if self.front.data[4]!='w':
                while self.front.data[4]!='w':
                    self.rotate_cube("d")
        def opposite(face, i):
            pass
        def move_edge(obj: cube):
            def move_to_back():
                pass
            def orient():
                pass
            def move_to_front():
                pass
        def face_int(face: str):
            if face=="top":
                return 1
            elif face=="left":
                return 3
            elif face=="right":
                return 5
            elif face=="bottom":
                return 7
            else:
                raise Exception
        def search_for_edgewhites(face: str):
            for i in [1,3,5,7]:
                if self.get_face(face).data[i]=='w':
                    opp=opposite(face, i)
                    opp_color=self.get_face(opp[0]).data[opp[1]]
                    if opp_color!=self.get_face(opp[0]).data[4]:
                        move_edge((face, i), ("front", face_int(self.face_color(opp_color))))

    def yellow_plus(self) -> None:
        def random_plus(obj: cube) -> None:
            if obj.back.data[1] != 'y' and obj.back.data[3] == 'y' and obj.back.data[5] == 'y' and obj.back.data[7] != 'y':
                obj.move('horz', 1, 'l')
                obj.move('side', 3, 'u')
                obj.move('wall', 3, 'l')
                obj.move('side', 3, 'd')
                obj.move('wall', 3, 'r')
                obj.move('horz', 1, 'r')
            elif obj.back.data[1] == 'y' and obj.back.data[3] != 'y' and obj.back.data[5] != 'y' and obj.back.data[7] == 'y':
                obj.move('side', 3, 'u')
                obj.move('horz', 3, 'r')
                obj.move('wall', 3, 'l')
                obj.move('horz', 3, 'l')
                obj.move('wall', 3, 'r')
                obj.move('side', 3, 'd')
            elif obj.back.data[1] == 'y' and obj.back.data[3] == 'y' and obj.back.data[5] != 'y' and obj.back.data[7] != 'y':
                obj.move('horz', 1, 'l')
                obj.move('side', 3, 'u')
                obj.move('wall', 3, 'l')
                obj.move('side', 3, 'd')
                obj.move('wall', 3, 'r')
                obj.move('horz', 1, 'r')
                random_plus(obj)
            elif obj.back.data[1] == 'y' and obj.back.data[3] != 'y' and obj.back.data[5] == 'y' and obj.back.data[7] != 'y':
                obj.move("wall", 3, 'r')
                random_plus(obj)
            elif obj.back.data[1] != 'y' and obj.back.data[3] != 'y' and obj.back.data[5] == 'y' and obj.back.data[7] == 'y':
                obj.move("wall", 3, 'r')
                obj.move("wall", 3, 'r')
                random_plus(obj)
            elif obj.back.data[1] != 'y' and obj.back.data[3] == 'y' and obj.back.data[5] != 'y' and obj.back.data[7] == 'y':
                obj.move('side', 3, 'u')
                obj.move('horz', 3, 'r')
                obj.move('wall', 3, 'l')
                obj.move('horz', 3, 'l')
                obj.move('wall', 3, 'r')
                obj.move('side', 3, 'd')
                random_plus(obj)
            elif obj.back.data[1] == 'y' and obj.back.data[3] == 'y' and obj.back.data[5] == 'y' and obj.back.data[7] == 'y':
                return
            else:
                raise Exception

        def correcting(obj: cube) -> None:

            def algo_b(obj: cube) -> None:
                obj.move('side', 3, 'u')
                obj.move('wall', 3, 'l')
                obj.move('side', 3, 'd')
                obj.move('wall', 3, 'l')
                obj.move('side', 3, 'u')
                obj.move('wall', 3, 'r')
                obj.move('wall', 3, 'r')
                obj.move('side', 3, 'd')

            def algo_o(obj: cube) -> None:
                obj.move("wall", 3, 'r')
                obj.move("horz", 1, 'l')
                obj.move("wall", 3, 'l')
                obj.move("horz", 1, 'r')
                obj.move("wall", 3, 'l')
                obj.move("horz", 1, 'l')
                obj.move("wall", 3, 'r')
                obj.move("wall", 3, 'r')
                obj.move("horz", 1, 'r')
            while obj.top.data[1] != 'b':
                obj.move('wall', 3, 'r')

            if obj.bottom.data[7] == 'g':
                if obj.right.data[5] == 'r':
                    return
                else:
                    algo_b(obj)
                    if obj.left.data[3] == 'g':
                        obj.move("wall", 3, 'r')
                        algo_o(obj)
                        if obj.top.data[1] != 'b':
                            algo_o(obj)
                        else:
                            print("here")
                            return
                    else:
                        return
            else:
                if obj.left.data[3] != 'o' and obj.right.data[5] != 'r':
                    algo_b(obj)
                    if obj.left.data[3] != 'o' or obj.right.data[5] != 'r' or obj.bottom.data[7] != 'g':
                        algo_b(obj)
                    else:
                        return
                else:
                    algo_b(obj)
                    correcting(obj)

        random_plus(self)
        correcting(self)
