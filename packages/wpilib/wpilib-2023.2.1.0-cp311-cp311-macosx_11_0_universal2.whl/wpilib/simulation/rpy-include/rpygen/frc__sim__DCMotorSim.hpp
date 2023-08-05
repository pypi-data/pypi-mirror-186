
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <../../_impl/include/frc/simulation/DCMotorSim.h>




#include <rpygen/frc__sim__LinearSystemSim.hpp>

namespace rpygen {

using namespace frc::sim;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__sim__DCMotorSim =
    PyTrampolineCfg_frc__sim__LinearSystemSim<2, 1, 2, 
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__sim__DCMotorSim :
    PyTrampolineCfgBase_frc__sim__DCMotorSim< CfgBase>
{
    using Base = frc::sim::DCMotorSim;

    using override_base_KGetCurrentDraw_v = frc::sim::DCMotorSim;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__sim__DCMotorSim =
    PyTrampoline_frc__sim__LinearSystemSim<
        PyTrampolineBase
        , 2, 1, 2
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__sim__DCMotorSim : PyTrampolineBase_frc__sim__DCMotorSim<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__sim__DCMotorSim<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__sim__DCMotorSim;

    using DCMotor = frc::DCMotor;


#ifndef RPYGEN_DISABLE_KGetCurrentDraw_v
    units::ampere_t GetCurrentDraw() const override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_KGetCurrentDraw_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(units::ampere_t), LookupBase,
            "getCurrentDraw", );
        return CxxCallBase::GetCurrentDraw();
    }
#endif




};

}; // namespace rpygen
