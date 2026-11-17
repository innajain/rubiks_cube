"""A small stand-in for the parts of VPython this project uses (box, vector, color, pi), so the original
rubik_1/2/3.py run unchanged in the browser under Pyodide.

Nothing is drawn here. Every box keeps its position, orientation, size and colour; each call to sleep()
(time.sleep is pointed at _sleep) closes a frame with the boxes that changed since the last one. The page
plays those frames back with three.js, waiting the slept time between them.
"""
import math

pi = math.pi

MAX_FRAMES = 300_000  # guard: a command that runs longer than this is stopped instead of hanging the page


class vector:
    __slots__ = ("x", "y", "z")

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __add__(self, o):
        return vector(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return vector(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, k):
        return vector(self.x * k, self.y * k, self.z * k)

    __rmul__ = __mul__

    def __truediv__(self, k):
        return vector(self.x / k, self.y / k, self.z / k)

    def __neg__(self):
        return vector(-self.x, -self.y, -self.z)

    def __eq__(self, o):
        return isinstance(o, vector) and self.x == o.x and self.y == o.y and self.z == o.z

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"<{self.x:g}, {self.y:g}, {self.z:g}>"

    @property
    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)


def norm(v):
    m = v.mag
    return v / m if m else vector(0, 0, 0)


def mag(v):
    return v.mag


class color:
    white = vector(1, 1, 1)
    black = vector(0, 0, 0)
    red = vector(1, 0, 0)
    green = vector(0, 1, 0)
    blue = vector(0, 0, 1)
    yellow = vector(1, 1, 0)
    orange = vector(1, 0.6, 0)
    cyan = vector(0, 1, 1)
    magenta = vector(1, 0, 1)
    purple = vector(0.4, 0.2, 0.6)

    @staticmethod
    def gray(g):
        return vector(g, g, g)


# --- frame recording ---------------------------------------------------------------------------------

_boxes = []
_dirty = set()
_frames = []  # list of (dt seconds, flat list of 14 floats per changed box)
_count = 0


def _qmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw)


def _qrot(q, v):
    w, x, y, z = q
    # v' = v + 2w(q×v) + 2 q×(q×v)
    cx, cy, cz = y * v.z - z * v.y, z * v.x - x * v.z, x * v.y - y * v.x
    cx2, cy2, cz2 = y * cz - z * cy, z * cx - x * cz, x * cy - y * cx
    return vector(v.x + 2 * (w * cx + cx2), v.y + 2 * (w * cy + cy2), v.z + 2 * (w * cz + cz2))


class box:
    def __init__(self, pos=None, size=None, color=None, **_ignored):
        self._id = len(_boxes)
        _boxes.append(self)
        self._pos = pos if pos is not None else vector(0, 0, 0)
        self._size = size if size is not None else vector(1, 1, 1)
        self._color = color if color is not None else vector(1, 1, 1)
        self._q = (1.0, 0.0, 0.0, 0.0)
        _dirty.add(self._id)

    def _touch(self):
        _dirty.add(self._id)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, v):
        self._pos = v
        self._touch()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, v):
        self._size = v
        self._touch()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, v):
        self._color = v
        self._touch()

    def rotate(self, angle=pi / 4, axis=None, origin=None):
        if axis is None:
            axis = _qrot(self._q, vector(1, 0, 0))
        if origin is None:
            origin = self._pos
        n = norm(axis)
        s = math.sin(angle / 2)
        r = (math.cos(angle / 2), n.x * s, n.y * s, n.z * s)
        self._q = _qmul(r, self._q)
        self._pos = origin + _qrot(r, self._pos - origin)
        self._touch()


def _flush(dt):
    global _count
    data = []
    for i in sorted(_dirty):
        b = _boxes[i]
        p, s, c, q = b._pos, b._size, b._color, b._q
        data += (i, p.x, p.y, p.z, q[0], q[1], q[2], q[3], s.x, s.y, s.z, c.x, c.y, c.z)
    _dirty.clear()
    if data or dt:
        _frames.append((dt, data))
        _count += 1
        if _count > MAX_FRAMES:
            raise RuntimeError("stopped: this took too many steps")


def _sleep(t):
    _flush(float(t))


def _take():
    """Flush what is left and hand over the recorded frames."""
    global _frames, _count
    _flush(0.0)
    out, _frames, _count = _frames, [], 0
    return out


def _clear():
    """Forget every box (the page drops its meshes too)."""
    _boxes.clear()
    _dirty.clear()
    _frames.clear()
