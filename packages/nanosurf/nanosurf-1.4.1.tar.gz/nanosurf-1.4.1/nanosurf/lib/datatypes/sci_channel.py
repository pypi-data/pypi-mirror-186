"""Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""


import typing
import numpy as np

class SciChannel:
    def __init__(self, 
        copy_from: typing.Union[list, np.ndarray, 'SciChannel', None] = None, 
        array_length: int = 0, 
        unit :str = ""):

        self.value = np.zeros(array_length)
        self.unit = unit

        if copy_from is not None:
            if isinstance(copy_from, SciChannel):
                self.value = np.copy(copy_from.value)
                self.unit = copy_from.unit
            else:
                self.value = np.copy(copy_from)
                self.unit = unit

