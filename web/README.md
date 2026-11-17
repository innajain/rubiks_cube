# Web version

Runs `rubik_1.py`, `rubik_2.py` and `rubik_3.py` unchanged in the browser: Python through
[Pyodide](https://pyodide.org) in a web worker, drawing through [three.js](https://threejs.org).

- `py/vpython.py` stands in for the parts of VPython the project uses (`box`, `vector`, `color`, `pi`).
  Nothing is drawn in Python: every `sleep()` in an animation closes a frame of changed boxes, and the
  page plays the frames back.
- `py/web.py` does what `commander()` did in the terminal (moves, `rot`, scramble, solve) and returns the frames.
- `worker.js` loads Pyodide and the Python files; `index.html` has the 3D view, buttons and the unfolded net.

Try it locally from the repository root:

```bash
python3 -m http.server 8000
```

then open http://localhost:8000/web/

To host it, copy `web/` and put `rubik_1.py`, `rubik_2.py` and `rubik_3.py` into its `py/` folder
(the worker looks there first, then one level up). Pyodide and three.js load from the jsdelivr CDN.
