#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:52:31 2022

@author: chris
"""

import functools
from matplotlib import pyplot
import numpy as np

from . import misc
#from .np2ta import passwrap as pw
from .set import TablaSet


def _unpack_set(tset, *args):
    '''
    For args of type str which are in the TablaSet arg tset, get elements out
    of tset.
    '''
    args2 = []
    keys = []
    for arg in args:
        if type(arg) is str and arg in tset:
            args2.append(tset[arg])
            keys.append(arg)
        else:
            args2.append(arg)
    return tuple(args2), keys


def _automeshtile(*args):
    '''
    For each arg which is TablArray type, add it to a temporary TablaSet,
    then extract all such args using TablaSet.meshtile, and return all args.

    1. First, this means all TablArray args must be broadcast compatible.
    2. This means after the return, the args will be meshed to flesh out their
    broadcast shape.

    Primarily this is useful for calling plots. So, tablarray has duplicate
    plot methods that should look familiar from matplotlib.pyplot, e.g.
    tablarray.contourf and .plot. Those are wrapped with automeshtile, making
    explicit meshing unnecessary for tablarray users.

    Returns
    -------
    args : tuple
        TablaSet.meshtile() filtered copy of input. args of other types are
        returned unchanged.
    '''
    keys = None
    if len(args) >= 2 and misc.istablaset(args[0]):
        args, keys = _unpack_set(*args)
    temp_set = TablaSet()
    is_TA = [misc.istablarray(arg) for arg in args]
    n_TA = np.sum(is_TA)
    index, = np.nonzero(is_TA)
    if keys is None:
        keys = [('a%d') % i for i in index]
    # first pass, setup a TablaSet
    for i in index:
        arg = args[i]
        key = keys[i]
        temp_set[key] = arg
    args2 = list(args)
    for i in index:
        key = keys[i]
        arg = temp_set.meshtile(key)
        args2[i] = arg
    xdata = dict(is_TA=is_TA, n_TA=n_TA, ind_TA=index, temp_set=temp_set,
                 keys=keys)
    return tuple(args2), xdata


def _wrap_automesh(func):
    """
    wrapper that filters args using automeshtile
    """
    @functools.wraps(func)
    def automeshed(*args, **kwargs):
        args2, _ = _automeshtile(*args)
        func(*args2, **kwargs)
    automeshed.__doc__ = (
        "**automeshed TablArray/TablaSet (passthrough)** %s\n\n" % func.__name__
        + automeshed.__doc__)
    return automeshed


bar = _wrap_automesh(pyplot.bar)
barbs = _wrap_automesh(pyplot.barbs)
boxplot = _wrap_automesh(pyplot.boxplot)
contour = _wrap_automesh(pyplot.contour)
contourf = _wrap_automesh(pyplot.contourf)
csd = _wrap_automesh(pyplot.csd)
hist = _wrap_automesh(pyplot.hist)
plot = _wrap_automesh(pyplot.plot)
polar = _wrap_automesh(pyplot.polar)
psd = _wrap_automesh(pyplot.psd)
#quiver = _wrap_automesh(pyplot.quiver)
scatter = _wrap_automesh(pyplot.scatter)
#triplot = _wrap_automesh(pyplot.triplot)


def quiver2d(*args, **kwargs):
    '''
    Plot a 2d field of arrows.

    See matplotlib.quiver, now wrapped for TablArray

    Call signature::

        quiver([X, Y], UV, [C], **kwargs)

    Where X, Y, UV are broadcast compatible but meshing is not required
    (see automeshtile).

    Parameters
    ----------
    X, Y : TablArray
        arrow base locations
    UV : TablArray
        2d arrow vectors, i.e. cellular shape c(2,)
    C : ndarray or TablArray
        optionally sets the color
    '''
    args, _ = _automeshtile(*args)
    if len(args) == 1:
        uv = args[0]
        # factor uv vector for tuple
        u = uv.cell[0]
        v = uv.cell[1]
        args2 = u, v
    elif len(args) == 2:
        uv, c = args
        u = uv.cell[0]
        v = uv.cell[1]
        args2 = u, v, c
    elif len(args) == 3:
        x, y, uv = args
        u = uv.cell[0]
        v = uv.cell[1]
        args2 = x, y, u, v
    elif len(args) == 4:
        x, y, uv, c = args
        u = uv.cell[0]
        v = uv.cell[1]
        args2 = x, y, u, v, c
    else:
        raise ValueError
    pyplot.quiver(*args2, **kwargs)


def quiver3d(*args, **kwargs):
    '''
    Plot a 3d field of arrows.

    Call signature::

        quiver3d([X, Y, Z], UVW, [C], **kwargs)

    See ax.quiver for 3d, esp. kwargs like length

    Where X, Y, Z, UVW are broadcast compatible but meshing is not required
    (see automeshtile).

    Parameters
    ----------
    X, Y, Z: TablArray
        arrow base locations
    UVW : TablArray
        3d arrow vectors, i.e. cellular shape c(3,)
    C : ndarray or TablArray
        optionally sets the color
    '''
    args, _ = _automeshtile(*args)
    if len(args) == 1:
        uvw = args[0]
        # factor uv vector for tuple
        u = uvw.cell[0]
        v = uvw.cell[1]
        w = uvw.cell[2]
        args2 = u, v, w
    elif len(args) == 2:
        uvw, c = args
        u = uvw.cell[0]
        v = uvw.cell[1]
        w = uvw.cell[2]
        args2 = u, v, c
    elif len(args) == 4:
        x, y, z, uvw = args
        u = uvw.cell[0]
        v = uvw.cell[1]
        w = uvw.cell[2]
        args2 = x, y, z, u, v, w
    elif len(args) == 5:
        x, y, z, uvw, c = args
        u = uvw.cell[0]
        v = uvw.cell[1]
        w = uvw.cell[2]
        args2 = x, y, z, u, v, w, c
    else:
        raise ValueError
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')
    ax.quiver(*args2, **kwargs)


def plot3d(*args, **kwargs):
    '''
    3d scatter plot
    '''
    args, _ = _automeshtile(*args)
    args2 = []
    for arg in args:
        arg2 = arg.base.ravel() if misc.istablarray(arg) else arg
        args2.append(arg2)
    ax = pyplot.axes(projection='3d')
    ax.plot(*tuple(args2), **kwargs)


def contour3d_solidrect(*args, cbargs={'pad': 0.1}, **kwargs):
    '''
    Contour plots in 3d, i.e. for (x, y, z, scalar-data), display as a 3d
    rectangular solid with 2d contours along the edge surfaces.

    Note that arrays must be 3dim in cartesian coordinates, and the solid
    must be rectangular.
    '''
    args, xdata = _automeshtile(*args)
    tset = xdata['temp_set']
    keys = xdata['keys']
    x, y, z, data = args[:4]
    # determine slicing
    def _get_sliceat(ax, position):
        ax_dim, xdata = tset.axis_of(keys[ax])
        N = xdata['N']
        sign = xdata['sign']
        if sign > 0:
            i = int(position * (N - 1) + .5)
            mn = xdata['beg']
            mx = xdata['end']
        else:
            i = int((1 - position) * (N - 1) + .5)
            mn = xdata['end']
            mx = xdata['beg']
        slice0 = [slice(None), slice(None), slice(None)]
        slice0[ax_dim] = i
        sliced_set = tset.__getitem__(tuple(keys + slice0))
        x0, y0, z0, data0 = sliced_set.meshtile(*tuple(keys))
        return x0, y0, z0, data0, mn, mx
    # plot args
    d_mn = data.min()
    d_mx = data.max()
    plot_kwargs = dict(
        vmin=d_mn, vmax=d_mx, levels=np.linspace(d_mn, d_mx, 11))
    # do the contour plots
    ax = pyplot.axes(projection='3d')
    x0, y0, _, data0, zmn, zmx = _get_sliceat(2, 1)
    ax.contourf(x0, y0, data0, zdir='z', offset=zmx, **plot_kwargs, **kwargs)
    x0, _, z0, data0, ymn, ymx = _get_sliceat(1, 0)
    ax.contourf(x0, data0, z0, zdir='y', offset=ymn, **plot_kwargs, **kwargs)
    _, y0, z0, data0, xmn, xmx = _get_sliceat(0, 1)
    C = ax.contourf(data0, y0, z0, zdir='x', offset=xmx, **plot_kwargs, **kwargs)
    # plot the edges
    kw_edges = dict(color='0.1', linewidth=1, zorder=1e3)
    ax.plot([xmx, xmx], [ymn, ymx], [zmx, zmx], **kw_edges)
    ax.plot([xmn, xmx], [ymn, ymn], [zmx, zmx], **kw_edges)
    ax.plot([xmx, xmx], [ymn, ymn], [zmn, zmx], **kw_edges)
    # the colorbar
    pyplot.colorbar(C, ax=ax, **cbargs)
