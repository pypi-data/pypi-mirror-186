"""
Helper funcs for plotly figures
"""
import numpy as np
import pandas as pd
import warnings
try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
except:
    warnings.warn("'plotly' not available.", RuntimeWarning)
from collections import defaultdict
from collections.abc import Iterable
from functools import partial
from .. import _helper
from .base import color_std, plotly_default_colors

def add_offset(x0, xf, offset=0.05):
    """x0 (xf) == lower (upper) limit for the axis range."""
    inverse_transform = lambda *xs: [(xf-x0)*x + x0 for x in xs]
    return inverse_transform(-offset, 1+offset)
    
def get_common_range(fig, axes=["x", "y"], offset=[0.05, 0.05]):
    data = defaultdict(list)
    for plot in fig.data:
        for ax in axes:          
            if hasattr(plot, f"error_{ax}") and getattr(plot, f"error_{ax}").array is not None:
                additions = [np.array([*plot[f"error_{ax}"]["array"]]), -np.array([*plot[f"error_{ax}"]["array"]])] 
            else:
                additions = [0]
            for addition in additions:
                try:
                    arr = (plot[ax] + addition)[~np.isnan(plot[ax])]
                except:
                    continue
                arr_min, arr_max = arr.min(), arr.max()
                data[f"{ax}-min"].append(arr_min)
                data[f"{ax}-max"].append(arr_max)
    for k, v in data.items():
        func = min if "min" in k else max
        data[k] = func(v)
    ranges = {ax: add_offset(data[f"{ax}-min"], data[f"{ax}-max"], offset=off) for ax, off in zip(axes, offset)}
    return ranges

def get_nplots(fig):
    return sum(1 for x in fig.layout if "xaxis" in x)

def mod_delete_axes(fig, axes=["x", "y"]):
    non_visible_axes_specs = dict(visible=False, showgrid=False, zeroline=False) 
    return {f"{ax}axis{i}": non_visible_axes_specs for ax in axes for i in [""] + [*range(1, get_nplots(fig) + 1)]}

def get_mod_layout(key, val=None):
    def mod_layout(fig, val, axes=["x","y"]):
        if isinstance(val, Iterable) and not isinstance(val, str):
            return {"{}axis{}_{}".format(ax, i, key): v for (ax, v) in zip(axes, val) for i in [""] + [*range(1, get_nplots(fig) + 1)]}
        else:
            return {"{}axis{}_{}".format(ax, i, key): val for ax in axes for i in [""] + [*range(1, get_nplots(fig) + 1)]}
    if val is None:
        return mod_layout
    else:
        def mod_layout_fixed_val(fig, axes=["x", "y"]):
            return mod_layout(fig, val, axes)
        return mod_layout_fixed_val

mod_dashes           = partial(_helper.sequence_or_stream, ["solid", "dash", "dot"])
mod_ticksize         = get_mod_layout("tickfont_size")
mod_logaxes          = get_mod_layout("type", "log") 
mod_expfmt           = get_mod_layout("exponentformat", "power")
mod_range            = get_mod_layout("range")
mod_logaxes_expfmt   = lambda fig, axes=["x", "y"]: {**mod_logaxes(fig, axes=axes), **mod_expfmt(fig, axes=axes)}

def mod_common_range(fig, axes=["x", "y"], **kwargs):
    return mod_range(fig, val=get_common_range(fig, axes=axes, **kwargs), axes=axes)

