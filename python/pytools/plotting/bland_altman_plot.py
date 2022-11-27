"""绘制Bland-Altman图
"""

from __future__ import annotations
from typing import List

import pandas as pd
import scipy.stats as st

import plotly.graph_objects as go
from plotnine import (
    ggplot,
    geom_point,
    geom_hline,
    ggtitle,
    xlab, ylab,
    theme_bw
)

# pylint: disable=C0103
def plot_bland_altman(x, y, alpha: float = 0.05, backend: str = "plotnine") -> ggplot | go.Figure:
    """绘制Bland-Altman图

    Args:
        x (_type_): 1D数据
        y (_type_): 1D数据
        alpha (float): 显著性值
        backend (str, optional): _description_. Defaults to "plotnine".

    Returns:
        ggplot | go.Figure: _description_
    """
    z_score = st.norm.ppf(1 - alpha/2)
    temp_df = pd.DataFrame({
            "diff": pd.Series(x) - pd.Series(y),
            "avg": (pd.Series(x) + pd.Series(y)) / 2
        })
    mean_diff = temp_df['diff'].mean()
    lower = mean_diff - z_score * temp_df['diff'].std()
    upper = mean_diff + z_score * temp_df['diff'].std()

    if backend == "plotly":
        fig = go.Figure(
            data = [
                go.Scatter(
                    x=temp_df["avg"],
                    y=temp_df["diff"],
                    mode="markers"
                )
            ],
        )
        fig.add_hline(y=mean_diff)
        fig.add_hline(y=upper, line_color="red", line_dash="dash")
        fig.add_hline(y=lower, line_color="red", line_dash="dash")
        fig.add_hline(y=0, line_color="grey", line_dash="dash")
        fig.update_layout(
            title="Bland-Altman Plot",
            xaxis_title="Average",
            yaxis_title="Difference Between Instruments",
            template="plotly_white",
        )
    else:
        fig = ggplot(temp_df, aes(x = "avg", y = "diff")) +\
            geom_point(size=2) +\
            geom_hline(yintercept = mean_diff) +\
            geom_hline(yintercept = lower, color = "red", linetype="dashed") +\
            geom_hline(yintercept = upper, color = "red", linetype="dashed") +\
            geom_hline(yintercept = 0, color = "grey", linetype="dashed") +\
            ggtitle("Bland-Altman Plot") +\
            ylab("Difference Between Instruments") +\
            xlab("Average") + theme_bw()
    return fig
