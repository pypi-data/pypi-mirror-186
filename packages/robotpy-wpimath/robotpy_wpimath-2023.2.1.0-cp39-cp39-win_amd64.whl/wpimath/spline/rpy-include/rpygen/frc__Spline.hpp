
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\..\_impl\include\frc\spline\Spline.h>

#include <pybind11/stl.h>




namespace rpygen {

using namespace frc;



template <int Degree, typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__Spline :
    CfgBase
{
    using Base = frc::Spline<Degree>;

    using override_base_KCoefficients_v = frc::Spline<Degree>;
};


template <typename PyTrampolineBase, int Degree, typename PyTrampolineCfg>
struct PyTrampoline_frc__Spline : PyTrampolineBase, virtual py::trampoline_self_life_support {
    using PyTrampolineBase::PyTrampolineBase;

    using PoseWithCurvature [[maybe_unused]] = typename frc::Spline<Degree>::PoseWithCurvature;


#ifndef RPYGEN_DISABLE_KCoefficients_v
    Matrixd<6, Degree + 1 > Coefficients() const override {
        throw std::runtime_error("not implemented");
    }
#endif




};

}; // namespace rpygen


namespace rpygen {

using namespace frc;


template <int Degree>
struct bind_frc__Spline {

    
      using ControlVector [[maybe_unused]] = typename frc::Spline<Degree>::ControlVector;
    using PoseWithCurvature [[maybe_unused]] = typename frc::Spline<Degree>::PoseWithCurvature;

    
      using Spline_Trampoline = rpygen::PyTrampoline_frc__Spline<typename frc::Spline<Degree>, Degree, typename rpygen::PyTrampolineCfg_frc__Spline<Degree>>;
    static_assert(std::is_abstract<Spline_Trampoline>::value == false, "frc::Spline<Degree> " RPYBUILD_BAD_TRAMPOLINE);
py::class_<typename frc::Spline<Degree>, Spline_Trampoline> cls_Spline;


      py::class_<typename frc::Spline<Degree>::ControlVector> cls_ControlVector;





    py::module &m;
    std::string clsName;

bind_frc__Spline(py::module &m, const char * clsName) :
    cls_Spline(m, clsName),


    cls_ControlVector(cls_Spline, "ControlVector"),




    m(m),
    clsName(clsName)
{
    
}

void finish(const char * set_doc = NULL, const char * add_doc = NULL) {

    
  cls_Spline.doc() =
    "Represents a two-dimensional parametric spline that interpolates between two\n"
"points.\n"
"\n"
"@tparam Degree The degree of the spline.";

  cls_Spline
      .def(py::init<>(), release_gil()
  )
    
      .def("getPoint", &frc::Spline<Degree>::GetPoint,
      py::arg("t"), release_gil(), py::doc(
    "Gets the pose and curvature at some point t on the spline.\n"
"\n"
":param t: The point t\n"
"\n"
":returns: The pose and curvature at that point.")
  )
    
;

    
  cls_ControlVector.doc() =
    "Represents a control vector for a spline.\n"
"\n"
"Each element in each array represents the value of the derivative at the\n"
"index. For example, the value of x[2] is the second derivative in the x\n"
"dimension.";

  cls_ControlVector
;

  


    if (set_doc) {
        cls_Spline.doc() = set_doc;
    }
    if (add_doc) {
        cls_Spline.doc() = py::cast<std::string>(cls_Spline.doc()) + add_doc;
    }

    cls_ControlVector
  .def(
    py::init<
      wpi::array<double, (Degree + 1) / 2>,
      wpi::array<double, (Degree + 1) / 2>>(),
    py::arg("x"),
    py::arg("y")
  )
  .def_readwrite("x", &frc::Spline<Degree>::ControlVector::x)
  .def_readwrite("y", &frc::Spline<Degree>::ControlVector::y);

}

}; // struct bind_frc__Spline

}; // namespace rpygen