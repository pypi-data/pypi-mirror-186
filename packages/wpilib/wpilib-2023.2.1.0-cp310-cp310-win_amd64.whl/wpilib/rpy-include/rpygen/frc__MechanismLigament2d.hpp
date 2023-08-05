
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\_impl\include\frc\smartdashboard\MechanismLigament2d.h>




#include <rpygen/frc__MechanismObject2d.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__MechanismLigament2d =
    PyTrampolineCfg_frc__MechanismObject2d<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__MechanismLigament2d :
    PyTrampolineCfgBase_frc__MechanismLigament2d< CfgBase>
{
    using Base = frc::MechanismLigament2d;

    using override_base_UpdateEntries_TNetworkTable_ = frc::MechanismLigament2d;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__MechanismLigament2d =
    PyTrampoline_frc__MechanismObject2d<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__MechanismLigament2d : PyTrampolineBase_frc__MechanismLigament2d<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__MechanismLigament2d<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__MechanismLigament2d;



#ifndef RPYGEN_DISABLE_UpdateEntries_TNetworkTable_
    void UpdateEntries(std::shared_ptr<nt::NetworkTable > table) override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_UpdateEntries_TNetworkTable_;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "_updateEntries", table);
        return CxxCallBase::UpdateEntries(std::move(table));
    }
#endif




};

}; // namespace rpygen
