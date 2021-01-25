import scipy.optimize as optimize
from settings import curve_fit_parameter_settings

def curve_fit(model, x, y, sigma, p0, bounds, loss_modifier='linear'):
    # Weigh the residuals by the measurement errors simply by division,
    # just like scipy.optimize.curve_fit does
    compute_residuals = lambda p: (1 / sigma) * (model(x, p[0], p[1]) - y)

    print("---------------------------------")
    print("Fitting model:", model.__name__)

    res_lsq = optimize.least_squares(
        compute_residuals,
        x0=p0,
        bounds=bounds,
        loss=loss_modifier,
        verbose=2
    )

    p = res_lsq["x"]

    # The Coefficient of determination is computed according to the
    # "most general definition" from the wikipedia article:
    # https://en.wikipedia.org/wiki/Coefficient_of_determination#Definitions
    SS_res = ((y - model(x, p[0], p[1])) ** 2).sum()
    SS_tot = ((y - y.mean()) ** 2).sum()
    coefficient_of_determination = 1 - SS_res / SS_tot

    print("Coefficient of determination:", coefficient_of_determination, "(SS_tot:", SS_tot, " SS_res:", SS_res, ")")
    print("Hubble constant:", p[0])
    print("Matter density:", p[1])
    return (p, None)
