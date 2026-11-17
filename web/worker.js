// Runs the original Python project with Pyodide, off the page's main thread so the animation never stalls.
importScripts("https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js");

const FILES = ["vpython.py", "rubik_1.py", "rubik_2.py", "rubik_3.py", "web.py"];
let web = null;

const ready = (async () => {
  const py = await loadPyodide();
  const dir = "/home/pyodide/cube";
  py.FS.mkdirTree(dir);
  for (const f of FILES) {
    // py/ holds everything when deployed; in the repo the project files sit one level up, next to web/.
    let r = await fetch("py/" + f, { cache: "no-cache" });
    if (!r.ok && f.startsWith("rubik_")) r = await fetch("../" + f, { cache: "no-cache" });
    if (!r.ok) throw new Error("could not load " + f);
    py.FS.writeFile(dir + "/" + f, await r.text());
  }
  py.runPython(`import sys; sys.path.insert(0, ${JSON.stringify(dir)})`);
  web = py.pyimport("web");
})();

function unpack(res) {
  const [dts, lens, data, net, error] = res.toJs();
  res.destroy();
  // Copy into fresh, 4-byte aligned buffers so they can be viewed as floats/ints and transferred.
  const f32 = (u8) => new Float32Array(u8.slice().buffer);
  const out = { dts: f32(dts), lens: new Int32Array(lens.slice().buffer), data: f32(data), net, error };
  return [out, [out.dts.buffer, out.lens.buffer, out.data.buffer]];
}

self.onmessage = async (e) => {
  const { id, cmd, arg, smoothness, seconds } = e.data;
  try {
    await ready;
    const res = cmd === "new" ? web.new(smoothness, seconds) : web.run(cmd, arg ?? "", smoothness, seconds);
    const [out, transfer] = unpack(res);
    self.postMessage({ id, ok: true, ...out }, transfer);
  } catch (err) {
    self.postMessage({ id, ok: false, error: String(err && err.message ? err.message : err).split("\n").slice(-2).join(" ") });
  }
};
