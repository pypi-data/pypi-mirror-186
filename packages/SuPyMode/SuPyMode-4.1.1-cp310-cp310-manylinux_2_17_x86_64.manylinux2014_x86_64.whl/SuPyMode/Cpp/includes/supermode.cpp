#pragma once

#include "definitions.cpp"
#include "utils.cpp"
#include "numpy_interface.cpp"


struct SuperMode
{
  VectorType Betas, EigenValues, Index;
  size_t ITRLength, Nx, Ny, ModeNumber, sMode;
  std::string left_boundary, right_boundary, top_boundary, bottom_boundary;
  MatrixType Fields, Coupling, Adiabatic;

  SuperMode(size_t ModeNumber){this->ModeNumber = ModeNumber;}
  SuperMode(){}


  void Init(size_t &ITRLength,
            size_t &Nx,
            size_t &Ny,
            std::string &left_boundary,
            std::string &right_boundary,
            std::string &top_boundary,
            std::string &bottom_boundary,
            int sMode)
  {
    this->Nx             = Nx;
    this->Ny             = Ny;
    this->sMode          = sMode;
    this->ITRLength      = ITRLength;
    this->Fields         = MatrixType(Nx * Ny, ITRLength);
    this->Betas          = VectorType(ITRLength);
    this->EigenValues    = VectorType(ITRLength);
    this->Index          = VectorType(ITRLength);
    this->Adiabatic      = MatrixType(sMode, ITRLength);
    this->Coupling       = MatrixType(sMode, ITRLength);
    this->bottom_boundary = bottom_boundary;
    this->top_boundary    = top_boundary;
    this->right_boundary  = right_boundary;
    this->left_boundary   = left_boundary;
  }

  void copy_other_slice(SuperMode& Other, size_t Slice)
  {
      this->Fields.col(Slice) = Other.Fields.col(Slice);
      this->Betas[Slice]      = Other.Betas[Slice];
      this->Index[Slice]      = Other.Index[Slice];
      this->Adiabatic         = Other.Adiabatic;
      this->Coupling          = Other.Coupling;
  }


  ScalarType compute_overlap(SuperMode& Other, size_t &Slice)
  {
    return this->Fields.col(Slice).transpose() * Other.Fields.col(Slice);
  }

  ScalarType compute_overlap(SuperMode& Other, size_t &&Slice)
  {
    return this->Fields.col(Slice).transpose() * Other.Fields.col(Slice);
  }

  ScalarType compute_overlap(SuperMode& Other, size_t &&Slice0, size_t &&Slice1)
  {
    return this->Fields.col(Slice0).transpose() * Other.Fields.col(Slice1);
  }

  ScalarType compute_overlap(SuperMode& Other, size_t &Slice0, size_t &&Slice1)
  {
    return this->Fields.col(Slice0).transpose() * Other.Fields.col(Slice1);
  }


  ScalarType compute_coupling(SuperMode& Other, size_t Slice, VectorType &MeshGradient, ScalarType &kInit)
  {
    ComplexScalarType C;
    if (this->ModeNumber == Other.ModeNumber)
    {
      C = 0.0;
    }

    else
    {
      VectorType overlap = this->Fields.col(Slice).cwiseProduct( Other.Fields.col(Slice) );

      ScalarType Beta0 = this->Betas[Slice], Beta1 = Other.Betas[Slice];

      C = - (ScalarType) 0.5 * J * kInit*kInit / sqrt(Beta0 *  Beta1) * abs( 1.0f / (Beta0 - Beta1) );

      ScalarType I = Trapz(overlap.cwiseProduct( MeshGradient ), 1.0, Nx, Ny);

      C *= I;

      C = abs(C);
    }

    this->Coupling(Other.ModeNumber, Slice) = abs(C);
    Other.Coupling(this->ModeNumber, Slice) = abs(C);

    return abs(C);
  }


  ScalarType compute_adiabatic(SuperMode& Other, size_t Slice, VectorType &MeshGradient, ScalarType &kInit)
  {
    ScalarType A;

    ScalarType Beta0 = this->Betas[Slice], Beta1 = Other.Betas[Slice];

    if (this->ModeNumber == Other.ModeNumber) { A = 0.0; }
    else { A = abs( (Beta0-Beta1) / compute_coupling(Other, Slice, MeshGradient, kInit) ); }

    this->Adiabatic(Other.ModeNumber, Slice) = A;
    Other.Adiabatic(this->ModeNumber, Slice) = A;

    return A;
  }


  void populate_coupling_adiabatic(SuperMode& Other, size_t Slice, VectorType &MeshGradient, ScalarType &kInit)
  {
    ComplexScalarType C;
    ScalarType A;

    ScalarType Beta0 = this->Betas[Slice], Beta1 = Other.Betas[Slice];

    if (this->ModeNumber == Other.ModeNumber)
    {
      C = 0.0;
      A = 0.0;
    }

    else
    {
      VectorType overlap = this->Fields.col(Slice).cwiseProduct( Other.Fields.col(Slice) );

      ScalarType Beta0 = this->Betas[Slice], Beta1 = Other.Betas[Slice];

      C  = - (ScalarType) 0.5 * J * kInit*kInit / sqrt(Beta0 *  Beta1) * abs( 1.0f / (Beta0 - Beta1) );

      ScalarType I       = Trapz(overlap.cwiseProduct( MeshGradient ), 1.0, Nx, Ny);

      C      *=  I;

      C = abs(C);

      A = abs( (Beta0-Beta1) / C );
    }

    this->Coupling(Other.ModeNumber, Slice) = abs(C);
    Other.Coupling(this->ModeNumber, Slice) = abs(C);
    this->Adiabatic(Other.ModeNumber, Slice) = A;
    Other.Adiabatic(this->ModeNumber, Slice) = A;
  }


  ndarray GetFields(){ return eigen_to_ndarray_( this->Fields, { ITRLength, Nx, Ny} ); }
  ndarray GetIndex(){ return eigen_to_ndarray_( this->Index, { ITRLength} ); }
  ndarray GetBetas(){ return eigen_to_ndarray_( this->Betas, { ITRLength} ); }
  ndarray GetAdiabatic(){ return eigen_to_ndarray_( this->Adiabatic, { ITRLength, sMode} ); }

  ndarray GetCoupling(){ return eigen_to_ndarray_( this->Coupling, { ITRLength, sMode} ); }
  ndarray GetAdiabaticSpecific(SuperMode& Mode){ return eigen_to_ndarray_( this->Adiabatic.row(Mode.ModeNumber), { ITRLength} ); }
  ndarray GetCouplingSpecific(SuperMode& Mode){ return eigen_to_ndarray_( this->Coupling.row(Mode.ModeNumber), { ITRLength} ); }
};



