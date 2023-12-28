import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate

from tools.coefficient_calculators import logarithmic_function_coefficients, r_squared

from tools.math_functions import logarithmic_function


class LogarithmicCalc:
    # Основания логарифма которые будем перебирать
    log_base_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # Все расчеты по заданным основаниям логарифма
    all_calc = []
    # Наилучший из расчетов
    max_calc = None

    def __init__(self, x, y):
        self.X = np.array(x).astype(float)
        self.Y = np.array(y).astype(float)
        self._calc()

    def _calc(self):
        for base in self.log_base_list:
            # Ищем коэффициенты функции
            coefficients = logarithmic_function_coefficients(self.X, self.Y, base)
            # Считаем значения y по полученной функции
            y_calc = logarithmic_function(self.X, *coefficients, base)
            # Даем оценку с помощью коэффициента детерминации
            r_squared_ = r_squared(self.Y, y_calc)
            # Сохраняем результат по данному основанию логарифма
            result = [base, *coefficients, r_squared_]
            self.all_calc.append(result)
            # Обновляем максимум если текущее значение больше
            if (not self.max_calc) or (self.max_calc[3] < r_squared_):
                self.max_calc = result

    def show(self):
        result_rows = [['Наилучшее', '', '', ''], self.max_calc]
        table_rows = [*self.all_calc, *result_rows]
        headers_table = ['Основание лог', 'b1', 'b0', 'Коэффициент детерминации']
        main_table = tabulate(table_rows, headers_table)
        wrap_table = tabulate([[main_table]], ['Логарифмическая'], tablefmt='grid')
        print(wrap_table)

    def graphic(self, name: str):
        step = self.get_step()
        range_ = self.get_range()
        x_pred = np.arange(*range_, step)
        y_pred = logarithmic_function(x_pred, *self.max_calc[1:-1], self.max_calc[0])
        plt.plot(x_pred, y_pred, color='red',label=name + '_Прогноз')
        plt.scatter(self.X, self.Y, label=name + '_Исходник')
        plt.legend()
        plt.show()

    def get_range(self):
        shift = self.X.max() - self.X.min()
        start = self.X.min() - shift
        end = self.X.max() + shift
        if start < 0:
            end += abs(start)
            start = 0.0000001
        return [start, end]

    def get_step(self):
        return (self.X.max() - self.X.min()) / self.X.size
