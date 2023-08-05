#pragma once

#include "supermode.cpp"
#include "extrapolate.cpp"
#include "laplacian.cpp"
#include "definitions.cpp"
#include "utils.cpp"
#include "numpy_interface.cpp"

class CppSolver : public BaseLaplacian
{
  public:
    size_t n_computed_mode, n_sorted_mode, max_iteration, DegenerateFactor, ITRLength, Order, ExtrapolOrder;
    ScalarType Tolerance, k, kInit, kDual, lambda, MaxIndex;
    ScalarType *MeshPtr, *ITRPtr;
    std::vector<double> ITRList;
    MSparse EigenMatrix, Identity, M;
    VectorType MeshGradient;
    Eigen::BiCGSTAB<MSparse>  Solver;
    std::vector<SuperMode> SuperModes, sorted_supermodes;


  CppSolver(ndarray &Mesh,
            ndarray &PyMeshGradient,
            Vecf2D &FinitDiffMatrix,
            size_t n_computed_mode,
            size_t n_sorted_mode,
            size_t max_iteration,
            ScalarType Tolerance,
            ScalarType Wavelength,
            bool Debug)
               : BaseLaplacian(Mesh)
                {
                 this->FinitDiffMatrix   = FinitDiffMatrix;
                 this->Debug             = Debug;
                 this->n_computed_mode   = n_computed_mode;
                 this->n_sorted_mode     = n_sorted_mode;
                 this->max_iteration     = max_iteration;
                 this->Tolerance         = Tolerance;

                 this->MeshPtr           = (ScalarType*) Mesh.request().ptr;
                 this->lambda            = Wavelength;
                 this->k                 = 2.0 * PI / Wavelength;
                 this->kInit             = this->k;
                 ScalarType *adress      = (ScalarType*) PyMeshGradient.request().ptr;

                 Eigen::Map<VectorType> MeshGradient( adress, size );
                 this->MeshGradient = MeshGradient;

                 generate_mode_set();

                 compute_max_index();
               }


   SuperMode get_mode(size_t Mode){ return sorted_supermodes[Mode]; }

   void SwapMode(SuperMode &Mode0, SuperMode &Mode1);


  void set_boundaries(std::string left_boundary, std::string right_boundary, std::string top_boundary, std::string bottom_boundary)
  {
      this->left_boundary = left_boundary;
      this->right_boundary = right_boundary;
      this->top_boundary = top_boundary;
      this->bottom_boundary = bottom_boundary;
  }

   void generate_mode_set()
   {
     for (int i=0; i<n_computed_mode; ++i)
        SuperModes.push_back(SuperMode(i));

     for (int i=0; i<n_sorted_mode; ++i)
        sorted_supermodes.push_back(SuperMode(i));

   }

   MSparse compute_finit_diff_matrix()
   {
       EigenMatrix = BaseLaplacian::Laplacian;

       size_t iter = 0;

       for(size_t i=0; i<Nx; ++i)
          for(size_t j=0; j<Ny; ++j){
              Identity.coeffRef(iter, iter) = + pow(MeshPtr[iter] * kDual, 2);
              ++iter;
            }

       EigenMatrix += Identity;

       Identity.setIdentity();

       return -1.0 * EigenMatrix;
       }


   tuple<MatrixType, VectorType> compute_eigen_solution(ScalarType alpha){

       MSparse EigenMatrix = compute_finit_diff_matrix();

       Spectra::SparseGenRealShiftSolve<ScalarType> op(EigenMatrix);

       Spectra::GenEigsRealShiftSolver<Spectra::SparseGenRealShiftSolve<ScalarType>> eigs(op, n_computed_mode, 2*n_computed_mode, alpha);

       eigs.init();

       int nconv = eigs.compute(Spectra::SortRule::LargestMagn, max_iteration, Tolerance);

       EigenMatrix.resize(0,0);

       MatrixType Vectors = eigs.eigenvectors().real();

       VectorType Values = eigs.eigenvalues().real();

       return std::make_tuple(Vectors, Values);
       }


   void compute_laplacian(){

     Identity = MSparse(size,size); Identity.setIdentity();

     FromTriplets();
   }


   void prepare_supermodes()
   {
     for (SuperMode& mode : SuperModes)
         mode.Init(ITRLength, Nx, Ny, left_boundary, right_boundary, top_boundary, bottom_boundary, n_sorted_mode);
   }


   void populate_computed_supermodes(size_t Slice, MatrixType& EigenVectors, VectorType& EigenValues)
   {
     for (SuperMode& mode : SuperModes)
     {
       mode.Fields.col(Slice)   << EigenVectors.col(mode.ModeNumber);
       mode.Fields.col(Slice).normalize();
       mode.Betas[Slice]        = sqrt( - EigenValues[mode.ModeNumber] ) / ITRList[Slice];
       mode.EigenValues[Slice]  = EigenValues[mode.ModeNumber];
       mode.Index[Slice]        = sqrt( abs( mode.EigenValues[Slice] ) ) / (ITRList[Slice] * kInit);
     }

   }


