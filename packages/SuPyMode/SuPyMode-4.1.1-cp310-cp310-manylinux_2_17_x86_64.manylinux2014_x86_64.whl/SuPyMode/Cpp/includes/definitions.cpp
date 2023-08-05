#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "../../../extern/eigen/Eigen/Sparse"
#include "../../../extern/spectra/include/Spectra/GenEigsRealShiftSolver.h"
#include "../../../extern/spectra/include/Spectra/MatOp/SparseGenRealShiftSolve.h"
#include <vector>
#include <iostream>


typedef double                                                      ScalarType;
typedef std::complex<ScalarType>                                    ComplexScalarType;
typedef Eigen::Matrix<ScalarType, Eigen::Dynamic, 1>                VectorType;
typedef Eigen::Matrix<ComplexScalarType, Eigen::Dynamic, 1>         ComplexVectorType;
typedef Eigen::Matrix<ScalarType, Eigen::Dynamic, Eigen::Dynamic>   MatrixType;
typedef pybind11::array_t<ScalarType>                               ndarray;
typedef pybind11::array_t<ComplexScalarType>                        Cndarray;
typedef pybind11::buffer_info                                       info;
typedef Eigen::SparseMatrix<ScalarType, Eigen::ColMajor>            MSparse;
typedef std::vector<ScalarType>                                     Vecf1D;
typedef std::vector<std::vector<ScalarType>>                        Vecf2D;
typedef Eigen::Triplet<ScalarType>                                  fTriplet;

ScalarType inf = std::numeric_limits<ScalarType>::infinity();

std::complex<ScalarType> J(0.0, 1.0);

#define PI 3.1415926535897932384626f