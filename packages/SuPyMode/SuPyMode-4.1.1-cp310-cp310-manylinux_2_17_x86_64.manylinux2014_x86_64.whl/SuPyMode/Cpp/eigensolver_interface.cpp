#include <pybind11/pybind11.h>
#include "includes/eigensolver.cpp"



PYBIND11_MODULE(CppSolver, module)
{
    pybind11::class_<CppSolver>(module, "CppSolver")
    .def(pybind11::init<ndarray&, ndarray&, Vecf2D&, size_t, size_t, size_t, ScalarType, ScalarType, bool>(),
         pybind11::arg("mesh"),
         pybind11::arg("gradient"),
         pybind11::arg("finit_matrix"),
         pybind11::arg("n_computed_mode"),
         pybind11::arg("n_sorted_mode"),
         pybind11::arg("max_iter"),
         pybind11::arg("tolerance"),
         pybind11::arg("wavelength"),
         pybind11::arg("debug") = false
       )

     .def("loop_over_itr",                &CppSolver::loop_over_itr, pybind11::arg("itr"), pybind11::arg("extrapolation_order"), pybind11::arg("alpha"))
     .def("compute_adiabatic",            &CppSolver::compute_adiabatic)
     .def("compute_coupling_adiabatic",   &CppSolver::compute_coupling_and_adiabatic)
     .def("compute_coupling",             &CppSolver::compute_coupling)
     .def("sort_modes",                   &CppSolver::sort_supermodes, pybind11::arg("sorting"))
     .def("compute_laplacian",            &CppSolver::compute_laplacian)
     .def("get_slice",                    &CppSolver::get_slice, pybind11::arg("slice"))
     .def("get_mode",                     &CppSolver::get_mode)
     .def("set_boundaries",               &CppSolver::set_boundaries,  pybind11::arg("left"),  pybind11::arg("right"),  pybind11::arg("top") , pybind11::arg("bottom"))


     .def_readwrite("left_boundary",   &CppSolver::left_boundary)
     .def_readwrite("right_boundary",  &CppSolver::right_boundary)
     .def_readwrite("top_boundary",    &CppSolver::top_boundary)
     .def_readwrite("bottom_boundary", &CppSolver::bottom_boundary)
     .def_readwrite("n_sorted_mode",   &CppSolver::n_sorted_mode)
     .def_readwrite("n_computed_mode", &CppSolver::n_computed_mode)
     .def_readwrite("itr_length",      &CppSolver::ITRLength)
     .def_readwrite("itr_list",        &CppSolver::ITRList)
     .def_readwrite("wavelength",      &CppSolver::lambda);
}

