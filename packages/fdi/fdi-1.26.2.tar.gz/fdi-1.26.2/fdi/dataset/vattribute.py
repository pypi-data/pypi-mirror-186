# -*- coding: utf-8 -*-

import logging
# create logger
logger = logging.getLogger(__name__)
#logger.debug('level %d' %  (logger.getEffectiveLevel()))


class VAttribute():
    """ Attributes are stored in instance variables.

    Variable names start with a '_'.
    """

    def __init__(self, **kwds):
        """
        Parameter
        ---------

        Returns
        -------
        """
        super().__init__(**kwds)

    def __getattribute__(self, name):
        """ Returns the '_name'd attitute value.
        """
        if name.startswith('_'):
            return super().__getattribute__(name)
        else:
            return super().__getattribute__(f'_{name}')

    def __setattr__(self, name, value):
        """ Set the '_name'd attitute value to `value`.
        """
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            super().__setattr__(f'_{name}', value)
