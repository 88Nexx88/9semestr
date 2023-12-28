import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate

from tools.coefficient_calculators import (liner_function_coefficients,
                                     parabolic_function_coefficients,
                                     hyperbolic_function_coefficients,
                                     r_squared)

from tools.math_functions import (liner_function,
                            parabolic_function,
                            hyperbolic_function)


class AllModelCalc:
    liner = None
    parabolic = None
    hyperbolic = None
    max = None

    def __init__(self, x, y):
        self.X = np.array(x).astype(float)
        self.Y = np.array(y).astype(float)
        self._calc()

    def _calc(self):
        x = self.X
        y = self.Y

        # Линейная
        liner_function_coefficients_ = liner_function_coefficients(x, y)
        y_calc = liner_function(x, *liner_function_coefficients_)
        r2 = r_squared(y, y_calc)
        self.liner = ['Линейная', *liner_function_coefficients_, r2]
        self.max = self.liner

        # параболическая
        parabolic_function_coefficients_ = parabolic_function_coefficients(x, y)
        y_calc = parabolic_function(x, *parabolic_function_coefficients_)
        r2 = r_squared(y, y_calc)
        self.parabolic = ['Параболическая', *parabolic_function_coefficients_, r2]
        if r2 > self.max[-1]:
            self.max = self.parabolic

        # гиперболическая
        zero_indexes = np.where(x == 0)
        x = np.delete(x, zero_indexes, axis=0)
        y = np.delete(y, zero_indexes, axis=0)
        hyperbolic_function_coefficients_ = hyperbolic_function_coefficients(x, y)
        y_calc = hyperbolic_function(x, *hyperbolic_function_coefficients_)
        r2 = r_squared(y, y_calc)
        self.hyperbolic = ['Гиперболическая', *hyperbolic_function_coefficients_, r2]
        if r2 > self.max[-1]:
            self.max = self.hyperbolic

    def show(self):
        table_rows = [[self.liner[0], '', *self.liner[1:]],
                      [*self.parabolic],
                      [self.hyperbolic[0], '', *self.hyperbolic[1:]]]
        headers_table = ['Тип', 'b2', 'b1', 'b0', 'Коэф детерминации']
        main_table = tabulate(table_rows, headers_table, tablefmt='grid')
        print(main_table)

    def graphic(self, name: str):
        step = self.get_step()
        range_ = self.get_range()
        x_pred = np.arange(*range_, step)
        y_pred = None
        if self.max[0] == "Линейная":
            y_pred = liner_function(x_pred, *self.max[1:-1])
        elif self.max[0] == "Параболическая":
            y_pred = parabolic_function(x_pred, *self.max[1:-1])
        elif self.max[0] == "Гиперболическая":
            x_pred_pol = x_pred[np.where(x_pred > 0)]
            x_pred_otr = x_pred[np.where(x_pred < 0)]
            y_pred_pol = hyperbolic_function(x_pred_pol, *self.max[1:-1])
            y_pred_otr = hyperbolic_function(x_pred_otr, *self.max[1:-1])
            plt.plot(x_pred_otr, y_pred_otr, color='red', label=name + '_Прогноз')
            plt.plot(x_pred_pol, y_pred_pol, color='red', label=name + '_Прогноз')
            plt.scatter(self.X, self.Y, label=name + '_Исходник')
            plt.legend()
            plt.show()
            return


        plt.plot(x_pred, y_pred, color= 'red', label=name + '_Прогноз')
        plt.scatter(self.X, self.Y, label=name + '_Исходник')
        plt.legend()
        plt.show()

    def get_range(self):
        shift = self.X.max() - self.X.min()
        start = self.X.min() - shift
        end = self.X.max() + shift
        # if start < 0:
        #     end += abs(start)
        #     start = 0.0000001
        return [start, end]

    def get_step(self):
        return (self.X.max() - self.X.min()) / self.X.size
