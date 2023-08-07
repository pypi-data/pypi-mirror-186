from ._models import mc, mc_t
import numpy as np
from scipy.optimize import minimize
from scipy.stats import linregress
import matplotlib.pyplot as plt
from findpeaks import findpeaks
from logging import warning
from ._example_data import return_data


class findlinear:
    """Calculate the evidence of a segment of curve being linear, and find the
    global maximum or local maxima.

    Parameters
    ----------
    X : list of floats or 1-D numpy array
        the x vector of data.
    Y : array-like
        the y vector or matrix of data, each row being one replicate of
        measurement.
    std : list of floats or 1-D numpy array, optional
        the standard deviation of the input data.
    intercept : bool, default True
        if False, the intercept is forced to be zero.
    start : int, default 0
        the min index of x that a valid segment allows.
    end : int, optional
        the max index of x that a valid segment allows (inclusive).
    estimate_std : bool, optional
        if True, estimate std from data; default True when Y has >= 3
        replicates.
    minlen : int, default 3
        the minimal length of a valid segment (must be >= 3).
    attempt : int, default 20
        the max number of attempts to run the BFGS minimize routine when the std
        is neither provided nor estimated.

    Raises
    ------
    ValueError
        when Y has multiple replicates and std is provided.

    Examples
    --------
    >>> from findlinear.findlinear import findlinear, get_example_data
    >>> x, y = get_example_data()
    >>> fl = findlinear(x, y)
    >>> fl.find_all()
    >>> fl.plot()
    >>> fl.get_argmax()
    >>> fl.get_peaks()

    """

    def __init__(
        self,
        X,
        Y,
        std=None,
        intercept=True,
        start=0,
        end=None,
        estimate_std="default",
        minlen=3,
        attempt=20,
    ):
        # Load settings
        self.X = np.asarray(X)
        self.Y = np.asarray(Y)
        if isinstance(std, (list, np.ndarray)):
            self.std = np.asarray(std)
        else:
            self.std = None
        self.start = start
        if end:
            self.end = end
        else:
            self.end = self.X.shape[0]
        if minlen >= 3:
            self.minlen = minlen
        else:
            warning("minlen must be >= 3. Reset to 3.")
            self.minlen = 3
        self.attempt = attempt
        self.intercept = intercept
        # handle estimate_std
        if estimate_std == "default":
            # if Y has 3 replicates and std is none
            if (self.Y.ndim > 1) and (self.Y.shape[0] >= 3) and (self.std is None):
                estimate_std = True
            else:
                estimate_std = False
        # if std is provided, do not estimate_std (overwrite user's setting)
        if self.std is not None:
            estimate_std = False
        # if std is not provided but Y is 1-D, impossible to estimate_std
        elif self.Y.ndim == 1:
            estimate_std = False
        # if std is provided but Y is 2-D, throw error
        if self.std is not None and self.Y.ndim > 1:
            raise ValueError("When std is provided, Y should be 1-D.")
        # now estimate std
        self.estimate_std = estimate_std
        if estimate_std:
            # x, y, instead of X, Y, are what the methods actually use
            self.x = self.X
            self.y = self.Y.mean(axis=0)
            # OK to write std because estimate_std is True only when std is None
            self.std = self.Y.std(axis=0)
        else:
            self.x = self.X
            self.y = self.Y
        # handle estimated std=0 when replicates have the same value by chance
        if self.std is not None:
            self.std[self.std == 0] = self.std.mean()
        # results
        self.evidence = {
            "find from": None,
            "find all": None,
            "find through": None,
        }
        self.through = None
        self.peaks = None
        self.lastrun = None

    def _find_from_unknown_s(self):
        """internal: calculate the evidence when the std is unknown.

        Raises
        ------
        ValueError
            when the length of longest segment is smaller than the minlen.

        """

        res = []
        start, end, minlen, intercept = (
            self.start,
            self.end,
            self.minlen,
            self.intercept,
        )
        funcs = mc_t(intercept)
        if end - start <= minlen:
            raise ValueError(f"(end - start) must be no less than {minlen}.")
        # Initial guess with linear regression
        init_guess = self._get_init_guess()
        # Go through N's
        for n in range(minlen, end + 1 - start):
            # Run calculation and update init_guess
            init_guess, evi = self._cal_evidence_unknown_s(
                start, start + n, init_guess, funcs
            )
            if evi is None:
                break
            else:
                res.append(evi)
        return res

    def _get_init_guess(self):
        """internal: get initial guess by regressing over the whole x and y

        """
        X, Y, intercept = self.x, self.y, self.intercept
        if Y.ndim > 1:
            # take the first rep as first guess
            lin_res = linregress(X, Y[0, :])
        else:
            lin_res = linregress(X, Y)
        if intercept:
            init_guess = (lin_res.slope, lin_res.intercept)
        else:
            init_guess = (lin_res.slope,)
        return init_guess

    def _cal_evidence_unknown_s(self, start, end, init_guess, funcs):
        """internal: calculate evidence without std

        Parameters
        ----------
        start : init
            start of segment
        end : int
            end of segment (inclusive)
        init_guess : tuple
            initial guess for scipy.optimize.minimize
        funcs : tuple of functions
            tuple of -logL, hessian and jacobian.

        """
        X, Y, intercept, attempt = (
            self.x,
            self.y,
            self.intercept,
            self.attempt,
        )
        neglogL, hess, jac = funcs
        # flatten multiple reps
        if Y.ndim > 1:
            X_flat = np.append([], [X[start:end]] * Y.shape[0])  # flatten X
            Y_flat = Y[:, start:end].flatten(order="C")
            n_flat = len(X[start:end]) * Y.shape[0]
        else:
            X_flat = X[start:end]
            Y_flat = Y[start:end]
            n_flat = len(X[start:end])
        # run multiple attempts in case optimisation fails
        for k in range(attempt):
            if intercept:
                # Guess m and c
                th00 = np.random.normal(init_guess[0], 2 * np.abs(init_guess[0]))
                th01 = np.random.normal(init_guess[1], 2 * np.abs(init_guess[1]))
                th0 = (th00, th01)
            else:
                th0 = (np.random.normal(init_guess[0], 2 * np.abs(init_guess[0])),)
            # Find optimum
            with np.errstate(invalid="raise", divide="raise"):
                try:
                    th_opt = minimize(
                        neglogL, th0, (X_flat, Y_flat, n_flat), method="BFGS", jac=jac,
                    )
                except FloatingPointError:
                    continue
            if th_opt.success:
                init_guess = th_opt.x  # Update guess
                hess_opt = hess(th_opt.x, X_flat, Y_flat, n_flat)
                maxL = -th_opt.fun
                det = np.linalg.det(hess_opt / (2 * np.pi))
                if det > 0:
                    invdetsqrt = -np.log(det) / 2
                    return (init_guess, maxL + invdetsqrt)
                else:
                    continue
        else:
            # After running all attempts, still not return, then None
            return (None, None)

    def _find_from_known_s(self):
        """internal: calculate evidence of a segment when std is provided or estimated.

        Raises
        ------
        ValueError
            when the length of longest segment is smaller than the minlen.

        """

        X, Y, std, intercept, start, end, minlen = (
            self.x,
            self.y,
            self.std,
            self.intercept,
            self.start,
            self.end,
            self.minlen,
        )
        logL = mc(intercept)
        if end - start <= minlen:
            raise ValueError(f"(end - start) must be no less than {minlen}.")
        evi = [
            logL(X[start : start + n], Y[start : start + n], std[start : start + n], n)
            for n in range(minlen, end + 1 - start)
        ]
        return evi

    def find_from(self):
        """Calculate the evidence of a segment from a fixed start specified in self.start.

        Examples
        --------
        to calculate evidence for each possible segment starting from `x[15]`.

        >>> from findlinear.findlinear import findlinear
        >>> fl = findlinear(x, y, start=15)
        >>> fl.find_from()

        """
        if self.std is not None:
            evi = self._find_from_known_s()
        else:
            evi = self._find_from_unknown_s()
        # normalise to the longest segment and return
        evi = evi - evi[-1]
        self.evidence["find from"] = evi
        self.lastrun = "from"
        return evi

    def find_all(self):
        """Calculate evidence for each possible segment between start and end.

        Examples
        --------
        To calculate evidence for each possible segment:

        >>> from findlinear.findlinear import findlinear
        >>> fl = findlinear(x, y)
        >>> fl.find_all()

        One can calculate over a subset of data; note that `end` is inclusive

        >>> fl = findlinear(x, y, start=5, end=20)
        >>> # this loads data of `x[5:21]`, because `end` is inclusive
        >>> fl.find_all()

        """
        X, Y, std, intercept, start, end, minlen = (
            self.x,
            self.y,
            self.std,
            self.intercept,
            self.start,
            self.end,
            self.minlen,
        )
        # Matrix to record results
        results = np.empty((len(X), len(X)))
        results.fill(np.nan)
        if self.std is None:
            init_guess = self._get_init_guess()
            funcs = mc_t(intercept)
        else:
            logL = mc(intercept)
        # calculate evidence
        if self.std is None:
            warning("Std is not estimated or provided. If slow, try find_through().")
            for st in range(start, end - minlen):
                for ed in range(st + minlen, end + 1):  # confirm?
                    # Run calculation and update init_guess
                    init_guess, evi = self._cal_evidence_unknown_s(
                        st, ed, init_guess, funcs
                    )
                    if evi is None:
                        continue
                    else:
                        results[st, ed - 1] = evi
        else:
            for st in range(start, end - minlen):
                for ed in range(st + minlen, end + 1):  # confirm?
                    evi = logL(X[st:ed], Y[st:ed], std[st:ed], ed - st)
                    results[st, ed - 1] = evi  # must be (end - 1)?
        # Normalise to start:end
        results = results - results[start, end - 1]
        self.evidence["find all"] = results
        self.lastrun = "all"
        return results

    def find_through(self, through):
        """Calculate evidence for each possible segment that passes through a point.

        Parameters
        ----------
        through : int
            index of the point that the segment should pass through.

        Raises
        ------
        ValueError
            if start < through < end is not satified.

        Examples
        --------
        To calculate evidence for each possible segment containing `x[15]`

        >>> from findlinear.findlinear import findlinear
        >>> fl = findlinear(x, y)
        >>> fl.find_through(through=15)

        One can calculate over a subset of data; note that `end` is inclusive

        >>> fl = findlinear(x, y, start=5, end=30)
        >>> # this loads data of `x[5:31]`, because `end` is inclusive
        >>> fl.find_through(through=15)

        """
        X, Y, std, intercept, start, end, minlen = (
            self.x,
            self.y,
            self.std,
            self.intercept,
            self.start,
            self.end,
            self.minlen,
        )
        if through <= start or through >= end:
            raise ValueError(
                f"through must be between start = {start} and end = {end} (exclusive)."
            )
        # Matrix to record results
        results = np.empty((len(X), len(X)))
        results.fill(np.nan)
        if self.std is None:
            init_guess = self._get_init_guess()
            funcs = mc_t(intercept)
        else:
            logL = mc(intercept)
        # calculate evidence
        if self.std is None:
            warning(
                "Std is not estimated or provided. If slow, estimate std if possible."
            )
            for st in range(start, min(through, end - minlen)):
                for ed in range(max(st + minlen, through + 1), end + 1):  # confirm?
                    # Run calculation and update init_guess
                    init_guess, evi = self._cal_evidence_unknown_s(
                        st, ed, init_guess, funcs
                    )
                    if evi is None:
                        continue
                    else:
                        results[st, ed - 1] = evi
        else:
            for st in range(start, min(through, end - minlen)):
                for ed in range(max(st + minlen, through + 1), end + 1):  # confirm?
                    evi = logL(X[st:ed], Y[st:ed], std[st:ed], ed - st)
                    results[st, ed - 1] = evi  # must be (end - 1)?
        # Normalise to start:end
        results = results - results[start, end - 1]
        self.evidence["find through"] = results
        self.through = through
        self.lastrun = "through"
        return results

    def plot(self, result=None, figsize=(6, 5), **kwargs):
        """Plot the evidence for all calcuated fragments.

        Parameters
        ----------
        result : {"from", "all", "through"}, optional
            result to be plotted; default plotting the latest result.

        figsize : tuple, default (6, 5)
            figsize passed on to `matplotlib.pyplot.figure`.

        kwargs :
            keyword arguments to be passed to `matplotlib.axes.Axes.plot`
            when result="from", otherwise `matplotlib.axes.Axes.imshow`.

        Examples
        --------
        `plot` returns both the figure and axes, enabling users to customise them

        >>> from findlinear.findlinear import findlinear
        >>> fl = findlinear(x, y)
        >>> fl.find_from()
        >>> fig, ax = fl.plot()
        >>> ax.set_ylim(200,)

        `plot` also accepts `kwargs` to be passed to `plot` or `imshow` in Matplotlib.

        >>> fl.find_through(through=20)
        >>> fig, ax = fl.plot(vmin=100, vmax=500)

        """
        if not result:
            result = self.lastrun
        res = self.evidence[f"find {result}"]
        if res is None:
            raise ValueError(
                f"cannot find the result. Please run find_{result}() first."
            )
        if result == "from":
            fig, ax = plt.subplots(figsize=figsize)
            xmin = self.start + self.minlen - 1
            x = self.X[xmin : xmin + len(res)]
            ax.plot(x, res, **kwargs)
            ax.set_xlabel("x")
            ax.set_ylabel("relative log evidence")
            return fig, ax
        elif result in ["all", "through"]:
            fig = plt.figure(constrained_layout=True, figsize=figsize)
            # create three axes
            gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4),)
            ax = fig.add_subplot(gs[1, 0])
            ax_mgx = fig.add_subplot(gs[0, 0], sharex=ax)
            ax_mgy = fig.add_subplot(gs[1, 1], sharey=ax)
            # calculate marginal
            res_norm = np.exp(res - np.nanmax(res))
            mgx = np.nansum(res_norm, axis=0) / np.sum(~np.isnan(res_norm), axis=0)
            mgy = np.nansum(res_norm, axis=1) / np.sum(~np.isnan(res_norm), axis=1)
            img = ax.imshow(res, origin="lower", aspect="auto", **kwargs)
            fig.colorbar(img, ax=ax, location="left", use_gridspec=True)
            ax.set_ylabel("index of start")
            ax.set_xlabel("index of end")
            ax_mgx.plot(mgx)
            ax_mgx.xaxis.set_tick_params(labelbottom=False)
            ax_mgy.plot(mgy, range(len(mgy)))
            ax_mgy.yaxis.set_tick_params(labelleft=False)
            axes = [ax, ax_mgx, ax_mgy]
            return fig, axes
        else:
            return None

    def get_argmax(self, result=None):
        """Get the indices of the start and the end of the linear segment.

        Parameters
        ----------
        result : {"from", "all", "through"}, optional
            result to be handled; default the latest result.

        Raises
        ------
        ValueError
            if the corresponding result does not exist yet.

        """
        if not result:
            result = self.lastrun
        res = self.evidence[f"find {result}"]
        if res is None:
            raise ValueError(
                f"cannot find the result. Please run find_{result}() first."
            )
        if result == "from":
            ind = np.nanargmax(res)
            xmin = self.start + self.minlen - 1
            return (self.start, xmin + ind)
        else:
            ind = np.unravel_index(np.nanargmax(res), res.shape)
            return ind

    @staticmethod
    def _run_regression(row, x, y):
        """internal: run regression onto the find_peaks dataframe

        Parameters
        ----------
        row : pandas.Series
            a row of find_peaks dataframe
        x : numpy.array
            self.x
        y : numpy.array
            self.y

        """
        end = int(row["y"])
        start = int(row["x"])
        X = x[start : end + 1]
        Y = y[start : end + 1]
        lin_res = linregress(X, Y)
        row["slope"] = lin_res.slope
        row["intercept"] = lin_res.intercept
        row["rsquare"] = lin_res.rvalue ** 2
        row["x range"] = (x[start], x[end])
        row["y range"] = (y[start], y[end])
        return row

    @staticmethod
    def _get_evidence(row, res, result):
        """internal: get log evidence from result matrix to add to the find_peaks dataframe.

        Parameters
        ----------
        row : pandas.Series
            a row of find_peaks dataframe
        res : numpy.array
            a value of self.evidence

        """
        end = int(row["y"])
        start = int(row["x"])
        if result == "from":
            return res[end]
        else:
            return res[start, end]

    def get_peaks(self, result=None):
        """Get all the local peaks of evidence.

        Parameters
        ----------
        result : {"from", "all", "through"}, optional
            result to be handled; default the latest result.

        Raises
        ------
        ValueError
            if the corresponding result does not exist yet.

        Examples
        --------
        >>> from findlinear.findlinear import findlinear
        >>> fl = findlinear(x, y)
        >>> fl.find_through(through=15)
        >>> fl.get_peaks()

        """
        if not result:
            result = self.lastrun
        res = self.evidence[f"find {result}"]
        if res is None:
            raise ValueError(
                f"cannot find the result. Please run find_{result}() first."
            )
        fp = findpeaks(
            method="topology", whitelist="peak", denoise=None, togray=False, scale=False
        )
        # replace nan with -inf to get findpeaks working.
        res[np.isnan(res)] = -np.inf
        fp_results = fp.fit(res.T)
        X, Y = self.x, self.y
        if Y.ndim > 1:
            # flatten
            X = np.append([], [X] * Y.shape[0])
            Y = Y.flatten(order="C")
        fp_df = (
            fp_results["persistence"]
            .dropna()
            .apply(self._run_regression, x=X, y=Y, axis=1)
            .sort_values(by="score", ascending=False)
            .reset_index(drop=True)
        )
        fp_df["log evidence"] = fp_df.apply(
            self._get_evidence, res=res, result=result, axis=1
        )
        self.peaks = (result, fp_df)
        return fp_df


def get_example_data(plot=False):
    """Return example data, with x being cell number and y being three replicates of OD measurement.

    Parameters
    ----------
    plot : bool, default False
        If true, plot the example data.

    Examples
    --------
    >>> from findlinear.findlinear import get_example_data
    >>> x, y = get_example_data()
    """
    x, y = return_data()
    if plot:
        fig, ax = plt.subplots()
        for j in range(y.shape[0]):
            ax.scatter(x, y[j, :], alpha=0.7)
        ax.set_xlabel("cell number")
        ax.set_ylabel("optical density (OD)")
        plt.plot()
    return x, y
