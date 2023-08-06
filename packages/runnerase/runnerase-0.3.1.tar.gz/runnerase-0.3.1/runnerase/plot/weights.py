#!/usr/bin/env python3
"""Plot atomic neural network weights."""

from typing import Optional, Dict

import numpy as np

import matplotlib.pyplot as plt

from .setup import GenericPlots


class RunnerWeightsPlots(GenericPlots):
    """A plotting interface for atomic neural network weights."""

    def __init__(self, data: Dict[str, np.ndarray]) -> None:
        """Initialize the class."""
        self.data = data

    def hist(self,  axes: Optional[plt.Axes] = None) -> plt.Axes:
        """Create a histogram of the neural network weights.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        """
        # If no axis object was provided, use the last one or create a new one.
        if axes is None:
            axes = plt.gca()

        # Choose the right style for a bar plot.
        self.add_style('bar')

        # weights.data contains a dictionary of np.ndarrays.
        for element, data in self.data.items():

            # Determine the number of bins.
            n_bins = int(data.max() - data.min()) * 5

            # Use a context manager to apply styles locally.
            with plt.style.context(self.styles):

                # Create histogram for this element.
                axes.hist(data, bins=n_bins,
                          label=f'Element {element}', log=True)

                # Set title and labels.
                axes.set_xlabel('Weights values / a. u.')
                axes.set_ylabel('Occurences')
                axes.set_title('RuNNer Atomic Neural Network Weights')

                axes.legend()

        return axes
