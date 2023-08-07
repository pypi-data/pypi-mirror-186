__version__ = "0.3"
__author__ = "Thomas Baldauf"
__email__ = "thomas.baldauf@dlr.de"
__license__ = "MIT"
__birthdate__ = '15.11.2021'
__status__ = 'prod' # options are: dev, test, prod

from .singleton import Singleton
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import warnings


class Clock(Singleton):
    """
    The clock of the simulation.
    """

    def __init__(self, t0=datetime.min, dt=relativedelta(months=1)):
        """
        Init a world clock.

        :param t0: optional, starting date of the clock
        :param dt: optional, datetime.timedelta describing the real time step. Default is one month.

        Example

        .. code-block:: python

            from sfctools import Clock

            for i in range(500):
                # simulation steps

                Clock().tick()
                print(Clock().get_time(), Clock().get_real_time())

        """

        if self.do_init: # only init the clock at the first constructor call! See Singleton super class implementation

            self._t0 = t0
            self._t = 0  # the simulation tme
            self._real_time = t0  # the real time as datetime object starting at big bang
            self._dt = dt
            self.set_initialized()

    @property
    def t0(self):
        return self._t0

    def reset(self,verbose=False):
        """
        Resets the clock

        :param verbose: bool (default False), triggers a reset warning if True
        """

        if verbose:
            warnings.warn("Clock has been reset")

        self._t = 0  # the simulation tme
        self._real_time = self._t0  # the real time as datetime object starting at big bang

    def tick(self):
        """
        Increases the clock tick by one
        """
        self._t += 1
        self._real_time += self._dt

    def get_time(self):
        """
        Gets the current simulation time as int
        """
        return self._t

    def get_real_time(self):
        """
        Get the real time (the actual time on the 'non-simulation' timeline) as datetime
        """
        return self._real_time  # < TODO test this
