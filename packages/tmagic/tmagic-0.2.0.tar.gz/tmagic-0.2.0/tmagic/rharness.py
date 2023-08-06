"""
Module providing the R language exercise harness class 'RHarness'.
:author: András Aszódi
:date: 2022-08-25
"""
import re

import rpy2.robjects
from IPython.core.getipython import get_ipython

from .harness import Harness

class RHarness(Harness):
    """
    This class runs R code from an IPython cell
    and check its result.
    """

    @classmethod
    def _setup_ipython(cls):
        """
        Creates a class variable that points to the current IPython instance.
        As a side effect, loads the "rpy2" IPython extensions as well.
        """
        cls.IPYTHON = get_ipython()
        if cls.IPYTHON is not None:
            cls.IPYTHON.run_line_magic("load_ext", "rpy2.ipython")

    def __init__(self):
        """
        Creates an RHarness instance.
        """
        super().__init__()
        # any other setup
        pass

    # -- "hidden" --

    def _exec_script(self, script):
        """
        Executes an R script and returns the value of the last expression,
        or None if the last command was not an expression.
        :param script: R code as a possibly multi-line string.
        :return: The value of the last expression seen, or None
        """
        if self.IPYTHON is None:
            # cannot do anything
            # maybe raise an exception?
            return None
        try:
            # The %%R cell magic always returns None, we need %R line magic
            # and convert the multi-line `script` to a one-liner on the R side
            charvec = RHarness._rlines_to_charvec(script)
            if charvec is None:
                return None
            oneliner = f"eval(parse(text={charvec}))"
            result = self.IPYTHON.run_line_magic("R", oneliner)
            return result
        except rpy2.rinterface_lib._rinterface_capi.RParsingError:
            raise ValueError(f"R could not parse \"{oneliner}\"")
        except (KeyboardInterrupt, SystemExit):
            pass    # ignore them silently

    @staticmethod
    def _rlines_to_charvec(script):
        """
        Convert the multi-line string `script` to the string representation
        of an R character vector whose elements are the original lines.
        This can be passed to an `eval(parse(text=...))` construct
        which will be run by the Rpy2 `%R` line magic in `_exec_script`.
        :param script: A multi-line string containing R code
        :return: R code for a character vector containing the lines to be parsed
            or None if no R code lines were found.
        """
        # Break `script` up into its constituent lines,
        # surround them with "-s, skip empty and whitespace-only lines
        def _quote(c):
            cq = c.replace(r'"', r'\"')
            return f'"{cq}"'

        lines = [_quote(c) for c in script.split('\n') if len(c) > 0 and not re.match(r"^[ \t]+$", c)]
        if len(lines) == 0:
            return None
        if len(lines) == 1:
            return lines[0]
        charvec = "c(" + ",".join(lines) + ")"
        return charvec

    def _check(self, expval):
        """
        Checks self._last against the expected value,
        using the comparisons implemented in the `AlmostEqual` class.
        Has the side effect of overwriting `self._last`
        with a standard Python data type instead of an RPy2 object.
        :param expval: The expected (correct) result of the test.
        :return: True if the check passed, False if failed.
        """
        # the "observed" value may be the instance of an RPy2 data structure
        # which we convert to bona fide Python types and save "back" in `self._last`
        rval = self._last
        if isinstance(rval, rpy2.robjects.DataFrame):
            # convert to Python dictionary of lists
            self._last = RHarness._rdataframe_to_pydictlist(rval)
        elif isinstance(rval, rpy2.robjects.vectors.Matrix):
            # convert to Python list of lists [[row1],[row2],...]
            self._last = RHarness._rmatrix_to_pylist(rval)
        elif isinstance(rval, rpy2.robjects.vectors.Vector):
            # R vectors and lists, including "simple variables" which are one-element vectors
            # convert them to Python dicts (possibly recursive), lists or a single variable
            self._last = RHarness._rlistvec_to_pydictlist(rval)
        else:
            # placeholder, we hope we can deal with `self._last`
            pass
        
        # compare
        return self._aeq.compare(expval, self._last)

    @staticmethod
    def _rlistvec_to_pydictlist(rlistvec):
        """
        Converts an R list or vector to a Python dictionary or list recursively.
        :param rlistvec: An instance of rpy2.robjects.vectors.Vector (which includes R lists, i.e. ListVector-s in Rpy2)
        :returns: the corresponding list of lists
        """
        if isinstance(rlistvec, rpy2.robjects.vectors.ListVector):
            # R list. Convert it to a dictionary. The values are obtained with
            # the `rx2` method, this corresponds to the `$` or `[[` operator in R.
            # Note that `ListVector` is a subclass of `Vector`
            # that's why this `if` comes first
            pdict = { name:RHarness._rlistvec_to_pydictlist(rlistvec.rx2(name)) for name in rlistvec.names }
            return pdict
        elif isinstance(rlistvec, rpy2.robjects.vectors.Vector):
            # R vectors. R lists have been handled above
            return rlistvec[0] if len(rlistvec) == 1 else list(rlistvec)
        else:
            return None

    @staticmethod
    def _rmatrix_to_pylist(rmat):
        """
        Converts an R matrix to a Python list of lists
        :param rmat: An instance of rpy2.robjects.vectors.Matrix
        :returns: A Python list of lists, the 2nd level corresponds to the rows
            or None for any other type
        """
        if not isinstance(rmat, rpy2.robjects.vectors.Matrix):
            return None
        pymat = [ list(rmat.rx(rowidx, True)) for rowidx in range(1, rmat.nrow+1) ]
        return pymat

    @staticmethod
    def _rdataframe_to_pydictlist(rdf):
        """
        Converts an R data frame to a Python dictionary of lists (=columns of the data frame).
        :param rdf: An instance of rpy2.robjects.DataFrame
        :returns: A Python dictionary. The keys are the data frame column names,
            the values are the column vectors as lists.
        """
        if not isinstance(rdf, rpy2.robjects.DataFrame):
            return None
        pydl = { colnm:list(rdf.rx2(colnm)) for colnm in rdf.colnames }
        return pydl


# Class initialisation
# sets up IPython
RHarness._setup_ipython()
