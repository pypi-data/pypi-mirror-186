# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import aesara.tensor as at
from pymc import (
    Binomial,
    Deterministic,
    HalfNormal,
    Model,
    Multinomial,
    Normal,
    math,
    sample,
)


def phi(x):
    """Cumulative normal distribution"""
    return 0.5 + 0.5 * at.erf(x / at.sqrt(2))


def hmetad_subjectLevel(
    data, sample_model=True, num_samples: int = 1000, num_chains: int = 4, **kwargs
):
    """Hierachical Bayesian modeling of meta-d' (subject level).

    This is an internal function. The subject level model must be
    called using :py:func:`metadpy.bayesian.hmetad`.

    Parameters
    ----------
    data : dict
        Response data.
    sample_model : boolean
        If `False`, only the model is returned without sampling.
    num_samples : int
        The number of samples per chains to draw (defaults to `1000`).
    num_chains : int
        The number of chains (defaults to `4`).
    **kwargs : keyword arguments
        All keyword arguments are passed to `func::pymc.sampling.sample`.

    Returns
    -------
    model : :py:class:`pymc.Model` instance
        The pymc model. Encapsulates the variables and likelihood factors.
    trace : :py:class:`pymc.backends.base.MultiTrace` or
        :py:class:`arviz.InferenceData`
        A `MultiTrace` or `ArviZ InferenceData` object that contains the
        samples.

    References
    ----------
    .. [#] Fleming, S.M. (2017) HMeta-d: hierarchical Bayesian estimation
    of metacognitive efficiency from confidence ratings, Neuroscience of
    Consciousness, 3(1) nix007, https://doi.org/10.1093/nc/nix007
    """
    nRatings = data["nratings"]
    with Model() as model:

        # Type 1 priors
        c1 = Normal("c1", mu=0.0, tau=2)
        d1 = Normal("d1", mu=0.0, tau=0.5)

        # TYPE 1 SDT BINOMIAL MODEL
        h = phi(d1 / 2 - c1)
        f = phi(-d1 / 2 - c1)
        H = Binomial("H", n=data["S"], p=h, observed=data["H"])
        FA = Binomial("FA", n=data["N"], p=f, observed=data["FA"])

        # Type 2 priors
        meta_d = Normal("meta_d", mu=d1, tau=2)

        # Specify ordered prior on criteria
        # bounded above and below by Type 1 c1
        cS1_hn = HalfNormal(
            "cS1_hn",
            tau=2,
            shape=nRatings - 1,
        )
        cS1 = Deterministic("cS1", at.sort(-cS1_hn) + (c1 - data["Tol"]))

        cS2_hn = HalfNormal(
            "cS2_hn",
            tau=2,
            shape=nRatings - 1,
        )
        cS2 = Deterministic("cS2", at.sort(cS2_hn) + (c1 - data["Tol"]))

        # Means of SDT distributions
        S2mu = Deterministic("S2mu", meta_d / 2)
        S1mu = Deterministic("S1mu", -meta_d / 2)

        # Calculate normalisation constants
        C_area_rS1 = phi(c1 - S1mu)
        I_area_rS1 = phi(c1 - S2mu)
        C_area_rS2 = 1 - phi(c1 - S2mu)
        I_area_rS2 = 1 - phi(c1 - S1mu)

        # Get nC_rS1 probs
        nC_rS1 = phi(cS1 - S1mu) / C_area_rS1
        nC_rS1 = Deterministic(
            "nC_rS1",
            math.concatenate(
                (
                    [
                        phi(cS1[0] - S1mu) / C_area_rS1,
                        nC_rS1[1:] - nC_rS1[:-1],
                        (
                            (phi(c1 - S1mu) - phi(cS1[(nRatings - 2)] - S1mu))
                            / C_area_rS1
                        ),
                    ]
                ),
                axis=0,
            ),
        )

        # Get nI_rS2 probs
        nI_rS2 = (1 - phi(cS2 - S1mu)) / I_area_rS2
        nI_rS2 = Deterministic(
            "nI_rS2",
            math.concatenate(
                (
                    [
                        ((1 - phi(c1 - S1mu)) - (1 - phi(cS2[0] - S1mu))) / I_area_rS2,
                        nI_rS2[:-1] - (1 - phi(cS2[1:] - S1mu)) / I_area_rS2,
                        (1 - phi(cS2[nRatings - 2] - S1mu)) / I_area_rS2,
                    ]
                ),
                axis=0,
            ),
        )

        # Get nI_rS1 probs
        nI_rS1 = (-phi(cS1 - S2mu)) / I_area_rS1
        nI_rS1 = Deterministic(
            "nI_rS1",
            math.concatenate(
                (
                    [
                        phi(cS1[0] - S2mu) / I_area_rS1,
                        nI_rS1[:-1] + (phi(cS1[1:] - S2mu)) / I_area_rS1,
                        (phi(c1 - S2mu) - phi(cS1[(nRatings - 2)] - S2mu)) / I_area_rS1,
                    ]
                ),
                axis=0,
            ),
        )

        # Get nC_rS2 probs
        nC_rS2 = (1 - phi(cS2 - S2mu)) / C_area_rS2
        nC_rS2 = Deterministic(
            "nC_rS2",
            math.concatenate(
                (
                    [
                        ((1 - phi(c1 - S2mu)) - (1 - phi(cS2[0] - S2mu))) / C_area_rS2,
                        nC_rS2[:-1] - ((1 - phi(cS2[1:] - S2mu)) / C_area_rS2),
                        (1 - phi(cS2[nRatings - 2] - S2mu)) / C_area_rS2,
                    ]
                ),
                axis=0,
            ),
        )

        # Avoid underflow of probabilities
        nC_rS1 = math.switch(nC_rS1 < data["Tol"], data["Tol"], nC_rS1)
        nI_rS2 = math.switch(nI_rS2 < data["Tol"], data["Tol"], nI_rS2)
        nI_rS1 = math.switch(nI_rS1 < data["Tol"], data["Tol"], nI_rS1)
        nC_rS2 = math.switch(nC_rS2 < data["Tol"], data["Tol"], nC_rS2)

        # TYPE 2 SDT MODEL (META-D)
        # Multinomial likelihood for response counts ordered as c(nR_S1,nR_S2)
        Multinomial(
            "CR_counts",
            n=data["CR"],
            p=nC_rS1,
            shape=nRatings,
            observed=data["counts"][:nRatings],
        )
        Multinomial(
            "FA_counts",
            n=FA,
            p=nI_rS2,
            shape=nRatings,
            observed=data["counts"][nRatings : nRatings * 2],
        )
        Multinomial(
            "M_counts",
            n=data["M"],
            p=nI_rS1,
            shape=nRatings,
            observed=data["counts"][nRatings * 2 : nRatings * 3],
        )
        Multinomial(
            "H_counts",
            n=H,
            p=nC_rS2,
            shape=nRatings,
            observed=data["counts"][nRatings * 3 : nRatings * 4],
        )

        if sample_model is True:
            trace = sample(
                trace=[meta_d, cS1, cS2],
                return_inferencedata=True,
                chains=num_chains,
                draws=num_samples,
                **kwargs
            )

            return model, trace

        else:
            return model


