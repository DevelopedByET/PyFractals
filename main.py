# Native
import os
import sys
from cmath import *
from math import *

# Custom
from JuliaSet.animation import Animation
from JuliaSet.core import JuliaSet
from MandelBrot.core import Mandelbrot


os.environ['CC'], os.environ['CXX'] = ('gcc-9', 'g++-9') if sys.platform == 'darwin' else ('gcc', 'g++')


class Fractal:
    # All colormaps available
    ALL_CMAPS = [
        'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1',
        'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral',
        'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'
    ]

    # Best looking colormaps for fractals
    BEST_CMAPS_FOR_FRACTALS = [
        'afmhot', 'binary', 'binary_r', 'bone_r', 'cividis', 'CMRmap_r', 'cubehelix', 'gist_heat_r', 'ocean_r', 'RdGy_r', 'RdBu_r'
    ]

    # Some c0 exemple for the JuliaSet
    C0S = [
        1-(1 + sqrt(5))/2,
        -0.4+0.6j,
        0.285+0j,
        0.285+0.01j,
        0.45+0.1428,
        -0.70176-0.3842j,
        -0.835-0.2321j,
        -0.8+0.156j,
        -0.7269+0.1889j,
        -0.8j,
        -0.42+0.6j,
        -0.772691322542185 + 0.124281466072787j,
    ]

    def __init__(self, maximum_iteration: int, cmaps: list, save_res: bool) -> None:
        """
        :param maximum_iteration: Maximum Iterations while creating the fractal
        :param cmaps: List of all the colormaps the create after the set is calculated
        :param save_res: When set to False, it will show the image instead of saving it
        """
        self.maxit = maximum_iteration
        self.cmaps = cmaps
        self.save_res = save_res

    def get_mandelbrot(self, multiplicator: int) -> None:
        """
        Create a image of the Mandelbrot set

        :param multiplicator: Size mutliplicator (base size (multiplicator = 1) is 410x512px)
        """
        mdb = Mandelbrot(mult=multiplicator, maxit=self.maxit)
        mdb.save(cmaps=self.cmaps) if self.save_res else mdb.show(cmaps=self.cmaps)

    def get_julia_set(self, multiplicator: int, c0: complex) -> None:
        """
        Create a image of the JuliaSet

        :param multiplicator: Size mutliplicator (base size (multiplicator = 1) is 512x512px)
        :param c0: Starting complex number for the JuliaSet
        """
        js = JuliaSet(c0, multiplicator, self.maxit)
        js.save(cmaps=self.cmaps) if self.save_res else js.show(cmaps=self.cmaps)


    def get_julia_set_anim(self, c_func: str, cmap: str, _from: int or float, to: int or float, step: float, vid_name: str, fps: int=60) -> None:
        """
        Create a animation of the JuliaSet based of a passed function

        :param c_func: function to calculate for each frame using 'X' as the variable (e.g: "0 + 0.7885 * exp(1j*X)")
        :param cmap: colormap to use for the result images
        :param _from: start of the range for X (e.g: 0)
        :param to: end of the range for X (e.g: 2*pi)
        :param step: step between the values of X in the range (e.g: 0.005)
        :param vid_name: Name of the video at the end
        :param fps: Frames per second of the outputed video
        """
        animator = Animation(_from, to, step, vid_name=vid_name)
        animator.create_animation(self.mult, self.maxit, cmap, c_func)


ftal = Fractal(maximum_iteration=1000, cmaps=["cubehelix", 'gist_heat_r', 'ocean_r', 'RdGy_r'], save_res=True)
ftal.get_julia_set(6, Fractal.C0S[2])
