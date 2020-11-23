# Native
import os
from math import *
from cmath import *
from time import time

# Installed
import cv2 as cv

# Custom Modules
from assets.utils import float_range
from JuliaSet.core import JuliaSet


class Animation:
    def __init__(self, range_from: float or int, range_to: float or int, range_step: float, frames_folder: str = "out/JuliaSet/tmp", vid_name: str = "Animation.avi", fps: int = 60) -> None:
        os.mkdir("out/JuliaSet/tmp") if not os.path.exists("out/JuliaSet/tmp") else None
        [os.remove(f"out/JuliaSet/tmp/{x}") for x in os.listdir(frames_folder)] if frames_folder == "out/JuliaSet/tmp" else None
        self.rngf = range_from
        self.rngt = range_to
        self.rngs = range_step
        self.framesfd = frames_folder
        self.fps = fps
        self.vname = vid_name if vid_name.endswith(".mp4") else f"{vid_name}.mp4"
        os.mkdir("out/JuliaSet/Video") if not os.path.exists("out/JuliaSet/Video") else None
        self.save_path = f"out/JuliaSet/Video/{self.vname}"
        (print("This name is already taken... Please find a new one."), quit()) if self.vname in os.listdir("out/JuliaSet/Video") else None

    def animation_from_iamges(self) -> tuple:
        print("Making frames into a video...")
        s = time()
        images = [img for img in os.listdir(self.framesfd) if img.endswith(".png")]
        frame = cv.imread(os.path.join(self.framesfd, images[0]))
        height, width, layers = frame.shape
        video = cv.VideoWriter(self.save_path, 0, self.fps, (width,height))
        [(video.write(cv.imread(os.path.join(self.framesfd, img))), print(f"Current IMG: '{img}'")) for img in images]
        cv.destroyAllWindows()
        video.release()
        print(f"Video finished in {round(time() - s, 3)} sec. Cleaning up tmp files...")
        [os.remove(f"out/JuliaSet/tmp/{x}") for x in os.listdir(self.framesfd)]
        print(f"Cleaning finished. Video saved here: {self.save_path}")
        return self.save_path, round(time() - s, 3)


    def create_animation(self, mult: int, maxit: int, cmap: str, c_func: str) -> tuple:
        inv_step = int(f"1{'0' * (len(str(self.rngs)) - 2)}")
        rng = list(float_range(self.rngf, self.rngt, self.rngs))
        for x in rng:
            c = eval(c_func.replace("X", f"{x}"))
            fn = f"{'0' * (len(str(int(rng[-1]*inv_step))) - len(str(int(x*inv_step))))}{int(x*inv_step)}.png"
            jset = JuliaSet(c, mult, maxit, auto_name=False, for_anim=True, silent=True)
            jset.save(fn=fn, cmaps=[cmap,])
        return self.animation_from_iamges()