import unittest
from unittest import TestCase

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm
import pytest

from metadpy import load_dataset
from metadpy.bayesian import extractParameters, hmetad

model, _ = hmetad(
    nR_S1=np.array([52, 32, 35, 37, 26, 12, 4, 2]),
    nR_S2=np.array([2, 5, 15, 22, 33, 38, 40, 45]),
    nRatings=4,
    sample_model=False,
    backend="pymc",
)

pm.model_to_graphviz(model)


_, trace = hmetad(
    nR_S1=np.array([52, 32, 35, 37, 26, 12, 4, 2]),
    nR_S2=np.array([2, 5, 15, 22, 33, 38, 40, 45]),
    nRatings=4,
    sample_model=True,
    backend="pymc",
)


az.plot_trace(trace)
plt.tight_layout()

_, trace_numpyro = hmetad(
    nR_S1=np.array([52, 32, 35, 37, 26, 12, 4, 2]),
    nR_S2=np.array([2, 5, 15, 22, 33, 38, 40, 45]),
    nRatings=4,
    sample_model=True,
    backend="numpyro",
)
az.plot_trace(trace_numpyro)


from metadpy.bayesian import extractParameters

data = extractParameters(
    nR_S1=np.array([52, 32, 35, 37, 26, 12, 4, 2]),
    nR_S2=np.array([2, 5, 15, 22, 33, 38, 40, 45]),
)


def phi(x):
    """Cumulative normal distribution"""
    return 0.5 + 0.5 * math.erf(x / math.sqrt(2))


x = at.dscalar("x")
y = at.dscalar("y")

# Create a simple example expression
y = 0.5 + 0.5 * at.erf(x / at.sqrt(2))


# Convert the expression into a callable object that takes `(a, b)`
# values as input and computes the value of `c`.
phi = aesara.function([x], y)
f_c(1.5)

with pm.Model() as model:
    slopes = pm.Bound(
        "slopes",
        pm.Normal.dist(0, 5),
        lower=0.0,
        shape=4,
        initval=[1, 2, 3, 4],
        transform=pm.distributions.transforms.ordered,
    )

    trace = sample(
        return_inferencedata=True,
    )


az.plot_trace(trace)


import numpy as np
from pymc3 import (
    Binomial,
    Deterministic,
    HalfNormal,
    Model,
    Multinomial,
    Normal,
    math,
    sample,
)


def phi(x):
    """Cumulative normal distribution"""
    return 0.5 + 0.5 * math.erf(x / math.sqrt(2))


