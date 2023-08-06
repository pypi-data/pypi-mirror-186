"""
The `checker` module provides tools to check exact and approximate equality.
:author: András Aszódi
:date: 2023-01-18
"""

import math
import numbers
import unittest

# -- Classes --

class AlmostEqual:
    """
    Provides equality comparisons with the added twist
    that `float` values are approximately compared.
    """
    
    def __init__(self, rel_tol=1e-9):
        """
        Sets up an AlmostEqual instance.
        :param rel_tol: The relative tolerance to be used
            in comparing floats. See `math.isclose()`.
        """
        self._tol = math.fabs(rel_tol)
    
    def compare(self, expval, obsval):
        """
        Compares two values. The type of comparison
        depends on the type of `expval`. If it is a "composite type"
        (e.g. list, dict, etc.) then element-wise comparison is performed.
        "Simple types" are compared directly except for float-s
        which are approximately compared using `math.isclose()`.
        :param expval: The "expected value"
        :param obsval: The "observed value" which is supposed to be close to `expval`
        :return: `True` if the values are "close", `False` otherwise.
        """
        
        # Note: only the "most important" cases are covered
        # Warning: the composite type comparisons "recursively" invoke `compare()`!
        if isinstance(expval, dict):
            return self._compare_dicts(expval, obsval)
        elif isinstance(expval, (list, tuple,)):
            return self._compare_lists(expval, obsval)
        elif isinstance(expval, set) or isinstance(expval, frozenset):
            return self._compare_sets(expval, obsval)
        else:
            return self._compare_simple(expval, obsval)

    # -- "hidden" methods --
    
    def _compare_dicts(self, expd, obsd):
        """
        Compares two dictionaries.
        We _assume_ that the dictionary keys are "simple types"
        and no one in his right mind would use floats as keys.
        The values, however, may be composite types.
        :param expd: The "expected" dictionary
        :param obsd: The "observed" dictionary which is supposed to be close to `expd`
        :return: `True` if the values are "close", `False` otherwise.
        """
        if not isinstance(obsd, dict) or len(expd) != len(obsd):
            # don't bother
            return False
        for key in expd:
            try:
                expv = expd[key]
                obsv = obsd[key]
                return self.compare(expv, obsv) # recursion here
            except KeyError:
                return False
        
    def _compare_lists(self, expl, obsl):
        """
        Compares two lists or tuples.
        The elements may be composite types which are then recursively compared.
        Order matters.
        :param expl: The "expected" list/tuple
        :param obsl: The "observed" list/tuple which is supposed to be close to `expl`
        :return: `True` if the values are "close", `False` otherwise.
        """
        if not isinstance(obsl, (list,tuple)) or len(expl) != len(obsl):
            # don't bother
            return False
        for e1, e2 in zip(expl, obsl):
            if not self.compare(e1, e2):
                return False
        return True
        
    def _compare_sets(self, exps, obss):
        """
        Compares two sets and/or frozensets.
        The elements may be composite types which are then recursively compared.
        Order (obviously) doesn't matter.
        :param exps: The "expected" set
        :param obss: The "observed" set which is supposed to be close to `exps`
        :return: `True` if the values are "close", `False` otherwise.
        """
        if not isinstance(obss, (set,frozenset)) or len(exps) != len(obss):
            # don't bother
            return False
        return self._compare_lists(sorted(list(exps)), sorted(list(obss)))
    
    def _compare_simple(self, expval, obsval):
        """
        Compares two "simple type" (i.e. not composite) values. 
        "Simple types" are compared directly except for float-s
        which are approximately compared using `math.isclose()`.
        :param expval: The "expected value"
        :param obsval: The "observed value" which is supposed to be close to `expval`
        :return: `True` if the values are "close", `False` otherwise.
        """
        if expval is None:
            return obsval is None
        if isinstance(expval, float):
            try:
                return math.isclose(expval, obsval, rel_tol=self._tol)
            except TypeError:
                # `obsval` was not a float
                return False
        if isinstance(expval, str):
            try:
                unittest.TestCase().assertMultiLineEqual(expval, obsval)
                return True
            except AssertionError:
                return False
        # otherwise...
        return expval == obsval