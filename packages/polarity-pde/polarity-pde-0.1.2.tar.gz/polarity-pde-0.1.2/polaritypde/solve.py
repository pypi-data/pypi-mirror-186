import numpy as np


def evaluate(func, xrange, yrange, resolution0=1000, iterations=1, resolution_step=2, args=()):
    """
    Solve a function in the form 0 = f(x, y)

    :param func: function to solve (0 = f(x,y,*args))
    :param xrange: (lower x, upper x)
    :param yrange: (lower y, upper y)
    :param resolution0: resolution of grid space for first iteration
    :param iterations: if > 1 will iteratively refine solution by increasing resolution by factor of resolution_step
    :param resolution_step:
    :param args: additional arguments for func
    :return: two 1D arrays of points corresponding to x and y coordinates. NB these are UNORDERED, plot using
        plt.scatter(xpoints,ypoints)

    """

    for iteration in range(iterations):

        if iteration == 0:

            # Set x and y values
            n_sims = resolution0
            xvals = np.linspace(xrange[0], xrange[1], n_sims)
            yvals = np.linspace(yrange[0], yrange[1], n_sims)

            # Evaluate
            res = func(np.tile(xvals, (n_sims, 1)).T, np.tile(yvals, (n_sims, 1)), *args)
            res_2d_sign = np.sign(res)

        else:
            # Find boundary regions
            a = np.nonzero(np.nan_to_num(np.diff(res_2d_sign, axis=0)))
            b = np.nonzero(np.nan_to_num(np.diff(res_2d_sign, axis=1)))
            c = np.nonzero(np.nan_to_num(res_2d_sign[:-1, :-1] - res_2d_sign[1:, 1:]))
            xpoints = np.r_[a[0], b[0], c[0]]
            ypoints = np.r_[a[1], b[1], c[1]]

            # Set x and y values
            n_sims = resolution_step * (n_sims - 1) + 1

            run_bool = np.zeros([n_sims, n_sims])
            for x, y in zip(xpoints, ypoints):
                run_bool[x * resolution_step:x * resolution_step + (resolution_step + 1),
                y * resolution_step:y * resolution_step + (resolution_step + 1)] = 1
            sims_array_ind = np.nonzero(run_bool)
            xvals = xrange[0] + sims_array_ind[0] * (xrange[1] - xrange[0]) / (n_sims - 1)
            yvals = yrange[0] + sims_array_ind[1] * (yrange[1] - yrange[0]) / (n_sims - 1)

            # Evaluate
            res = func(xvals, yvals, *args)

            # Organise res
            res_2d = np.nan * np.zeros([n_sims, n_sims])
            for r in range(len(res)):
                res_2d[sims_array_ind[0][r], sims_array_ind[1][r]] = res[r]
            res_2d_sign = np.sign(res_2d)

    a = np.nonzero(np.nan_to_num(np.diff(res_2d_sign, axis=0)))
    b = np.nonzero(np.nan_to_num(np.diff(res_2d_sign, axis=1)))
    c = np.nonzero(np.nan_to_num(res_2d_sign[:-1, :-1] - res_2d_sign[1:, 1:]))
    xpoints = np.r_[a[0], b[0], c[0]]
    ypoints = np.r_[a[1], b[1], c[1]]

    xpoints = xrange[0] + (xpoints / n_sims) * (xrange[1] - xrange[0])
    ypoints = yrange[0] + (ypoints / n_sims) * (yrange[1] - yrange[0])
    return xpoints, ypoints