nRatings = data["nratings"]
with Model() as model:

    # Type 1 priors
    c1 = Normal("c1", mu=0.0, tau=2)
    d1 = Normal("d1", mu=0.0, tau=0.5)

    # TYPE 1 SDT BINOMIAL MODEL
    h = phi(d1 / 2 - c1)
    f = phi(-d1 / 2 - c1)
    H = Binomial("H", data["S"], h, observed=data["H"])
    FA = Binomial("FA", data["N"], f, observed=data["FA"])

    # Type 2 priors
    meta_d = Normal("meta_d", mu=d1, tau=2)

    # Specify ordered prior on criteria
    # bounded above and below by Type 1 c1
    cS1_hn = HalfNormal(
        "cS1_hn",
        tau=2,
        shape=nRatings - 1,
        testval=np.linspace(1.5, 0.5, nRatings - 1),
    )
    cS1 = Deterministic("cS1", -cS1_hn + (c1 - data["Tol"]))

    cS2_hn = HalfNormal(
        "cS2_hn",
        tau=2,
        shape=nRatings - 1,
        testval=np.linspace(0.5, 1.5, nRatings - 1),
    )
    cS2 = Deterministic("cS2", cS2_hn + (c1 - data["Tol"]))

    # Means of SDT distributions
    S2mu = math.flatten(meta_d / 2, 1)
    S1mu = math.flatten(-meta_d / 2, 1)

    # Calculate normalisation constants
    C_area_rS1 = phi(c1 - S1mu)
    I_area_rS1 = phi(c1 - S2mu)
    C_area_rS2 = 1 - phi(c1 - S2mu)
    I_area_rS2 = 1 - phi(c1 - S1mu)

    # Get nC_rS1 probs
    nC_rS1 = phi(cS1 - S1mu) / C_area_rS1
    nC_rS1 = Deterministic(
        "nC_rS1",
        math.concatenate(
            (
                [
                    phi(cS1[0] - S1mu) / C_area_rS1,
                    nC_rS1[1:] - nC_rS1[:-1],
                    ((phi(c1 - S1mu) - phi(cS1[(nRatings - 2)] - S1mu)) / C_area_rS1),
                ]
            ),
            axis=0,
        ),
    )

    # Get nI_rS2 probs
    nI_rS2 = (1 - phi(cS2 - S1mu)) / I_area_rS2
    nI_rS2 = Deterministic(
        "nI_rS2",
        math.concatenate(
            (
                [
                    ((1 - phi(c1 - S1mu)) - (1 - phi(cS2[0] - S1mu))) / I_area_rS2,
                    nI_rS2[:-1] - (1 - phi(cS2[1:] - S1mu)) / I_area_rS2,
                    (1 - phi(cS2[nRatings - 2] - S1mu)) / I_area_rS2,
                ]
            ),
            axis=0,
        ),
    )

    # Get nI_rS1 probs
    nI_rS1 = (-phi(cS1 - S2mu)) / I_area_rS1
    nI_rS1 = Deterministic(
        "nI_rS1",
        math.concatenate(
            (
                [
                    phi(cS1[0] - S2mu) / I_area_rS1,
                    nI_rS1[:-1] + (phi(cS1[1:] - S2mu)) / I_area_rS1,
                    (phi(c1 - S2mu) - phi(cS1[(nRatings - 2)] - S2mu)) / I_area_rS1,
                ]
            ),
            axis=0,
        ),
    )

    # Get nC_rS2 probs
    nC_rS2 = (1 - phi(cS2 - S2mu)) / C_area_rS2
    nC_rS2 = Deterministic(
        "nC_rS2",
        math.concatenate(
            (
                [
                    ((1 - phi(c1 - S2mu)) - (1 - phi(cS2[0] - S2mu))) / C_area_rS2,
                    nC_rS2[:-1] - ((1 - phi(cS2[1:] - S2mu)) / C_area_rS2),
                    (1 - phi(cS2[nRatings - 2] - S2mu)) / C_area_rS2,
                ]
            ),
            axis=0,
        ),
    )

    # Avoid underflow of probabilities
    nC_rS1 = math.switch(nC_rS1 < data["Tol"], data["Tol"], nC_rS1)
    nI_rS2 = math.switch(nI_rS2 < data["Tol"], data["Tol"], nI_rS2)
    nI_rS1 = math.switch(nI_rS1 < data["Tol"], data["Tol"], nI_rS1)
    nC_rS2 = math.switch(nC_rS2 < data["Tol"], data["Tol"], nC_rS2)

    # TYPE 2 SDT MODEL (META-D)
    # Multinomial likelihood for response counts ordered as c(nR_S1,nR_S2)
    Multinomial(
        "CR_counts",
        data["CR"],
        nC_rS1,
        shape=nRatings,
        observed=data["counts"][:nRatings],
    )
    Multinomial(
        "FA_counts",
        FA,
        nI_rS2,
        shape=nRatings,
        observed=data["counts"][nRatings : nRatings * 2],
    )
    Multinomial(
        "M_counts",
        data["M"],
        nI_rS1,
        shape=nRatings,
        observed=data["counts"][nRatings * 2 : nRatings * 3],
    )
    Multinomial(
        "H_counts",
        H,
        nC_rS2,
        shape=nRatings,
        observed=data["counts"][nRatings * 3 : nRatings * 4],
    )


with model:
    trace = sample(
        return_inferencedata=True,
    )


az.plot_trace(trace)
