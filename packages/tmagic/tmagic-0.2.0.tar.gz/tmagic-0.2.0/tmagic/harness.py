"""
Exercise harness infrastructure.
Provides the abstract base class 'Harness'.
:author: András Aszódi
:date: 2020-11-04
"""

from sys import stderr
from abc import ABC, abstractmethod
from code import InteractiveInterpreter

from .checker import AlmostEqual

class Harness(ABC, InteractiveInterpreter):
    """
    This abstract class can be configured to run code from an IPython cell
    and check its result.
    """

    def __init__(self, rel_tol=1e-9):
        """
        Creates a Harness instance.
        :param rel_tol: The relative tolerance to be used
            in comparing floats. See `AlmostEqual.__init__()`.
        """
        # Invoke all base class ctors
        # If there are lots of base classes, then see
        # see https://stackoverflow.com/a/50463991
        ABC.__init__(self)
        # The InteractiveInterpreter parent is initialised with the current local variables
        InteractiveInterpreter.__init__(self, locals())
        self._aeq = AlmostEqual(rel_tol)
        self._last = None

    def test_expr(self, expval, cell):
        """
        This method serves as the back-end of the custom magics in the ExerMagic class.
        It runs the contents of a cell
        and compares the result to an expected value which was registered before.
        :param expval: The expected result of the test. ExerMagic looks this up
            from its internal dictionary.
        :param cell: Possibly multi-line string, the contents of the cell
            decorated with `%%pyexer` or `%%rexer`.
        :return: True if the test passed, False otherwise (including exceptions)
        """
        try:
            # execute the cell's contents
            self._last = self._exec_script(cell)
            # compare result to expected value
            return self._check(expval)
        except Exception as err:
            print(str(err), file=stderr)
            return False

    @property
    def last(self):
        return self._last

    # -- "hidden" methods --

    @abstractmethod
    def _exec_script(self, script):
        """
        Executes a script and returns the value of the last expression,
        or None if the last command was not an expression.
        :param script: Code as a possibly multi-line string.
        :return: The value of the last expression seen, or None
        """
        pass

    @abstractmethod
    def _check(self, expval):
        """
        Checks self._last against the expected value,
        using the comparisons implemented in the `AlmostEqual` class.
        :param expval: The expected (correct) result of the test.
        :return: True if the check passed, False if failed.
        """
        pass

