# -*- coding: utf-8 -*-
'''
Setup file
'''
import os
import setuptools
import subprocess as sp

setup_dir = os.path.dirname(__file__)
with open(os.path.join(setup_dir, 'XSteamPython', '__init__.py'), 'w') as init:
    init.write('from .XSteamPython import *')

with open(os.path.join(setup_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def git_version() -> str:
    """
    Uses `git describe` to determine product version

    Returns:
        str -- version
    """
    cwd = os.path.dirname(os.path.abspath(__file__))
    command = "git describe --tags"
    try:
        return sp.check_output(command.split(), cwd=cwd).decode("utf-8").strip().split("-")[0].split("v")[-1]
    except FileNotFoundError:
        return "X.Y.Z"


setuptools.setup(name='XSteamPython',
    version=git_version(),
    description='Port of XSteam tables by Magnus Holmgren to python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/raldridge11/XSteamPython',
    author='Magnus Holmgren; ported by R. Aldridge',
    packages=setuptools.find_packages(),
    python_requires='>=3.7.*',
    install_requires=['scipy>=1.6.1'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)

os.remove(os.path.join(setup_dir, 'XSteamPython', '__init__.py'))