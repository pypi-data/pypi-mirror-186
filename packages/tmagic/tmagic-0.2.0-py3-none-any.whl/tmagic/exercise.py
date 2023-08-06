"""
This module provides a base class for running exercises in an IPython notebook cell.
:author: András Aszódi
:date: 2020-11-03
"""

# Implementation note: the class is based on the IPython manual
# See https://ipython.readthedocs.io/en/stable/config/custommagics.html

from sys import stderr

from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.getipython import get_ipython

from .pyharness import PyHarness
from .rharness import RHarness

# -- Classes --

@magics_class
class ExerMagic(Magics):
    """
    Defines magics to run a piece of code wrapped in a unit test harness.
    """

    def __init__(self, tests=None):
        """
        Initialiser. Registers the created instance with IPython.
        :param tests: If `None`, then no tests are registered (this is the default).
            If a dictionary containing test name - expected value pairs or the name
            of a JSON file corresponding to such a dictionary, then
            they are registered using the `register_tests()` method.
        """
        # Set up this TestMagic instance as an IPython magic
        super().__init__(None)
        ipython = get_ipython()
        ipython.register_magics(self)

        # Test names and expected values
        self._tests = {}
        self.register_tests(tests)

    def register_test(self, testname, expvalue):
        """
        Registers a test (stores the expected value)
        :param testname: The name of the test
        :param expvalue: The expected value coming from the test
        """
        self._tests[testname] = expvalue

    def register_tests(self, tests):
        """
        Convenience method to register many tests at once.
        Invokes the `register_test()` method on all key-value pairs provided in `tests`
        :param tests: Either a dictionary with test name - expected value pairs,
            or the name of a JSON file from which such a dictionary can be `load`-ed.
        Errors are swallowed silently.
        """
        # local function
        def reg_from_dir(t):
            for testname, expvalue in t.items():
                self.register_test(testname, expvalue)

        try:
            if isinstance(tests, str):
                import json
                with open(tests) as inf:
                    reg_from_dir(json.load(inf))
            elif isinstance(tests, dict):
                reg_from_dir(tests)
            else:
                pass
        except Exception as err:
            print(f"ERROR: {str(err)} in 'register_tests', ignored")

    @cell_magic
    def pyexer(self, testname, cell):
        """
        IPython 'cell magic' to wrap a piece of Python code (sequence of expressions)
        in a unit test harness and have it run.
        Usage within an IPython cell:
        +-------------------------+
        | %%pyexer testname       |
        | Python code line        |
        | ... more code lines ... |
        +-------------------------+

        :param testname: Identifies the test to be used.
        :param cell: Contents of the cell
        :return: The value of the last expression of the cell contents or None
        """
        # Create a PyHarness instance to test the cell's contents
        harness = PyHarness()
        # make sure the harness knows about all the objects from previous cells
        cell = "from __main__ import *\n" + cell
        return self._run_exercise(harness, testname, cell)

    @cell_magic
    def rexer(self, testname, cell):
        """
        IPython 'cell magic' to wrap a piece of R code (sequence of expressions)
        in a unit test harness and have it run.
        Usage within an IPython cell:
        +-------------------------+
        | %%rexer testname        |
        | R code line             |
        | ... more code lines ... |
        +-------------------------+

        :param testname: Identifies the test to be used.
        :param cell: Contents of the cell
        :return: The value of the last expression of the cell contents or None
        """
        # Create an RHarness instance and test what's in the cell
        harness = RHarness()
        return self._run_exercise(harness, testname, cell)

    # -- "Private" methods --

    def _run_exercise(self, harness, testname, cell):
        """
        Runs the exercise in a "test harness".
        :param harness: The test harness that knows how to run Python or R code.
        :param testname: The name of the test. The corresponding expected value
            will be looked up within the method and compared to what the harness returned.
        :param cell: The contents of an IPython cell, i.e. the code to be executed.
        :return: The result of the last line of the `cell` code.
        """
        ok = harness.test_expr(self._tests[testname], cell)
        if ok:
            print("Passed :-)")
        else:
            # JupyterLab will print this with a red background
            print("Failed :-(", file=stderr)
        return harness.last


