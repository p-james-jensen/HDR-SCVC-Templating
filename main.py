from scipy.optimize import nnls

import numpy as np

from data30_6gysurf_1297 import ideal_doses, dwell_matrix, weights

optimal_times = nnls((np.array(dwell_matrix) * np.array([weights])).transpose() / 100,
                     np.array(ideal_doses) * np.array(weights), 10000)[0]
print(optimal_times)

resulting_doses = optimal_times.dot(dwell_matrix) / 100
print(resulting_doses)
