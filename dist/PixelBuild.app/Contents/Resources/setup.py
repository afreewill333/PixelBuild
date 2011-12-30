"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['PixelBuild.py']
DATA_FILES = ['configobj.py',
 'game.bmp',
 'level0000.map',
 'map.py',
 'pygame/',
 'spritesheet.bmp',
 'spritesheet.py']
OPTIONS = {'argv_emulation': False}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
