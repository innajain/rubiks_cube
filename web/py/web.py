"""Glue between the page and the original project: does what the old terminal commander did
(move, rot, scramble, solve), then hands the recorded animation frames back to the page."""
import array
import time

import vpython

time.sleep = vpython._sleep  # before the project imports sleep, so its animation steps become frames

from rubik_3 import rubiks_cube  # noqa: E402  (the project's own code, unchanged)

MOVES = ["U", "U_", "D", "D_", "F", "F_", "B", "B_", "L", "L_", "R", "R_", "M1u", "M1d", "M2r", "M2l", "M3", "M3_"]
ROTATIONS = ["u", "d", "l", "r", "cw", "acw"]
NAMES = {vpython.color.white: "w", vpython.color.yellow: "y", vpython.color.red: "r", vpython.color.orange: "o",
         vpython.color.blue: "b", vpython.color.green: "g", vpython.color.black: "k"}

obj = None


def net():
    """Sticker colours as six 3x3 faces (top, left, front, right, back, bottom), read the same way as show()."""
    o = obj
    front = [o.f1.dicto[k].dicto["front"].color for k in ["c1", "e1", "c2", "e2", "ct", "e3", "c3", "e4", "c4"]]
    top = [[o.f3, o.f2, o.f1][k // 3].dicto[["c1", "e1", "c2"][k % 3]].dicto["top"].color for k in range(9)]
    left = [[o.f3, o.f2, o.f1][k % 3].dicto[["c1", "e2", "c3"][k // 3]].dicto["left"].color for k in range(9)]
    right = [[o.f1, o.f2, o.f3][k % 3].dicto[["c2", "e3", "c4"][k // 3]].dicto["right"].color for k in range(9)]
    bottom = [[o.f1, o.f2, o.f3][k // 3].dicto[["c3", "e4", "c4"][k % 3]].dicto["bottom"].color for k in range(9)]
    back = [o.f3.dicto[k].dicto["back"].color for k in ["c2", "e1", "c1", "e3", "ct", "e2", "c4", "e4", "c3"]]
    return "".join(NAMES.get(c, "k") for face in (top, left, front, right, back, bottom) for c in face)


def pack():
    frames = vpython._take()
    dts = array.array("f", (f[0] for f in frames)).tobytes()
    lens = array.array("i", (len(f[1]) for f in frames)).tobytes()
    data = array.array("f", (x for f in frames for x in f[1])).tobytes()
    return dts, lens, data, net()


def new(smoothness, seconds):
    global obj
    vpython._clear()
    obj = rubiks_cube(smoothness, seconds)
    return pack() + ("",)


def run(cmd, arg, smoothness, seconds):
    obj.smoothness, obj.time = int(smoothness), float(seconds)
    try:
        if cmd == "move" and arg in MOVES:
            obj.move(arg)
        elif cmd == "rot" and arg in ROTATIONS:
            obj.rotate(arg)
        elif cmd == "scramble":
            obj.smoothness, obj.time = max(1, min(obj.smoothness, 6)), min(obj.time, 0.12)
            obj.scramble(20)
        elif cmd == "solve":
            obj.solve()
        else:
            raise ValueError(f"unknown command {cmd} {arg}")
    except Exception as e:  # noqa: BLE001
        # Drop the partial animation and send every box as it now stands, so the page matches Python again.
        vpython._take()
        vpython._dirty.update(range(len(vpython._boxes)))
        return pack() + (f"{type(e).__name__}: {e}",)
    return pack() + ("",)
