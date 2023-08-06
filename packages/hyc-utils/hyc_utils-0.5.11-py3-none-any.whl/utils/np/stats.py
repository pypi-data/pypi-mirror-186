import numpy as np
import numpy.ma as ma
from scipy import stats as spstats

__all__ = [
    'mean',
    'nanmean',
    'std',
    'nanstd',
    'var',
    'nanvar',
    'sem',
    'nansem',
    'count',
    'nancount',
    'cov',
    'nancov',
    'corrcoef',
    'nancorrcoef',
    'meanerr',
    'nanmeanerr',
]

mean = np.mean
nanmean = np.nanmean

def std(x, ddof=1, **kwargs):
    return np.std(x, ddof=ddof, **kwargs)

def nanstd(x, ddof=1, **kwargs):
    return np.nanstd(x, ddof=ddof, **kwargs)

def var(x, ddof=1, **kwargs):
    return np.var(x, ddof=ddof, **kwargs)

def nanvar(x, ddof=1, **kwargs):
    return np.nanvar(x, ddof=ddof, **kwargs)
    
def sem(x, axis=None, ddof=1, **kwargs):
    return std(x, axis=axis, ddof=ddof, **kwargs) / count(x, axis=axis)**0.5
    # return spstats.sem(x, axis=axis, ddof=ddof)

def nansem(x, axis=None, ddof=1, **kwargs):
    return nanstd(x, axis=axis, ddof=ddof, **kwargs) / nancount(x, axis=axis)**0.5
    # return spstats.sem(x, axis=axis, ddof=ddof, nan_policy='omit')
    
def count(x, axis=None):
    return np.sum(np.ones(x.shape, dtype=int), axis=axis)

def nancount(x, axis=None):
    return np.sum(~np.isnan(x), axis=axis)
    
cov = np.cov # by default, np.cov uses Bessel correction, in contrast to the rest of its stats functions
    
def nancov(x, y=None, **kwargs):
    x = ma.masked_where(np.isnan(x), x)
    if y is not None:
        y = ma.masked_where(np.isnan(y), y)
    return ma.cov(x, y=y, **kwargs)
    
corrcoef = np.corrcoef

def nancorrcoef(x, y=None, **kwargs):
    x = ma.masked_where(np.isnan(x), x)
    if y is not None:
        y = ma.masked_where(np.isnan(y), y)
    return ma.corrcoef(x, y=y, **kwargs)

def meanerr(y, yerr, axis=None):
    assert y.shape == yerr.shape
    
    y = np.mean(y, axis=axis)
    yerr = np.sum(yerr**2, axis=axis)**0.5/count(yerr, axis=axis)
        
    return y, yerr

def nanmeanerr(y, yerr, axis=None):
    assert y.shape == yerr.shape
    
    nans = np.isnan(y) | np.isnan(yerr)
    y, yerr = y.copy(), yerr.copy()
    y[nans] = np.nan
    yerr[nans] = np.nan

    y = np.nanmean(y, axis=axis)
    yerr = np.nansum(yerr**2, axis=axis)**0.5/nancount(yerr, axis=axis)
        
    return y, yerr