# Natives
import os
from time import time

# Installed
import numpy as np
from PIL import Image

# Custom Modules
from assets.utils import custom_colormap
from MandelBrot.mdb import generate_mandelbrot


class Mandelbrot:
    def __init__(self, mult: int = 5, maxit: int = 250, zoom: int = 1, auto_name: bool = True, silent: bool = False) -> None:
        self.silent = silent
        self.auto_name = auto_name
        h, w = int(410 * mult), int(512 * mult)
        x, y, self.maxit = -0.75, 0, maxit
        x_width, y_height = 1.5, 1.5 * h / w
        x_from, x_to = x - x_width / zoom, x + x_width / zoom
        y_from, y_to = y - y_height / zoom, y + y_height / zoom
        x1, x2, y1, y2 = x_from, x_to, y_from, y_to
        self.xx = np.arange(x1, x2, (x2-x1)/w, dtype=np.float32)
        self.yy = np.arange(y2, y1, (y1-y2)/h, dtype=np.float32)
        print(f"Mandelbrot set init with: H: {h} | W: {w} | IT: {maxit} | Silent Mode: {'ON' if silent else 'OFF'}")
        os.mkdir("out") if not os.path.exists("out") else None
        os.mkdir("out/Mandelbrot") if not os.path.exists("out/Mandelbrot") else None
        self.save_root = "out/Mandelbrot"
        self.filename = f"{self.save_root}/Result_%CMAP% ({h}x{w} & {maxit} IT).png" if auto_name else None

    def _get_file_name(self, fn: str, cmap: str) -> str:
        if self.auto_name:
            return self.filename.replace("%CMAP%", cmap)
        else:
            return f"{self.save_root}/{fn}" if ".png" in fn else f"{self.save_root}/{fn}.png"

    def _applyColorMap(self, data, cmap):
        print(f"\nCreating result image with '{cmap}' CMAP...") if not self.silent else None
        pil_img = Image.fromarray(custom_colormap(cmap, np.uint8(data))) if cmap != "None" else Image.fromarray(np.uint8(data))
        print(f"\nSaving result image with {cmap}...") if not self.silent else None
        return pil_img

    def save(self, cmaps: list, fn: str = "") -> None:
        print("\nCalculating Mandelbrot set values...") if not self.silent else None
        s = time()
        data = generate_mandelbrot(self.xx, self.yy, self.maxit)
        print(f"\nMandelbrot set calculated in {round(time() - s, 3)} sec") if not self.silent else None
        [self._applyColorMap(data, c).save(self._get_file_name(fn, c)) for c in cmaps]
        print(f"\nImage saved: {fn}") if not self.silent else print(f"Image saved: {fn}")
        print(f"\nTotal time needed: {round(time() - s, 3)} sec") if not self.silent else None

    def show(self, cmaps: list) -> None:
        print("\nCalculating Mandelbrot set values...") if not self.silent else None
        s = time()
        data = generate_mandelbrot(self.xx, self.yy, self.maxit)
        print(f"\nMandelbrot set calculated in {round(time() - s, 3)} sec") if not self.silent else None
        [self._applyColorMap(data, c).show() for c in cmaps]
        print(f"\nTotal time needed: {round(time() - s, 3)} sec") if not self.silent else None
