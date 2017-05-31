"""
Adaptfilt
=========
Adaptive filtering module for Python. For more information please visit
https://github.com/Wramberg/adaptfilt or https://pypi.python.org/pypi/adaptfilt
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

__version__ = '0.3'
__author__ = "Jesper Wramberg & Mathias Tausen"
__license__ = "MIT"

# Ensure user has numpy
try:
    import numpy
except:
    raise ImportError('Failed to import numpy - please make sure this is\
 available before using adaptfilt')

# Import functions directly into adaptfilt namespace
from adaptfilt.ap import ap
from adaptfilt.lms import lms
from adaptfilt.misc import mswe
from adaptfilt.nlms import nlms
from adaptfilt.nlmsru import nlmsru
from adaptfilt.rls import rls


def __rundoctests__(verbose=False):
    """
    Executes doctests
    """
    import doctest
    import adaptfilt.lms as testmod1
    import adaptfilt.nlms as testmod2
    import adaptfilt.ap as testmod3
    import adaptfilt.misc as testmod4
    import adaptfilt.nlmsru as testmod5
    lmsres = doctest.testmod(testmod1, verbose=verbose)
    nlmsres = doctest.testmod(testmod2, verbose=verbose)
    apres = doctest.testmod(testmod3, verbose=verbose)
    miscres = doctest.testmod(testmod4, verbose=verbose)
    nlmsrures = doctest.testmod(testmod5, verbose=verbose)
    print('   LMS: %i passed and %i failed' %
          (lmsres.attempted - lmsres.failed, lmsres.failed))
    print('  NLMS: %i passed and %i failed' %
          (nlmsres.attempted - nlmsres.failed, nlmsres.failed))
    print('NLMSRU: %i passed and %i failed' %
          (nlmsrures.attempted - nlmsrures.failed, nlmsrures.failed))
    print('    AP: %i passed and %i failed' %
          (apres.attempted - apres.failed, apres.failed))
    print('  MISC: %i passed and %i failed' %
          (miscres.attempted - miscres.failed, miscres.failed))
