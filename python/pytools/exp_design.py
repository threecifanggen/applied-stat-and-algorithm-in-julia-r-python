"""实验设计
"""
import scipy.stats as st

def num_of_quality_subjects(delta: float, p: float, alpha: float = 0.05) -> float:
    """定性实验中计算至少需要的样本数

    Args:
        delta (float): 定性允许的误差
        p (float): 定性正样本大致大小
        alpha (float, optional): 显著性. Defaults to 0.05.

    Returns:
        float: 返回样本数
    """
    z_score = st.norm.ppf(1 - alpha / 2)
    return z_score ** 2 * p * (1 - p) / delta ** 2

def num_of_quantity_subjects(delta: float, sigma: float, alpha: float = 0.05) -> float:
    """定量实验中计算至少需要的样本数

    Args:
        delta (float): 允许的误差
        sigma (float): 标准差
        alpha (float, optional): 显著性. Defaults to 0.05.

    Returns:
        float: 样本数
    """
    z_score = st.norm.ppf(1 - alpha / 2)
    return (z_score * sigma / delta) ** 2