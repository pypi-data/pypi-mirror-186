
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\..\_impl\include\frc\simulation\SingleJointedArmSim.h>




#include <rpygen/frc__sim__LinearSystemSim.hpp>

namespace rpygen {

using namespace frc::sim;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__sim__SingleJointedArmSim =
    PyTrampolineCfg_frc__sim__LinearSystemSim<2, 1, 1, 
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__sim__SingleJointedArmSim :
    PyTrampolineCfgBase_frc__sim__SingleJointedArmSim< CfgBase>
{
    using Base = frc::sim::SingleJointedArmSim;

    using override_base_KGetCurrentDraw_v = frc::sim::SingleJointedArmSim;
    using override_base_UpdateX_KRTVectord_2__KRTVectord_1__Tsecond_t = frc::sim::SingleJointedArmSim;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__sim__SingleJointedArmSim =
    PyTrampoline_frc__sim__LinearSystemSim<
        PyTrampolineBase
        , 2, 1, 1
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__sim__SingleJointedArmSim : PyTrampolineBase_frc__sim__SingleJointedArmSim<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__sim__SingleJointedArmSim<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__sim__SingleJointedArmSim;

    using DCMotor = frc::DCMotor;
    template <int S, int I, int O> using LinearSystem = frc::LinearSystem<S, I, O>;
    template <int I> using Vectord = frc::Vectord<I>;


#ifndef RPYGEN_DISABLE_KGetCurrentDraw_v
    units::ampere_t GetCurrentDraw() const override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_KGetCurrentDraw_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(units::ampere_t), LookupBase,
            "getCurrentDraw", );
        return CxxCallBase::GetCurrentDraw();
    }
#endif

#ifndef RPYGEN_DISABLE_UpdateX_KRTVectord_2__KRTVectord_1__Tsecond_t
    Vectord<2 > UpdateX(const Vectord<2>& currentXhat, const Vectord<1>& u, units::second_t dt) override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_UpdateX_KRTVectord_2__KRTVectord_1__Tsecond_t;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(Vectord<2 >), LookupBase,
            "_updateX", currentXhat, u, dt);
        return CxxCallBase::UpdateX(std::forward<decltype(currentXhat)>(currentXhat), std::forward<decltype(u)>(u), std::move(dt));
    }
#endif




};

}; // namespace rpygen
