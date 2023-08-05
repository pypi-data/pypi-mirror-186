# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import numpy
from MPSPlots.Render2D import Scene2D, ColorBar, Axis, Mesh, Line
from MPSPlots import CMAP


class InheritFromSuperMode():
    def _set_axis_(self, ax: Axis):
        for element, value in self.plot_style.items():
            setattr(ax, element, value)

    @property
    def mode_number(self):
        return self.parent_supermode.mode_number

    @property
    def solver_number(self):
        return self.parent_supermode.solver_number

    @property
    def axes(self):
        return self.parent_supermode.axes

    @property
    def boundaries(self):
        return self.parent_supermode.boundaries

    @property
    def itr_list(self):
        return self.parent_supermode.itr_list

    @property
    def ID(self):
        return self.parent_supermode.ID

    @property
    def name(self):
        return self.parent_supermode.name

    def get_adiabatic_specific(self, other_supermode: "SuperMode"):
        return self.parent_supermode.binding.get_adiabatic_specific(other_supermode.binding)

    def get_coupling_specific(self, other_supermode: "SuperMode"):
        return self.parent_supermode.binding.get_coupling_specific(other_supermode.binding)

    def slice_to_itr(self, slice: list = []):
        return self.parent_supermode.parent_set.slice_to_itr(slice)

    def itr_to_slice(self, itr: list = []):
        return self.parent_supermode.parent_set.itr_to_slice(itr)

    def _interpret_itr_slice_list_(self, *args, **kwargs):
        return self.parent_supermode.parent_set._interpret_itr_slice_list_(*args, **kwargs)


