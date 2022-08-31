#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2022
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

import logging
from pyomo.core.expr.base import ExpressionBase
from pyomo.core.expr.boolean_value import BooleanValue

logger = logging.getLogger('pyomo.contrib.cp')

class BeforeExpression(ExpressionBase, BooleanValue):
    """
    Temporal expression representing that the time point represented by the
    first argument must be before the time point represented by the second
    argument by at least 'delay' time periods.

    args:
        args (tuple): child nodes of type IntervalVarTimePoint
        delay: A (possible negative) integer value representing the number of
               time periods required between the first argument's value and the
               second argument's value
    """

    def __init__(self, before, after, delay):
        self._args = (before, after)
        self._delay = delay

    def nargs(self):
        return 2

    def _apply_operation(self, result):
        before, after = result
        return before + delay <= after

    def _to_string(self, values, verbose, smap):
        if self.delay == 0:
            first = values[0]
        elif self.delay > 0:
            first = "%s + %s" % (values[0], delay)
        else:
            first = "%s - %s" % (values[0], abs(delay))
        return "%s %s %s" % (first, "<=", values[1])

    @property
    def delay(self):
        return self._delay

    @property
    def args(self):
        """
        Return the child nodes

        Returns: Tuple containing the child nodes of this node
        """
        return self._args

class AtExpression(ExpressionBase, BooleanValue):
    """
    Temporal expression representing that the time point represented by the
    first argument must be equal to the delay plus the time point represented 
    by the second argument.

    args:
        args (tuple): child nodes of type IntervalVarTimePoint
        delay: A (possible negative) integer value representing the number of
               time periods required between the first argument's value and the
               second argument's value
    """
    def __init__(self, first, second, delay):
        self._args = (first, second)
        self._delay = delay

    def nargs(self):
        return 2

    def _apply_operation(self, result):
        before, after = result
        return before + delay == after

    def _to_string(self, values, verbose, smap):
        if self.delay == 0:
            first = values[0]
        elif self.delay > 0:
            first = "%s + %s" % (values[0], delay)
        else:
            first = "%s - %s" % (values[0], abs(delay))
        return "%s %s %s" % (first, "==", values[1])

    @property
    def delay(self):
        return self._delay

    @property
    def args(self):
        """
        Return the child nodes

        Returns: Tuple containing the child nodes of this node
        """
        return self._args
