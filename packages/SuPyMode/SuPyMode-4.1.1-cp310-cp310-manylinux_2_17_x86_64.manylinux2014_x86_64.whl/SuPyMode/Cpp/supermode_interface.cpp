#include <pybind11/pybind11.h>
#include "includes/supermode.cpp"

PYBIND11_MODULE(SuperMode, module)
{
    module.doc() = "A c++ wrapper class for SuperMode";

    pybind11::class_<SuperMode>(module, "SuperMode")
    .def("get_fields",                &SuperMode::GetFields)
    .def("get_index",                 &SuperMode::GetIndex)
    .def("get_betas",                 &SuperMode::GetBetas)
    .def("get_coupling",              &SuperMode::GetCoupling)
    .def("get_adiabatic",             &SuperMode::GetAdiabatic)
    .def("get_adiabatic_specific",    &SuperMode::GetAdiabaticSpecific)
    .def("get_coupling_specific",     &SuperMode::GetCouplingSpecific)
    .def_readwrite("left_boundary",   &SuperMode::left_boundary)
    .def_readwrite("right_boundary",  &SuperMode::right_boundary)
    .def_readwrite("top_boundary",    &SuperMode::top_boundary)
    .def_readwrite("bottom_boundary", &SuperMode::bottom_boundary)
    .def_readwrite("binding_number",  &SuperMode::ModeNumber);
}