class Field(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binding.get_fields()

    def get_values(self):
        return self._data

    @property
    def plot_style(self):
        return {
            "show_legend": False,
            "x_label": r'X-Direction [$\mu m$]',
            "y_label": r'Y-direction [$\mu m$]',
            "equal": True
        }

    def get_field_with_boundaries(self, slice: int):
        return self.apply_boundary_symmetries(mesh=self._data[slice])

    def apply_boundary_symmetries(self, mesh: numpy.ndarray) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
        x_axis, y_axis = self._add_boundaries_to_axis_()

        mesh = self._add_boundaries_to_mesh_(mesh=mesh)

        return x_axis, y_axis, mesh

    def add_symmetry_to_vector(self, vector: numpy.ndarray, type: str) -> numpy.ndarray:
        n = len(vector)
        dx = abs(vector[0] - vector[1])
        if type == 'right':
            start = vector[0]
            return numpy.arange(0, 2 * n) * dx + start
        elif type == 'left':
            start = vector[-1]
            return -numpy.arange(0, 2 * n)[::-1] * dx + start

    def _add_boundaries_to_axis_(self) -> tuple[numpy.ndarray, numpy.ndarray]:
        full_x_axis = self.axes.x.vector
        full_y_axis = self.axes.y.vector

        if self.boundaries['right'] in ['symmetric', 'anti-symmetric']:
            full_x_axis = self.add_symmetry_to_vector(full_x_axis, type='right')

        if self.boundaries['left'] in ['symmetric', 'anti-symmetric']:
            full_x_axis = self.add_symmetry_to_vector(full_x_axis, type='left')

        if self.boundaries['top'] in ['symmetric', 'anti-symmetric']:
            full_y_axis = self.add_symmetry_to_vector(full_y_axis, type='right')

        if self.boundaries['bottom'] in ['symmetric', 'anti-symmetric']:
            full_y_axis = self.add_symmetry_to_vector(full_y_axis, type='left')

        return full_x_axis, full_y_axis

    def _add_boundaries_to_mesh_(self, mesh: numpy.ndarray) -> numpy.ndarray:
        """
        Return mode field taking account of the boundaries of the solver

        """
        match self.boundaries['left']:
            case 'symmetric': mesh = numpy.c_[mesh[:, ::-1], mesh]

            case 'anti-symmetric': mesh = numpy.c_[-mesh[:, ::-1], mesh]

        match self.boundaries['right']:
            case 'symmetric': mesh = numpy.c_[mesh, mesh[:, ::-1]]

            case 'anti-symmetric': mesh = numpy.c_[mesh, -mesh[:, ::-1]]

        match self.boundaries['top']:
            case 'symmetric': mesh = mesh = numpy.r_[mesh, mesh[::-1, :]]

            case 'anti-symmetric': mesh = numpy.r_[mesh, -mesh[::-1, :]]

        match self.boundaries['bottom']:
            case 'symmetric': mesh = numpy.r_[mesh[::-1, :], mesh]

            case 'anti-symmetric': mesh = numpy.r_[-mesh[::-1, :], mesh]

        return mesh

    def _render_on_ax_(self, ax, slice):
        self._set_axis_(ax)

        ax.colorbar = ColorBar(symmetric=True, position='right')

        x, y, field = self.apply_boundary_symmetries(mesh=self._data[slice])

        artist = Mesh(x=x, y=y, scalar=field, colormap=CMAP.BKR)

        ax.add_artist(artist)

    def plot(self, slice_list: list = [0, -1], itr_list: list = []) -> Scene2D:
        """
        Plotting method for the fields.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(3, 3), tight_layout=True)

        slice_list, itr_list = self._interpret_itr_slice_list_(slice_list, itr_list)

        for n, (slice, itr) in enumerate(zip(slice_list, itr_list)):
            ax = Axis(row=n, col=0, title=f'{self.parent_supermode.name}\n[slice: {slice}  ITR: {itr:.2f}]')

            self._render_on_ax_(ax=ax, slice=slice)
            figure.add_axes(ax)

        return figure


class Index(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binding.get_index()

    def get_values(self):
        return self._data

    @property
    def plot_style(self):
        return {
            "show_legend": True,
            "x_label": 'ITR',
            "y_label": 'Effective refraction index'
        }

    def _render_on_ax_(self, ax: Axis):
        self._set_axis_(ax)
        artist = Line(x=self.itr_list, y=self._data, label=self.name)
        ax.add_artist(artist)

    def plot(self, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)

        ax = Axis(row=0, col=0)

        figure.add_axes(ax)

        self._render_on_ax_(ax)

        return figure


class Beta(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binding.get_betas()

    def get_values(self):
        return self._data

    @property
    def plot_style(self):
        return {
            "show_legend": True,
            "x_label": 'ITR',
            "y_label": 'Propagation constant'
        }

    def _render_on_ax_(self, ax: Axis):
        self._set_axis_(ax)
        artist = Line(x=self.itr_list, y=self._data, label=self.name)
        ax.add_artist(artist)

    def plot(self, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)

        ax = Axis(row=0, col=0)

        figure.add_axes(ax)

        self._render_on_ax_(ax)

        return figure


class Coupling(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binding.get_coupling()

    @property
    def plot_style(self):
        return {
            "show_legend": True,
            "x_label": 'ITR',
            "y_label": 'Mode coupling'
        }

    def get_values(self, other_supermode: 'SuperMode' = None) -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """
        if other_supermode is None:
            return self._data
        else:
            return self.get_coupling_specific(other_supermode=other_supermode)

    def _render_on_ax_(self, ax: Axis, other_supermode: 'SuperMode' = None):
        if other_supermode is None:
            other_supermode = self.parent_supermode.parent_set.SuperModes

        self._set_axis_(ax)
        for mode in other_supermode:
            if mode.ID == self.ID or mode.solver_number != self.solver_number:
                continue

            artist = Line(x=self.itr_list, y=self.get_values(mode), label=f'{self.name} - {mode.name}')
            ax.add_artist(artist)

    def plot(self, other_supermode: 'SuperMode' = None, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)
        ax = Axis(row=row, col=col)
        figure.add_axes(ax)

        self._render_on_ax_(ax=ax, other_supermode=other_supermode)

        return figure


class Adiabatic(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binding.get_adiabatic()

    def get_values(self, other_supermode: 'SuperMode' = None) -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """
        if other_supermode is None:
            return self._data
        else:
            return self.get_adiabatic_specific(other_supermode=other_supermode)

    @property
    def plot_style(self):
        return {
            "show_legend": True,
            "x_label": 'ITR',
            "y_label": 'Adiabatic criterion',
            "y_scale": 'log',
            "y_limits": [1e-4, 1]
        }

    def _render_on_ax_(self, ax: Axis, other_supermode: 'SuperMode' = None):
        if other_supermode is None:
            other_supermode = self.parent_supermode.parent_set.SuperModes

        self._set_axis_(ax)
        for mode in other_supermode:
            if mode.ID == self.ID or mode.solver_number != self.solver_number:
                continue

            artist = Line(x=self.itr_list, y=self.get_values(mode), label=f'{self.name} - {mode.name}')
            ax.add_artist(artist)

    def plot(self, other_supermode: 'SuperMode' = None, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """

        figure = Scene2D(unit_size=(10, 4), tight_layout=True)
        ax = Axis(row=row, col=col)
        figure.add_axes(ax)

        self._render_on_ax_(ax=ax, other_supermode=other_supermode)

        return figure

# -