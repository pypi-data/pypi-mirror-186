#pragma once

#include "definitions.cpp"

std::vector<size_t>
GetStride(std::vector<size_t> Dimension)
{
  std::reverse(Dimension.begin(), Dimension.end());

  std::vector<size_t> stride;
  stride.push_back( sizeof(ScalarType) );

  for (size_t i=0; i<Dimension.size()-1; ++i)
      stride.push_back( stride[i] * Dimension[i] );

  std::reverse(stride.begin(), stride.end());

  return stride;

}

ndarray
eigen_to_ndarray(MatrixType *Eigen3Vector, std::vector<size_t> dimension){

  ndarray PyVector;

  std::vector<size_t> stride = GetStride(dimension);

  pybind11::capsule free_when_done(Eigen3Vector->data(), [](void *f) {
     ScalarType *foo = reinterpret_cast<ScalarType *>(f);
     delete []foo; } );

  PyVector = ndarray( dimension, stride, Eigen3Vector->data(), free_when_done );

   return PyVector;
}

ndarray
eigen_to_ndarray(VectorType *Eigen3Vector, std::vector<size_t> dimension){

  ndarray PyVector;

  std::vector<size_t> stride = GetStride(dimension);

  pybind11::capsule free_when_done(Eigen3Vector->data(), [](void *f) {
     ScalarType *foo = reinterpret_cast<ScalarType *>(f);
     delete []foo; } );

  PyVector = ndarray( dimension, stride, Eigen3Vector->data(), free_when_done );

   return PyVector;
}

Cndarray
Eigen2Cndarray(ComplexVectorType *Eigen3Vector, std::vector<size_t> dimension){

  Cndarray PyVector;

  std::vector<size_t> stride = GetStride(dimension);

  pybind11::capsule free_when_done(Eigen3Vector->data(), [](void *f) {
     ComplexScalarType *foo = reinterpret_cast<ComplexScalarType *>(f);
     delete []foo;
   } );

  PyVector = Cndarray( dimension, stride, Eigen3Vector->data(), free_when_done);

   return PyVector;
}

ndarray
eigen_to_ndarray_(VectorType &&Eigen3Vector, std::vector<size_t> dimension){

  ndarray PyVector;


  VectorType * Vectors = new VectorType;
  (*Vectors) = Eigen3Vector;


  std::vector<size_t> stride = GetStride(dimension);

  pybind11::capsule free_when_done(Vectors->data(), [](void *f) {
     ScalarType *foo = reinterpret_cast<ScalarType *>(f);
     delete []foo; } );

  PyVector = ndarray( dimension, stride, Vectors->data(), free_when_done );

   return PyVector;
}

ndarray
eigen_to_ndarray_(VectorType &Eigen3Vector, std::vector<size_t> dimension){

  ndarray PyVector;


  VectorType * Vectors = new VectorType;
  (*Vectors) = Eigen3Vector;


  std::vector<size_t> stride = GetStride(dimension);

  pybind11::capsule free_when_done(Vectors->data(), [](void *f) {
     ScalarType *foo = reinterpret_cast<ScalarType *>(f);
     delete []foo; } );

  PyVector = ndarray( dimension, stride, Vectors->data(), free_when_done );

   return PyVector;
}

ndarray
eigen_to_ndarray_(MatrixType &Eigen3Vector, std::vector<size_t> dimension){

  ndarray PyVector;


  MatrixType * Vectors = new MatrixType;
  (*Vectors) = Eigen3Vector;


  std::vector<size_t> stride = GetStride(dimension);

  pybind11::capsule free_when_done(Vectors->data(), [](void *f) {
     ScalarType *foo = reinterpret_cast<ScalarType *>(f);
     delete []foo; } );

  PyVector = ndarray( dimension, stride, Vectors->data(), free_when_done );

   return PyVector;
}
