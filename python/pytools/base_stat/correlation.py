"""输出所有相关性值
"""

from scipy.stats import kendalltau, spearmanr, pearsonr
import pandas as pd

def correlation_summary(x, y) -> pd.DataFrame:
    """相关性总列

    Args:
        x (_type_): 任何1D的数据
        y (_type_): 任何1D的数据

    Returns:
        pd.DataFrame: 返回三个结果的表
    """
    return pd.DataFrame({
        "kendall-τ": list(kendalltau(x, y)),
        "Pearson": list(pearsonr(x, y)),
        "Spearman": list(spearmanr(x, y))
    }, index=["Correlation", "Sig."])