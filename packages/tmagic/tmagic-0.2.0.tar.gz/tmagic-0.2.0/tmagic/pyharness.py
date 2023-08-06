"""
Module providing the Python exercise harness class.
:author: András Aszódi
:date: 2022-08-25
"""

from sys import version_info
import ast

from .harness import Harness

class PyHarness(Harness):
    """
    This class can be configured to run Python code from an IPython cell
    and check its result.
    """

    def __init__(self):
        """
        Creates a PyHarness instance.
        """
        super().__init__()

    # -- "hidden" --

    def _exec_script(self, script):
        """
        Executes a Python script and returns the value of the last expression,
        or None if the last command was not an expression.
        :param script: Python code as a possibly multi-line string.
        :return: The value of the last expression seen, or None
        """

        # Implementation notes:
        # The basic idea comes from https://stackoverflow.com/a/47130538
        # AA modified the last expression evaluation part

        # make all previous notebook objects accessible by `from __main__ import *`:
        script = "from __main__ import *\n" + script

        # parse the cell contents into statements
        stmts = list(ast.iter_child_nodes(ast.parse(script)))
        if not stmts:
            return None
        try:
            if isinstance(stmts[-1], ast.Expr):
                # the last one is an expression and we will try to return the results
                # so we first execute the previous statements
                if len(stmts) > 1:
                    # NOTE: the signature of ast.Module.__init__ changed in Python V3.8.
                    # It requires a second argument which apparently should be the empty list.
                    # Could not find any official documentations, only indirect hints,
                    # e.g. https://github.com/ipython/ipython/issues/11590
                    # Workaround:
                    vmajor, vminor = version_info[:2]
                    if vmajor == 3 and vminor <= 7:
                        # old behaviour
                        code = ast.Module(stmts[:-1])
                    else:
                        # V3.8 and above, new signature, note 2nd argument []
                        code = ast.Module(stmts[:-1], [])
                    prevcode = compile(code, filename="<ast>", mode="exec")
                    self.runcode(prevcode)
                # Evaluate the last expression
                lastexpr = compile(ast.Expression(body=stmts[-1].value), filename="<ast>", mode="eval")
                # we don't use `self.runcode` because it always returns None
                # instead, run `eval` but set its "globals" to `self.locals`
                # in which code.InteractiveInterpreter maintains its state
                return eval(lastexpr, self.locals)
            else:
                # otherwise we just execute the entire code
                self.runsource(script)
                return None
        except (KeyboardInterrupt, SystemExit):
            pass    # ignore them silently

    def _check(self, expval):
        """
        Checks self._last against the expected value,
        using the comparisons implemented in the `AlmostEqual` class.
        :param expval: The expected (correct) result of the test.
        :return: True if the check passed, False if failed.
        """
        # observed and expected values
        obsval = self._last
        return self._aeq.compare(expval, obsval)
