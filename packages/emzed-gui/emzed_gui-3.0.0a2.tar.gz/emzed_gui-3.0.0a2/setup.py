# This file is part of emzed (https://emzed.ethz.ch), a software toolbox for analysing
# LCMS data with Python.
#
# Copyright (C) 2020 ETH Zurich, SIS ID.
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.


import os
import sys
from distutils.command.build_ext import build_ext as _build_ext

from setuptools import Extension, find_packages, setup



install_requires = (
    "emzed>=3.0.0a1",
    "PyQt5==5.15.7",
    "guidata==1.7.7",
    "pythonqwt==0.5.5",
    "guiqwt==3.0.3",
    "matplotlib==3.3.0" if sys.platform == "win32" else "matplotlib",
    "numpy",
)


class build_ext(_build_ext):
    """only require numpy when we build binary extension"""

    def run(self):
        # https://stackoverflow.com/questions/21605927/
        __builtins__.__NUMPY_SETUP__ = False
        import numpy

        self.include_dirs += [numpy.get_include()]
        _build_ext.run(self)


ext_modules = [
    Extension(
        "emzed_gui.optimized.optimized",
        [os.path.join("src", "emzed_gui", "optimized", "optimized.c")],
    )
]

setup(
    name="emzed_gui",
    version="3.0.0a2",
    description="",
    url="",
    author="Uwe Schmitt",
    author_email="uwe.schmitt@id.ethz.ch",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    install_requires=install_requires,
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    include_package_data=True,
)
