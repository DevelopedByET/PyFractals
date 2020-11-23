# Natives
import os
from time import time

# Installed
import numpy as np
from PIL import Image

# Custom Modules
from assets.utils import custom_colormap
from JuliaSet.juliasetcython import juliaset_cython


class JuliaSet:
    def __init__(self, c0: int, mult: int = 5, maxit: int = 250, auto_name: bool = True, for_anim: bool = False, silent: bool = False) -> None:
        w, h = int(512 * mult), int(512 * mult)
        self.c = c0
        self.lim = 1000
        self.maxit = maxit
        self.silent = silent
        self.auto_name = auto_name
        self.x = np.linspace(-1.6, 1.6, w)
        self.y = np.linspace(-1.6, 1.6, h)
        os.mkdir("out") if not os.path.exists("out") else None
        os.mkdir("out/JuliaSet") if not os.path.exists("out/JuliaSet") else None
        if not for_anim:
            self.save_root = f"out/JuliaSet/{c0}"
            self.filename = f"{self.save_root}/Result_%CMAP% ({h}x{w} & {maxit} IT).png" if auto_name else None
            os.mkdir(self.save_root) if not os.path.exists(self.save_root) else None
            self.save_root = f"out/JuliaSet/{c0}"
            print(f"JuliaSet init with: H: {h}px | W: {w}px | IT: {maxit} | C: {c0} | Silent Mode: {'ON' if silent else 'OFF'}")
        else:
            self.save_root = "out/JuliaSet/tmp"

    def _get_file_name(self, fn: str, cmap: str) -> str:
        if self.auto_name:
            return self.filename.replace("%CMAP%", cmap)
        else:
            return f"{self.save_root}/{fn}" if fn.endswith(".png") else f"{self.save_root}/{fn}.png"
    
    def _applyColorMap(self, data, cmap):
        print(f"\nCreating result image with '{cmap}' CMAP...") if not self.silent else None
        pil_img = Image.fromarray(custom_colormap(cmap, np.uint8(data)))
        print(f"\nSaving result image with {cmap}...") if not self.silent else None
        return pil_img

    def save(self, cmaps: list, fn: str = "") -> None:
        print(f"Calculating JuliaSet Values...") if not self.silent else None
        s = time()
        data = juliaset_cython(self.x, self.y, self.c, self.lim, self.maxit)
        print(f"\nJuliaSet caculated in: {round(time() - s, 2)} sec") if not self.silent else None
        [self._applyColorMap(data, c).save(self._get_file_name(fn, c)) for c in cmaps]
        print(f"\nImage saved: {fn}") if not self.silent else print(f"Image saved: {fn}")
        print(f"\nTotal time needed: {round(time() - s, 2)} sec") if not self.silent else None

    def show(self, cmaps: list) -> None:
        print(f"Calculating JuliaSet Values...") if not self.silent else None
        s = time()
        data = juliaset_cython(self.x, self.y, self.c, self.lim, self.maxit)
        print(f"\nJuliaSet caculated in: {round(time() - s, 2)} sec") if not self.silent else None
        print("\nCreating result image...") if not self.silent else None
        [self._applyColorMap(data, c).show() for c in cmaps]
        print(f"\nTotal time needed: {round(time() - s, 2)} sec") if not self.silent else None
