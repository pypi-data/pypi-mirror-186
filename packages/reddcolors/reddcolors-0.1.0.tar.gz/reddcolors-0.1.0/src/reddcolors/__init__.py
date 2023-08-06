# @auto-fold regex /^\s*if/ /^\s*else/ /^\s*def/
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as pl

from cycler import Cycler as cyclerobj
from cycler import cycler as cyclerfunc

import functools
from typing import Union

try:
    from jupyterthemes import jtplot
    isjupyterthemes = True
except ModuleNotFoundError:
    print('jupyterthemes missing, Palette set to manual mode\n')
    isjupyterthemes = False

class Palette(object):
    def __init__(self: object):
        self._colormap: str = pl.rcParams['image.cmap']
        self._cycler: cyclerobj = pl.rcParams['axes.prop_cycle']
        self._theme: str = 'default'
        self._auto: bool = isjupyterthemes
        
        self._bg: str = pl.rcParams['axes.facecolor']
        self._fg: str = pl.rcParams['text.color']
        
        self.set_theme()
        cycler0: cyclerobj = pl.rcParams['axes.prop_cycle']
        

        self.cycler_d: dict = dict(retro_metro = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45", "#27aeef", "#b33dc6"],
                                   dutch_field = ["#e60049", "#0bb4ff", "#50e991", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4", "#b3d4ff", "#00bfa0"],
                                   river_nights = ["#b30000", "#7c1158", "#4421af", "#1a53ff", "#0d88e6", "#00b7c7", "#5ad45a", "#8be04e", "#ebdc78"],
                                   spring_pastels = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7"],
                                   default = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
                                   jtplot = [c['color'] for c in cycler0],
                                   )
    
        self.jt_styles: list = ['chesterish', 'grade3', 'gruvboxd', 'gruvboxl', 'monokai', 'oceans16', 'onedork', 'solarizedd', 'solarizedl']
    
    @property
    def cycler_list(self: list) -> list: 
        return [*self.cycler_d]
    
    @property
    def style_list(self: list) -> list:
        return self.jt_styles
    
    @property
    def bg(self: str) -> str:
        return self._bg
    
    @bg.setter
    def bg(self: str, val: str):
        self._bg = val
    
    
    @property
    def fg(self: str) -> str:
        return self._fg
    
    @fg.setter
    def fg(self: str, val: str):
        self._fg = val
        
    @property
    def theme(self: str) -> str:
        return self._theme
    
    @theme.setter
    def theme(self, val:str):
        self._theme = val
    
    def set_theme(self):
        try:
            self.theme = jtplot.infer_theme()
            self._auto = True

            self.bg = pl.rcParams['axes.facecolor']
            self.fg = pl.rcParams['text.color']
            
        except ModuleNotFoundError:
            print('Colour detection failed. jupyterthemes not installed?')
        
    @property
    def colormap(self: str) -> str:
        return self._colormap
    
    @colormap.setter
    def colormap(self: str, val: str):
        self._colormap = val
        pl.rcParams['image.cmap'] = self._colormap
        
    def set_colormap(self, val: str):
        self.colormap = val
    
    @property
    def cycler(self: cyclerobj) -> cyclerobj:
        return self._cycler
    
    @cycler.setter
    def cycler(self: cyclerobj, val: cyclerobj):
        self._cycler = val
        pl.rcParams['axes.prop_cycle'] = self._cycler
        
    def set_cycler(self, val: Union[cyclerobj,str]):
        if type(val) == cyclerobj:
            self.cycler = val
        elif type(val) == str:
            self.cycler = cyclerfunc(color=self.cycler_d[val])
        else:
            print('Cycler not identified!')
            
    def set_style(self, kwargs: dict = None):
        if kwargs is None:
            kwargs = {}
        try:
            jtplot.style(**kwargs)
            self.set_theme()
            self.set_cycler(cyclerfunc(color=jtplot.get_theme_style(jtplot.infer_theme())[1]))
        except ModuleNotFoundError:
            print('Style detection failed. jupyterthemes not installed!')