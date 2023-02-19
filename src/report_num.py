import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fit_report_nums(report_nums, deg, time_range=None, doPlot=False):
    """Use polynomials to fit the report numbers with time.
    
    Parameters
    ----------
    report_nums : np.array (of type float64)
        The array of reported numbers corresponding to the decreasing consecutive dates.
    deg : int
        The degree of the polynomial used for fitting.
    time_range : int or None
        The range for selecting data, should not exceed the size of report_nums.
        Once specified, only the first many data will be used for fitting. This is
        because Wordle was very famous when it was first released, so there was a
        peak in the beginning of time, that is, towards the end of the array, which
        may cause overfitting due to unusual data. The option None stands means to
        disable the selection process.
    doPlot : boolean
        Whether to plot the original and fitted data.

    Returns
    -------
    normalize_coeff : float
        The normalizing coefficient used for the array of report_nums, used for reverting
        the prediction result back to the real scale.
    times : np.array
        The array of times, treating the last entry of report_nums as date 1, etc.
    coeffs : np.array
        The coefficient array returned by the fit.

    Example
    -------
    
    """
    normalize_coeff = np.max(report_nums)
    report_nums /= normalize_coeff
    nums = report_nums[:time_range]
    times = np.array(range(report_nums.size, 0, -1))
    coeffs = np.polyfit(times[:time_range], nums, deg)
    poly = np.polyval(coeffs, times)
    if doPlot:
        plt.scatter(times, report_nums, s=1)
        plt.plot(times, poly)
        plt.show()

if __name__ == "__main__":
    data = pd.read_excel("./dataset/wordle_data.xlsx")
    report_nums = data["result_num"].to_numpy(np.float64)
    print(data)

    # Use polynomials for fitting
    for time_range in [100, 200, 300]:
        for deg in range(1, 5):
            normalize_coeff, times, coeffs = fit_report_nums(report_nums, deg, time_range=time_range, doPlot=True)

