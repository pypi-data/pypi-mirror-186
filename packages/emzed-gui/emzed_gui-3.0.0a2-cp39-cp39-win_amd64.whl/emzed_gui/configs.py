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


import matplotlib.cm

colors = matplotlib.cm.get_cmap("tab10").colors


def get_color(i, brightened=False):
    c = colors[i % len(colors)]
    color = "#" + "".join("%02x" % round(255 * v) for v in c)
    if brightened:
        color = brighten(color)
    return color


def brighten(color):
    rgb = [int(color[i : i + 2], 16) for i in range(1, 6, 2)]
    rgb_light = [min(ii + 50, 255) for ii in rgb]
    return "#" + "".join("%02x" % v for v in rgb_light)


def config_for_eic(i):
    return dict(linewidth=2, color=get_color(i))


def config_for_fitted_peakshape_model(i):
    return {
        "fill.alpha": 0.25,
        "fill.color": get_color(i, brightened=True),
        "line.width": 0,
        "line.style": "NoPen",
    }


def config_for_spectrum(i):
    return dict(color=get_color(i), linewidth=1)
