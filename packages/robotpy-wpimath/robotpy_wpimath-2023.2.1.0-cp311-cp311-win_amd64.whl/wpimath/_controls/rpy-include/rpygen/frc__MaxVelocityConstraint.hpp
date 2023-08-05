
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\..\_impl\include\frc\trajectory\constraint\MaxVelocityConstraint.h>




#include <rpygen/frc__TrajectoryConstraint.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__MaxVelocityConstraint =
    PyTrampolineCfg_frc__TrajectoryConstraint<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__MaxVelocityConstraint :
    PyTrampolineCfgBase_frc__MaxVelocityConstraint< CfgBase>
{
    using Base = frc::MaxVelocityConstraint;

    using override_base_KMaxVelocity_KRTPose2d_Tcurvature_t_Tmeters_per_second_t = frc::MaxVelocityConstraint;
    using override_base_KMinMaxAcceleration_KRTPose2d_Tcurvature_t_Tmeters_per_second_t = frc::MaxVelocityConstraint;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__MaxVelocityConstraint =
    PyTrampoline_frc__TrajectoryConstraint<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__MaxVelocityConstraint : PyTrampolineBase_frc__MaxVelocityConstraint<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__MaxVelocityConstraint<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__MaxVelocityConstraint;

    using MinMax = frc::TrajectoryConstraint::MinMax;


#ifndef RPYGEN_DISABLE_KMaxVelocity_KRTPose2d_Tcurvature_t_Tmeters_per_second_t
    units::meters_per_second_t MaxVelocity(const Pose2d& pose, units::curvature_t curvature, units::meters_per_second_t velocity) const override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_KMaxVelocity_KRTPose2d_Tcurvature_t_Tmeters_per_second_t;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(units::meters_per_second_t), LookupBase,
            "maxVelocity", pose, curvature, velocity);
        return CxxCallBase::MaxVelocity(std::forward<decltype(pose)>(pose), std::move(curvature), std::move(velocity));
    }
#endif

#ifndef RPYGEN_DISABLE_KMinMaxAcceleration_KRTPose2d_Tcurvature_t_Tmeters_per_second_t
    MinMax MinMaxAcceleration(const Pose2d& pose, units::curvature_t curvature, units::meters_per_second_t speed) const override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_KMinMaxAcceleration_KRTPose2d_Tcurvature_t_Tmeters_per_second_t;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(MinMax), LookupBase,
            "minMaxAcceleration", pose, curvature, speed);
        return CxxCallBase::MinMaxAcceleration(std::forward<decltype(pose)>(pose), std::move(curvature), std::move(speed));
    }
#endif




};

}; // namespace rpygen
