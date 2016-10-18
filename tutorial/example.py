"""Module to subtract the foreground."""

from script.pipeline import SingleBase

import numpy as np


class Example(SingleBase):
    """Class to subtract the foreground."""

    params_init = {
            'output_files' : 'tmp/test.txt',
            'params_a' : 100,
            }

    prefix = 'example_'

    def process(self):

        data = np.arange(10)

        print self.params['params_a']
        print self.output_files

        return data

    def write_output(self, data):

        for output_file in self.output_files:
            np.savetxt(output_file, data)