def get_figure(height=800, width=1000, ticksize=32, font_size=40, margin=None, font_family="sans-serif", hovermode=False, delete_axes=False, **kwargs):
    fig = go.Figure(layout=dict(margin=dict(l=100, r=20, b=80, t=20, pad=1) if margin is None else margin,
                                height=height, width=width, yaxis=dict(tickfont_size=ticksize),
                                xaxis=dict(tickfont_size=ticksize), font_size=font_size, legend_font_size=font_size,
                                font_family=font_family, hovermode=hovermode,
                                **kwargs))
    if delete_axes:
        fig.update_layout(**mod_delete_axes(fig), margin=dict(l=0, t=0, b=0, r=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def get_subplots(cols, rows=1, horizontal_spacing=0.03, vertical_spacing=0.03, height=None, width=2500, ticksize=32, font_size=40, font_family="sans-serif",
                 hovermode=False, delete_axes=False, shared_xaxes=True, shared_yaxes=True, layout_kwargs={}, 
                 **make_subplots_kwargs):
    height = 800*rows if height is None else height
    fig = make_subplots(figure=go.Figure(layout=dict(margin=dict(l=100, r=20, b=80, t=60, pad=1), height=height, width=width)),
                        shared_yaxes=shared_yaxes, shared_xaxes=shared_xaxes,                        
                        horizontal_spacing=horizontal_spacing, vertical_spacing=vertical_spacing, rows=rows, cols=cols,
                        **make_subplots_kwargs
                       )
                    
    fig.for_each_annotation(lambda a: a.update(font={'size':font_size, "family":font_family}))
    fig.update_layout(**mod_ticksize(fig, val=ticksize), legend_font_size=font_size, hovermode=hovermode, **layout_kwargs)
    if delete_axes:
        fig.update_layout(**mod_delete_axes(fig), margin=dict(l=0, t=0, b=0, r=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def transparent_colorscale(fig, threshold=1e-10):
    """Values below threshold are invisible."""
    colorscale = fig.layout["coloraxis"]["colorscale"]
    low_limit = colorscale[0]
    new_low_limit = (threshold, low_limit[1])
    new_colorscale = ((0, 'rgba(0,0,0,0)'), new_low_limit, *colorscale[1:])
    return new_colorscale

def multiindex_to_label(i, depth=2):
    return [i.get_level_values(k).to_list() for k in range(depth)]

def set_multicategory_from_df(fig, df):
    fig.update_layout(xaxis_type="multicategory", yaxis_type="multicategory")
    fig.data[0]["x"] = multiindex_to_label(df.columns)
    fig.data[0]["y"] = multiindex_to_label(df.index)
    return

def CI_plot(x, y, CI, label=None, width=0.05, ms=10, color='rgba(255, 127, 14, 0.3)', fig=None, x_title=None, y_title=None):
    """
    Box plot where the box corresponds to the CI.
    
    Attributes:
        - x:    x coordinate for the CI
        - y:    value of the magnitude for the sample. Example: the mean if CI is a CI for the mean.
        - CI:   Confidence interval for y.
    """
    if fig is None:
        fig = get_figure(xaxis_title=x_title, yaxis_title=y_title)
    for i, (ci, x_val, ci_stat) in enumerate(zip(CI, x, y)):
        fig.add_trace(go.Scatter(x=[x_val]*2, y=ci[::-1], showlegend=False, mode="markers",
                                 marker=dict(color=color, symbol=["arrow-bar-down", "arrow-bar-up"], size=ms, line=dict(color="gray", width=2))
                                ))
        fig.add_shape(type="rect", xref="x", yref="y", line=dict(color="gray",width=3), fillcolor=color, x0=i-width, y0=ci[0], x1=i+width, y1=ci[1])
        fig.add_shape(type="line", xref="x", yref="y", line=dict(color="gray", width=4),  x0=i-width, y0=ci_stat, x1=i+width, y1=ci_stat)
    if label is not None:
        yrange = [*get_common_range(fig, axes=["y"]).values()][0]
        fig.add_trace(go.Scatter(x=[1000], y=[1000], mode="markers", name=label, showlegend=True,
                                 marker=dict(symbol="square", color=color, size=22), line=dict(color="gray", width=2)))
        fig.update_layout(**mod_range(fig, ([-0.25, len(x)-0.75], yrange)))
    return fig

def permtest_plot(df, H1="", colorscale="Inferno", log=True, height=800, width=1000, font_size=40, bar_len=0.9, bar_x=0.95, bar_thickness=100):
    """H1 should not contain latex code. Use unicode and HTML for super/sub-indices."""
    if log:
        df = np.log10(df)
        zmin, zmax = np.log10(0.05), 0
        legtitle = "log<sub>10</sub>P-value"
    else:
        zmin, zmax = None, None
        legtitle = "P-value"
    fig = px.imshow(df, zmin=zmin, zmax=zmax, color_continuous_scale=colorscale)
    fig.update_layout(coloraxis_colorbar=dict(len=bar_len, x=bar_x, title=f"{legtitle}<br>H<sub>1</sub>: {H1}", thickness=bar_thickness),
                      height=height, width=width, font_size=font_size, hovermode=False,
                      margin=dict(l=0, b=0, t=0, r=0)
                     )
    return fig
    
def violin(df, CI=None, CI_line="mean", **CI_kwargs):
    """
    Violin plot including optionally the CI.
    
    Attributes:
        - df:   melted DataFrame. Contains only two columns: variable name (x) and value (y).
                                  The column names set the OX and OY labels.
    """
    x, y = df.columns
    fig = get_figure(xaxis_title=x, yaxis_title=y)
    fig.add_trace(go.Violin(x=df[x], y=df[y], showlegend=False))
    if CI is not None:
        fig = CI_plot(df[x].unique(), getattr(df.groupby(x), CI_line)().values.squeeze(), CI, fig=fig, **CI_kwargs)
    return fig
