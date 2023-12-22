from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np


# Линейная
def liner_function_coefficients(x, y):
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y)
    return [model.coef_[0], model.intercept_]


# параболическая
def parabolic_function_coefficients(x, y):
    return np.polyfit(x, y, 2)


# гиперболическая

def hyperbolic_function_coefficients(x, y):
    return liner_function_coefficients((1 / x), y)


# логарифмическая
def logarithmic_function_coefficients(x, y, base):
    try:
        return liner_function_coefficients(np.log(x) / np.log(base), y)
    except:
        return None, None


# коэффициент детерминации
def r_squared(y_true, y_pred):
    # Общая сумма квадратов отклонений
    total_sum_of_squares = np.sum((y_true - np.mean(y_true)) ** 2)

    # Остаточная сумма квадратов отклонений
    residual_sum_of_squares = np.sum((y_true - y_pred) ** 2)

    # Коэффициент детерминации
    r2 = 1 - (residual_sum_of_squares / total_sum_of_squares)

    return r2
