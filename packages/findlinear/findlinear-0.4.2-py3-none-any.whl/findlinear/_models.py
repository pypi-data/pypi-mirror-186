#!/usr/bin/env python3
from sympy import (
    IndexedBase,
    log,
    Sum,
    Indexed,
    lambdify,
    gamma,
    simplify,
    hessian,
    symbols,
    Symbol,
    pi,
    diff,
)


def mc_t(intercept):
    """returns functions of the negative log evidence, hessian and jacobian of the y=mx+c model,
    assuming sigma is unknown but constant over x.

    Parameters
    ----------
    intercept : bool
        if False, force c = 0.

    """
    m, N, j, c = symbols("m N j c")
    y = IndexedBase("y")
    x = IndexedBase("x")
    stirling = (
        1 / 2 * log(2 * pi * (N / 2 - 1))
        + (N / 2 - 1) * log(N / 2 - 1)
        - (N / 2 - 1)
        + log(1 + 1 / (12 * (N / 2 - 1)) + 1 / (288 * (N / 2 - 1) ** 2))
    )
    logZ = stirling - log(2) - (N / 2) * log(pi)
    model = m * Indexed(x, j)
    theta = (m,)
    if intercept:
        model = model + c
        theta = (m, c)
    logL = (-N / 2) * log(Sum((Indexed(y, j) - model) ** 2, (j, 0, N - 1)))
    arg_list = (theta, x, y, N)
    neglogL = lambdify(arg_list, -(logL + logZ), modules=["numpy"])
    hess = lambdify(
        arg_list, hessian(-logL, theta), modules=["numpy"]
    )  # No need to add logZ
    # jac = lambdify(arg_list, Matrix([-logL]).jacobian(theta))
    jac = lambdify(arg_list, [diff(-logL, v) for v in theta], modules=["numpy"])
    return neglogL, hess, jac


def mc_t2(intercept):
    """returns functions of the negative log evidence, hessian and jacobian of the y=mx+c model,
    assuming sigma is unknown and not constant over x. Not used in findLinear.

    Parameters
    ----------
    intercept : bool
        if False, force c = 0.

    """
    m, N, j, c = symbols("m N j c")
    k, R = symbols("k R")  # k for y's subscript and R for number of replicates.
    y = IndexedBase("y")
    x = IndexedBase("x")
    logZ = (log(gamma(R / 2)) - log(2) - (R / 2) * log(pi)) * N
    model = m * Indexed(x, j)
    theta = (m,)
    if intercept:
        model = model + c
        theta = (m, c)
    logL = Sum(
        -R / 2 * log(Sum((Indexed(y, k, j) - model) ** 2, (k, 0, R - 1))), (j, 0, N - 1)
    )
    arg_list = (theta, x, y, N, R)
    neglogL = lambdify(arg_list, -(logL + logZ))
    hess = lambdify(arg_list, hessian(-logL, theta))  # No need to add logZ
    return neglogL, hess


def mc_approx(intercept):
    """y = mx+c model with known sigma (approximation). Not used in the main program."""
    m, N, j, c = symbols("m N j c")
    y = IndexedBase("y")
    x = IndexedBase("x")
    sig = IndexedBase("\sigma")
    model = m * Indexed(x, j)
    theta = (m,)
    if intercept:
        model = model + c
        theta = (m, c)
    logL = -Sum(
        (Indexed(y, j) - model) ** 2 / (2 * Indexed(sig, j) ** 2), (j, 0, N - 1)
    )
    logL = simplify(logL)
    arg_list = (theta, x, y, sig, N)
    neglogL = lambdify(arg_list, -logL)
    hess = lambdify(arg_list, hessian(-logL, theta))
    return neglogL, hess


def mc(intercept):
    """returns functions of the negative log evidence of the y=mx+c model assuming known sigma.

    Parameters
    ----------
    intercept : bool
        if False, force c = 0.

    """
    # Define symbols
    x = IndexedBase("x")
    y = IndexedBase("y")
    sig = IndexedBase("\sigma")
    j = Symbol("j")
    N = Symbol("N")
    arg_list = (x, y, sig, N)
    # Define T's
    T1 = Sum(Indexed(y, j) ** 2 / 2 / Indexed(sig, j) ** 2, (j, 0, N - 1))
    T2 = Sum(Indexed(x, j) ** 2 / 2 / Indexed(sig, j) ** 2, (j, 0, N - 1))
    T3 = Sum(1 / 2 / Indexed(sig, j) ** 2, (j, 0, N - 1))
    T4 = Sum(Indexed(y, j) / Indexed(sig, j) ** 2, (j, 0, N - 1))
    T5 = Sum(Indexed(x, j) * Indexed(y, j) / Indexed(sig, j) ** 2, (j, 0, N - 1))
    T6 = Sum(Indexed(x, j) / Indexed(sig, j) ** 2, (j, 0, N - 1))
    # Log likelihood
    if intercept:
        logl = (
            (1 - N / 2) * log(2 * pi)
            - Sum(log(Indexed(sig, j)), (j, 0, N - 1))
            - 1 / 2 * (log(4 * T2 * T3 - T6 ** 2))
            + (
                -4 * T1 * T2
                + T5 ** 2
                + (2 * T2 * T4 - T5 * T6) ** 2 / (4 * T2 * T3 - T6 ** 2)
            )
            / (4 * T2)
        )
    else:
        logl = (
            -N / 2 * log(2 * pi)
            - Sum(log(Indexed(sig, j)), (j, 0, N - 1))
            + 1 / 2 * (log(pi / T2))
            - T1
            + T5 ** 2 / (4 * T2)
        )
    return lambdify(arg_list, logl, modules=["numpy"])
