import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 191207196 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.1 
    stat, pval = ttest_ind(x, y, equal_var=False)
    return pval < alpha