   void loop_over_itr(std::vector<double> ITRList, size_t order = 1, ScalarType alpha=0){
     this->ITRList = ITRList;

     ITRLength = ITRList.size();


     kInit = 2.0 * PI / lambda;

     MatrixType EigenVectors;
     VectorType EigenValues;

     prepare_supermodes();

     std::vector<ScalarType> all_first_eigen_values;

     all_first_eigen_values.reserve(ITRLength);

     if (alpha == 0)
        alpha = -pow( k * compute_max_index(), 2 );



     for (size_t slice=0; slice<ITRLength; ++slice)
     {

       if (Debug)
       {
         size_t barWidth = 70;
         std::cout << "[";

         double progress = (double) slice/ITRLength;

         size_t pos = (size_t) (barWidth * progress);

         for (size_t i = 0; i < barWidth; ++i) {
             if (i < pos) std::cout << "=";
             else if (i == pos) std::cout << ">";
             else std::cout << " ";
         }
         std::cout << "] " << "ITR: " <<ITRList[slice] << "\n";
         std::cout.flush();

       }

       kDual = kInit * ITRList[slice];

       tie(EigenVectors, EigenValues) = compute_eigen_solution(alpha);

       populate_computed_supermodes(slice, EigenVectors, EigenValues);

       all_first_eigen_values.push_back(EigenValues[0]);

       size_t next = slice+1, mode=0;

       alpha = ExtrapolateNext(order, all_first_eigen_values, ITRList, next);
     }

   }

    vector<size_t> compute_supermodes_overlap(size_t Slice)
    {

        ScalarType best_overlap, Overlap;
        vector<size_t> Indices(n_sorted_mode);

        for (size_t i=0; i<n_sorted_mode; ++i)
        {
        best_overlap = 0;
        for (size_t j=0; j<n_computed_mode; ++j)
        {
            SuperMode Mode0 = SuperModes[i], Mode1 = SuperModes[j];

            Overlap = Mode0.compute_overlap(Mode1, Slice);

            if (Overlap > best_overlap) {Indices[i] = j; best_overlap = Overlap;}
        }
        if (best_overlap<0.8)
        std::cout<<"Bad mode correspondence: "<< best_overlap <<"  At ITR: "<< ITRList[Slice] <<". You should consider makes more ITR steps"<<std::endl;
        }

    return Indices;

    }

    void ArrangeModeField()
    {
        std::cout<<"Regularizing mode fields\n";

        for (size_t mode=0; mode<n_sorted_mode; ++mode)
        {
            SuperMode &Mode = sorted_supermodes[mode];
            for (size_t slice=0; slice<ITRLength-2; ++slice)
            {
                ScalarType overlap = Mode.compute_overlap(Mode, slice, slice+1);
                if (overlap < 0)
                    Mode.Fields.col(slice+1) *= -1;
            }

        }

    }

    void sort_supermodes(std::string Type)
    {
        std::cout<<"Sorting SuperModes\n";

        for (SuperMode &mode : sorted_supermodes)
        {
            mode.Init(ITRLength, Nx, Ny, left_boundary, right_boundary, top_boundary, bottom_boundary, n_sorted_mode);
        }

        if (Type == "field") sort_supermodes_with_fields();
        else if (Type == "index") sort_supermodes_with_index();
        else if (Type == "none") sort_supermodes_with_none();

        ArrangeModeField();
    }

    void sort_slice_with_index(size_t Slice)
    {
        vector<ScalarType> Betas;
        Betas.reserve(n_computed_mode);

        size_t iter=0;
        for (size_t mode=0; mode<n_sorted_mode; ++mode)
        {
            Betas.push_back(SuperModes[mode].Betas[Slice]);

            ++iter;
        }

        vector<size_t> sorted = sort_indexes( Betas );

        for (size_t mode=0; mode<n_sorted_mode; ++mode)
        {
            auto order = sorted[mode];
            sorted_supermodes[mode].copy_other_slice(SuperModes[order], Slice);
        }
    }


    void sort_supermodes_with_index()
    {
        for (size_t l=0; l<ITRLength; ++l)
            sort_slice_with_index(l);
    }


    void sort_supermodes_with_fields()
    {
        for (size_t mode=0; mode<n_sorted_mode; ++mode)
            sorted_supermodes[mode] = SuperModes[mode];

        for (size_t slice=0; slice<ITRLength-1; ++slice)
            sort_slice_with_fields(slice);
    }


    std::vector<std::vector<size_t>> get_max_index(Eigen::MatrixXf &Matrix)
    {
        std::vector<std::vector<size_t>> MaxIndex;
        Eigen::MatrixXf::Index max_index;

        for (size_t row=0; row < n_sorted_mode; row++ )
        {
            Matrix.row(row).maxCoeff(&max_index);
            MaxIndex.push_back( {row, (size_t) max_index} );
            Matrix.col(max_index) *= 0.;
        }
        return MaxIndex;
    }


