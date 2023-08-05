# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# Built-in imports
import numpy
from dataclasses import dataclass

# Local imports
from SuPyMode.Tools import representations


class InheritFromCppSolver():
    """
    Property class for inherited attribute from C++ EigenSolver.

    """
    @property
    def right_boundary(self) -> str:
        return self.cpp_solver.right_boundary

    @property
    def bottom_boundary(self) -> str:
        return self.cpp_solver.bottom_boundary

    @property
    def top_boundary(self) -> str:
        return self.cpp_solver.top_boundary

    @property
    def left_boundary(self) -> str:
        return self.cpp_solver.left_boundary


class InheritFromSuperSet():
    """
    Property class for inherited attribute from SuperSet.

    """
    @property
    def geometry(self) -> object:
        return self.parent_set.geometry

    @property
    def itr_list(self) -> numpy.ndarray:
        return self.parent_set.itr_list

    @property
    def axes(self) -> object:
        return self.parent_set.axes


@dataclass
class SuperMode(InheritFromCppSolver, InheritFromSuperSet):
    """
    .. note::
        This class is a representation of the fiber optic structures SuperModes.
        Those mode belongs to a SuperSet class and are constructed with the SuPySolver.
        It links to c++ SuperMode class.
    """
    parent_set: None
    """SuperSet to which is associated the computed this mode"""
    cpp_solver: None
    """c++ solver to which is linked this binded mode"""
    binding_number: int
    """Number which bind this mode to a specific c++ mode"""
    solver_number: int
    """Number which bind this mode to a specific python solver"""
    mode_number: int
    """Unique number associated to this mode in a particular symmetry set"""

    def __post_init__(self):
        self.binding = self.cpp_solver.get_mode(self.binding_number)
        self.ID = [self.solver_number, self.binding_number]
        self.name = f"Mode {self.ID[0]}:{self.ID[1]}"
        self.field = representations.Field(parent_supermode=self)
        self.index = representations.Index(parent_supermode=self)
        self.beta = representations.Beta(parent_supermode=self)
        self.coupling = representations.Coupling(parent_supermode=self)
        self.adiabatic = representations.Adiabatic(parent_supermode=self)

    @property
    def boundaries(self) -> dict:
        return {'bottom': self.bottom_boundary, 'right': self.right_boundary, 'top': self.top_boundary, 'left': self.left_boundary}

    def is_computation_compatible(self, other: 'SuperMode') -> bool:
        """
        Determines whether the specified other supermode is compatible
        for computation of the modal coupling and adiabatic criterion.
        It, basically return False only if the mode is the same or if the
        boundaries symmetries differ in some way.

        :param      other:  The other SuperMode to compare with
        :type       other:  SuperMode

        :returns:   True if the specified other is computation compatible, False otherwise.
        :rtype:     bool
        """
        if self.ID == other.ID or self.is_symmetry_compatible(other):
            return False
        else:
            return True

    def is_symmetry_compatible(self, other: 'SuperMode'):
        return self.boundaries == other.boundaries

# -
