#!/usr/bin/env python3
"""Plot direct properties of the calculator (dataset, energy, forces,...)."""

from typing import Optional, Dict, Any, List

import numpy as np
import matplotlib.pyplot as plt

from ase.atoms import Atoms

from .setup import GenericPlots


class RunnerPlots(GenericPlots):
    """A plotting interface for the Runner calculator."""

    def __init__(
        self,
        dataset: List[Atoms],
        results: Dict[str, Any]
    ) -> None:
        """Initialize the class."""
        self.dataset = dataset
        self.results = results
        self._energy_reference = None
        self._forces_reference = None
        self._energy_hdnnp = None
        self._forces_hdnnp = None

    @property
    def energy_reference(self):
        """Show the reference energies in `self.dataset`."""
        if self._energy_reference is None:
            self._energy_reference = np.array([i.get_potential_energy()
                                               for i in self.dataset])

        return self._energy_reference.copy()

    @property
    def energy_hdnnp(self):
        """Show the energy predictions of the HDNNP."""
        if self._energy_hdnnp is None:
            if 'energy' not in self.results or self.results['energy'] is None:
                raise RuntimeError('Cannot access energy prediction before '
                                   + 'running mode 3.')

            self._energy_hdnnp = self.results['energy']

        return self._energy_hdnnp.copy()

    @property
    def forces_reference(self):
        """Show the reference forces in `self.dataset`."""
        if self._forces_reference is None:
            self._forces_reference = np.array([i.get_forces()
                                               for i in self.dataset],
                                              dtype='object')

        return self._forces_reference.copy()

    @property
    def forces_hdnnp(self):
        """Show the force predictions of the HDNNP."""
        if self._forces_hdnnp is None:
            if 'forces' not in self.results or self.results['forces'] is None:
                raise RuntimeError('Cannot access force prediction before '
                                   + 'running mode 3.')

            self._forces_hdnnp = self.results['forces']

        return self._forces_hdnnp.copy()

    def energy_distribution(
        self,
        energy: np.ndarray,
        n_atoms: Optional[np.ndarray] = None,
        indices: Optional[np.ndarray] = None,
        axes: Optional[plt.Axes] = None,
    ) -> plt.Axes:
        """Create a scatter plot of the energy distribution in `energy`.

        Parameters
        ----------
        energy : np.ndarray
            A list of energies.
        n_atoms : np.ndarray
            If given, `energy` is normalized by `n_atoms`.
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # If no axis object was provided, use the last one or create a new one.
        if axes is None:
            axes = plt.gca()

        if indices is None:
            indices = np.arange(0, len(energy), 1)

        if n_atoms is not None:
            energy /= n_atoms

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create plot.
            axes.scatter(indices, energy[indices])

            # Set title and labels.
            axes.set_xlabel('Structure Index')
            axes.set_ylabel('Energy $E$ / eV atom$^{-1}$')
            axes.set_title('Energy Distribution in the Training Dataset')

        return axes

    def energy_distribution_reference(
        self,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the energy distribution in `self.dataset`.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # Determine the number of atoms in each structure.
        n_atoms = np.array([len(i) for i in self.dataset])

        return self.energy_distribution(self.energy_reference, n_atoms=n_atoms,
                                        indices=indices, axes=axes)

    def energy_distribution_hdnnp(
        self,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the predicted energy distribution.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # Determine the number of atoms in each structure.
        n_atoms = np.array([len(i) for i in self.dataset])

        return self.energy_distribution(self.energy_hdnnp, n_atoms=n_atoms,
                                        indices=indices, axes=axes)

    def totalforce_distribution(
        self,
        forces: np.ndarray,
        indices: Optional[np.ndarray] = None,
        axes: Optional[plt.Axes] = None
    ) -> plt.Axes:
        """Create a scatter plot of the total forces of each atom in `dataset`.

        Parameters
        ----------
        forces : np.ndarray
            The atomic forces (num_structures x num_atoms x 3).
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # If no axis object was provided, use the last one or create a new one.
        if axes is None:
            axes = plt.gca()

        # Calculate the total force of each atom.
        atomic_forces = np.vstack(forces)  # type: ignore
        totalforce = np.sqrt(np.sum(atomic_forces**2, axis=1))

        if indices is None:
            indices = np.arange(0, len(totalforce), 1)

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create plot.
            axes.scatter(indices, totalforce[indices])

            # Set title and labels.
            axes.set_xlabel('Structure Index')
            axes.set_ylabel(r'Total Force $F$ / eV $\AA^{-1}$')
            axes.set_title('Total Atomic Force Distribution')

        return axes

    def totalforce_distribution_reference(
        self,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the total forces of each atom in `dataset`.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        return self.totalforce_distribution(self.forces_reference,
                                            indices=indices, axes=axes)

    def totalforce_distribution_hdnnp(
        self,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the total force prediction of each atom.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        return self.totalforce_distribution(self.forces_hdnnp,
                                            indices=indices, axes=axes)

    def force_distribution(
        self,
        forces: np.ndarray,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the atomic force of each atom in `dataset`.

        Parameters
        ----------
        forces : np.ndarray
            The atomic forces (num_structures x num_atoms x 3).
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # If no axis object was provided, use the last one or create a new one.
        if axes is None:
            axes = plt.gca()

        # Calculate the total force of each atom.
        atomic_forces = np.vstack(forces)  # type: ignore

        if indices is None:
            indices = np.arange(0, len(atomic_forces), 1)

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create plot.
            axes.scatter(indices, atomic_forces[indices, 0],
                         label=r'$F_{\mathrm{x}}$')
            axes.scatter(indices, atomic_forces[indices, 1],
                         label=r'$F_{\mathrm{y}}$')
            axes.scatter(indices, atomic_forces[indices, 2],
                         label=r'$F_{\mathrm{z}}$')

            # Set title and labels.
            axes.set_xlabel('Structure Index')
            axes.set_ylabel(r'Total Force $F$ / eV $\AA^{-1}$')
            axes.set_title('Atomic Force Distribution')

            plt.legend()

        return axes

    def force_distribution_reference(
        self,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the forces of each atom in `dataset`.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        return self.force_distribution(self.forces_reference,
                                       indices=indices, axes=axes)

    def force_distribution_hdnnp(
        self,
        axes: Optional[plt.Axes] = None,
        indices: Optional[np.ndarray] = None
    ) -> plt.Axes:
        """Create a scatter plot of the force prediction of each atom.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        return self.force_distribution(self.forces_hdnnp,
                                       indices=indices, axes=axes)

    def energy_deviation_vs_reference(
        self,
        indices: Optional[np.ndarray] = None,
        axes: Optional[plt.Axes] = None,
    ) -> plt.Axes:
        """Create a scatter plot of energy deviation vs. reference energy.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # If no axis object was provided, use the last one or create a new one.
        if axes is None:
            axes = plt.gca()

        if indices is None:
            indices = np.arange(0, len(self.energy_reference), 1)

        # Determine the number of atoms in each structure.
        n_atoms = np.array([len(i) for i in self.dataset])

        energy_hdnnp = self.energy_hdnnp / n_atoms
        energy_reference = self.energy_reference / n_atoms

        # Calculate the deviation in meV.
        deviation = (energy_hdnnp - energy_reference) * 1000

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create plot.
            axes.scatter(energy_reference[indices], deviation[indices])

            # Set title and labels.
            axes.set_xlabel('Reference Energy $E$ / eV atom$^{-1}$')
            axes.set_ylabel(r'Energy Deviation $\Delta E$ / meV atom$^{-1}$')
            axes.set_title('Energy Deviation')

        return axes

    def energy_hdnnp_vs_reference(
        self,
        indices: Optional[np.ndarray] = None,
    ) -> plt.Axes:
        """Create a scatter plot of predicted energy vs. reference energy.

        Parameters
        ----------
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # Create a new figure for the histogram, if not given.
        fig = plt.figure()

        if indices is None:
            indices = np.arange(0, len(self.energy_reference), 1)

        # Determine the number of atoms in each structure.
        n_atoms = np.array([len(i) for i in self.dataset])

        energy_hdnnp = self.energy_hdnnp[indices] / n_atoms[indices]
        energy_reference = self.energy_reference[indices] / n_atoms[indices]

        # Determine the axis limits.
        axes_lim = [min(energy_hdnnp.min(), energy_reference.min()),
                    max(energy_hdnnp.max(), energy_reference.max())]

        # Construct the axes for the three different plots.
        gridspec = fig.add_gridspec(2, 2,  width_ratios=(7, 2),
                                    height_ratios=(2, 7), left=0.1,
                                    right=0.9, bottom=0.1, top=0.9,
                                    wspace=0.1, hspace=0.2)

        ax_scatter = fig.add_subplot(gridspec[1, 0])
        ax_histx = fig.add_subplot(gridspec[0, 0], sharex=ax_scatter)
        ax_histy = fig.add_subplot(gridspec[1, 1], sharey=ax_scatter)

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create scatter plot with diagonal line.
            ax_scatter.scatter(energy_reference, energy_hdnnp)
            ax_scatter.plot(energy_reference, energy_reference, color='grey')

            # Create histograms.
            ax_histx.hist(energy_reference)
            ax_histy.hist(energy_hdnnp, orientation='horizontal')
            ax_histx.tick_params(labelbottom=False)
            ax_histy.tick_params(labelleft=False)

            # Set axis limits.
            ax_scatter.set_xlim(axes_lim)
            ax_scatter.set_ylim(axes_lim)
            ax_histx.set_xlim(axes_lim)
            ax_histy.set_ylim(axes_lim)

            # Set title and labels.
            ax_scatter.set_xlabel('Reference Energy $E$ / eV atom$^{-1}$')
            ax_scatter.set_ylabel(r'Predicted Energy $E$ / eV atom$^{-1}$')
            fig.suptitle('Energy Comparison')

        return fig

    def force_deviation_vs_reference(
        self,
        indices: Optional[np.ndarray] = None,
        axes: Optional[plt.Axes] = None,
    ) -> plt.Axes:
        """Create a scatter plot of force deviation vs. reference force.

        Parameters
        ----------
        axes : plt.Axes
            A maplotlib.pyplot `Axes` instance to which the data will be added.
            If no axis is supplied, a new one is generated and returned instead.
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # If no axis object was provided, use the last one or create a new one.
        if axes is None:
            axes = plt.gca()

        force_hdnnp = np.vstack(self.forces_hdnnp)  # type: ignore
        force_reference = np.vstack(self.forces_reference)  # type: ignore

        if indices is None:
            indices = np.arange(0, len(force_reference), 1)

        force_hdnnp = force_hdnnp[indices, :]
        force_reference = force_reference[indices, :]

        # Calculate the deviation in meV.
        deviation = abs(force_hdnnp - force_reference) * 1000

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create plot.
            axes.scatter(force_reference[indices, 0], deviation[indices, 0],
                         label=r'$F_{\mathrm{x}}$')
            axes.scatter(force_reference[indices, 1], deviation[indices, 1],
                         label=r'$F_{\mathrm{y}}$')
            axes.scatter(force_reference[indices, 2], deviation[indices, 2],
                         label=r'$F_{\mathrm{z}}$')

            # Set title and labels.
            axes.set_xlabel(r'Reference Forces $F$ / eV $\AA^{-1}$')
            axes.set_ylabel(r'Force Deviation $\Delta F$ / meV $\AA^{-1}$')
            axes.set_title('Force Deviation')

            axes.legend()

        return axes

    def force_hdnnp_vs_reference(
        self,
        indices: Optional[np.ndarray] = None,
    ) -> plt.Axes:
        """Create a scatter plot of predicted forces vs. reference forces.

        Parameters
        ----------
        indices : List[int] or np.ndarray
            If given, only the structures at index `indices` in `self.dataset`
            will be plotted.
        """
        # Create a new figure for the histogram, if not given.
        fig = plt.figure()

        if indices is None:
            indices = np.arange(0, len(self.forces_reference), 1)

        forces_hdnnp = self.forces_hdnnp[indices]
        forces_reference = self.forces_reference[indices]

        # Create atomic arrays.
        atomic_forces_hdnnp = np.vstack(forces_hdnnp)  # type: ignore
        atomic_forces_reference = np.vstack(forces_reference)  # type: ignore

        # Determine the axis limits.
        axes_lim = [min(atomic_forces_hdnnp.min(),
                        atomic_forces_reference.min()),
                    max(atomic_forces_hdnnp.max(),
                        atomic_forces_reference.max())]

        # Construct the axes for the three different plots.
        gridspec = fig.add_gridspec(2, 2,  width_ratios=(7, 2),
                                    height_ratios=(2, 7), left=0.1,
                                    right=0.9, bottom=0.1, top=0.9,
                                    wspace=0.1, hspace=0.2)

        ax_scatter = fig.add_subplot(gridspec[1, 0])
        ax_histx = fig.add_subplot(gridspec[0, 0], sharex=ax_scatter)
        ax_histy = fig.add_subplot(gridspec[1, 1], sharey=ax_scatter)

        # Use a context manager to apply styles locally.
        with plt.style.context(self.styles):

            # Create scatter plot with diagonal line.
            ax_scatter.scatter(atomic_forces_reference[:, 0],
                               atomic_forces_hdnnp[:, 0],
                               label=r'$F_{\mathrm{x}}$')
            ax_scatter.scatter(atomic_forces_reference[:, 1],
                               atomic_forces_hdnnp[:, 1],
                               label=r'$F_{\mathrm{y}}$')
            ax_scatter.scatter(atomic_forces_reference[:, 2],
                               atomic_forces_hdnnp[:, 2],
                               label=r'$F_{\mathrm{z}}$')
            ax_scatter.plot(atomic_forces_reference.flatten(),
                            atomic_forces_reference.flatten(), color='grey')

            # Create histograms.
            ax_histx.hist(atomic_forces_reference[:, 0])
            ax_histy.hist(atomic_forces_hdnnp[:, 0], orientation='horizontal')
            ax_histx.hist(atomic_forces_reference[:, 1])
            ax_histy.hist(atomic_forces_hdnnp[:, 1], orientation='horizontal')
            ax_histx.hist(atomic_forces_reference[:, 2])
            ax_histy.hist(atomic_forces_hdnnp[:, 2], orientation='horizontal')
            ax_histx.tick_params(labelbottom=False)
            ax_histy.tick_params(labelleft=False)

            # Set axis limits.
            ax_scatter.set_xlim(axes_lim)
            ax_scatter.set_ylim(axes_lim)
            ax_histx.set_xlim(axes_lim)
            ax_histy.set_ylim(axes_lim)

            # Set title and labels.
            ax_scatter.set_xlabel(r'Reference Forces $F$ / eV $\AA^{-1}$')
            ax_scatter.set_ylabel(r'Predicted Forces $F$ / eV $\AA^{-1}$')
            fig.suptitle('Force Comparison')

            ax_scatter.legend()

        return fig