    void sort_slice_with_fields(size_t &Slice)
    {
        Eigen::MatrixXf Overlap_matrix = get_overlap_matrix(Slice);

        std::vector<std::vector<size_t>> MaxIndex = get_max_index(Overlap_matrix);


        for (auto couple: MaxIndex)
        {
            SuperMode &Mode0 = sorted_supermodes[couple[0]],
                      &Mode1 = SuperModes[couple[1]];

            Mode0.Fields.col(Slice+1) = Mode1.Fields.col(Slice+1);
            Mode0.Betas[Slice+1]      = Mode1.Betas[Slice+1];
            Mode0.Index[Slice+1]      = Mode1.Index[Slice+1];
        }
    }

    Eigen::MatrixXf get_overlap_matrix(size_t &Slice)
    {
        Eigen::MatrixXf Matrix(n_sorted_mode, n_computed_mode);

        for (SuperMode &Mode0 : sorted_supermodes)
            for (SuperMode &Mode1 : SuperModes)
                Matrix(Mode0.ModeNumber, Mode1.ModeNumber) = abs( Mode0.compute_overlap(Mode1, Slice, Slice+1) );

        return Matrix;

    }

    void SwapModes(SuperMode &Mode0, SuperMode &Mode1, size_t &&Slice)
    {
        Mode0.Fields.col(Slice) = Mode1.Fields.col(Slice);
        Mode0.Betas[Slice]      = Mode1.Betas[Slice];
        Mode0.Index[Slice]      = Mode1.Index[Slice];
    }


    void _sort_slice_with_fields(size_t Slice)
    {
        for (size_t previous=0; previous<n_sorted_mode; ++previous)
        {
            SuperMode &Mode0 = sorted_supermodes[previous];
            std::vector<ScalarType> Overlaps(n_computed_mode, 0);

            for (size_t after=0; after<n_computed_mode; ++after)
                {
                    SuperMode &Mode1 = SuperModes[after];
                    Overlaps[after] = abs( Mode0.Fields.col(Slice).transpose() * Mode1.Fields.col(Slice+1)  );
                }


            size_t bestFit = GetMaxValueIndex(Overlaps);

            SwapModes(Mode0, SuperModes[bestFit], Slice+1);
        }
   }



    void sort_supermodes_with_none()
    {
        for (size_t mode=0; mode<n_sorted_mode; ++mode)
             sorted_supermodes[mode] = SuperModes[mode];
    }


   void compute_coupling()
   {

     std::cout<<"Computing coupling\n";

     for (size_t slice=0; slice<ITRLength; ++slice)
         for (SuperMode &mode0 : sorted_supermodes)
             for (size_t m=0; m<n_sorted_mode;++m)
                 {
                   SuperMode &mode1 = sorted_supermodes[m];

                   mode1.compute_coupling(mode0, slice, MeshGradient, kInit);

                 }

   }


   void compute_adiabatic(){

     std::cout<<"Computing adiabatic\n";

     for (size_t slice=0; slice<ITRLength; ++slice)
         for (SuperMode &mode0 : sorted_supermodes)
             for (size_t m=0; m<n_sorted_mode;++m)
                 {
                   SuperMode &mode1 = sorted_supermodes[m];
                   mode1.Adiabatic(mode0.ModeNumber, slice) = mode1.compute_adiabatic(mode0, slice, MeshGradient, kInit);
                 }

   }


   void compute_coupling_and_adiabatic()
   {
     std::cout<<"Computing coupling/adiabatic\n";

     for (size_t slice=0; slice<ITRLength; ++slice)
         for (SuperMode &mode0 : sorted_supermodes)
             for (size_t m=0; m<n_sorted_mode;++m)
               mode0.populate_coupling_adiabatic(sorted_supermodes[m], slice, MeshGradient, kInit);
   }

   ScalarType compute_max_index()
   {
     MaxIndex = 0.0;
     for (size_t i=0; i<size; ++i)
        if (MeshPtr[i] > MaxIndex)
            MaxIndex = MeshPtr[i];

    return MaxIndex;
   }


   tuple<ndarray, ndarray> get_slice(size_t Slice)
   {
     MatrixType OutputFields(size, n_sorted_mode);
     VectorType OutputBetas(n_sorted_mode);

     for (size_t mode=0; mode<n_sorted_mode; ++mode)
     {
       OutputFields.col(mode) = SuperModes[mode].Fields.col(Slice);
       OutputBetas[mode]      = SuperModes[mode].Betas[Slice];
     }

     ndarray FieldsPython = eigen_to_ndarray_( OutputFields, { n_sorted_mode, Nx, Ny } ) ;

     ndarray BetasPython = eigen_to_ndarray_( OutputBetas, { n_sorted_mode } ) ;

     return std::make_tuple( FieldsPython, BetasPython );
   }

};
