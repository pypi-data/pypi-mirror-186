#pragma once

#include "definitions.cpp"

class BaseLaplacian{
  public:
    std::string top_boundary, bottom_boundary, left_boundary, right_boundary;
    ndarray Mesh;
    size_t Nx, Ny, size;
    ScalarType D0xy, D1y, D2y, D1x, D2x;
    MSparse Laplacian;
    bool Debug;
    Vecf2D FinitDiffMatrix;

    BaseLaplacian(ndarray&  Mesh){
      this->Nx                = Mesh.request().shape[0];
      this->Ny                = Mesh.request().shape[1];
      this->size              = Mesh.request().size;
      this->Mesh              = Mesh;
      this->Laplacian         = MSparse(this->size, this->size);
    }


    void FromTriplets()
    {
      Vecf1D Row  = FinitDiffMatrix[0],
             Col  = FinitDiffMatrix[1],
             Data = FinitDiffMatrix[2];

      std::vector<fTriplet> Tri;
      Tri.reserve(Row.size());

      for (int i=0; i<Row.size(); i++)
          Tri.push_back(fTriplet(Col[i], Row[i], Data[i]));


       Laplacian.setFromTriplets(Tri.begin(), Tri.end());
    }


};
