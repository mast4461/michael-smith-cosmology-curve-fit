import scipy.optimize as optimize
from settings import curve_fit_parameter_settings

def curve_fit(model, x, y, sigma, p0, bounds, loss_modifier='linear'):
    # Weigh the residuals by the measurement errors simply by division,
    # just like scipy.optimize.curve_fit does
    sigma_inverse = 1/sigma
    compute_residuals = lambda p: sigma_inverse * (model(x, p[0], p[1]) - y)

    res_lsq = optimize.least_squares(
        compute_residuals,
        x0=p0,
        bounds=bounds,
        loss=loss_modifier
    )

    return (res_lsq['x'], None)
