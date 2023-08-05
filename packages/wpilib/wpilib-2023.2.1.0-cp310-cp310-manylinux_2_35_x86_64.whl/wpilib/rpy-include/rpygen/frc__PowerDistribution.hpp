
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <../_impl/include/frc/PowerDistribution.h>

#include <wpi/sendable/SendableBuilder.h>



#include <rpygen/wpi__Sendable.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__PowerDistribution =
    PyTrampolineCfg_wpi__Sendable<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__PowerDistribution :
    PyTrampolineCfgBase_frc__PowerDistribution< CfgBase>
{
    using Base = frc::PowerDistribution;

    using override_base_InitSendable_RTSendableBuilder = frc::PowerDistribution;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__PowerDistribution =
    PyTrampoline_wpi__Sendable<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__PowerDistribution : PyTrampolineBase_frc__PowerDistribution<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__PowerDistribution<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__PowerDistribution;



#ifndef RPYGEN_DISABLE_InitSendable_RTSendableBuilder
    void InitSendable(wpi::SendableBuilder& builder) override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_InitSendable_RTSendableBuilder;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "initSendable", builder);
        return CxxCallBase::InitSendable(std::forward<decltype(builder)>(builder));
    }
#endif




};

}; // namespace rpygen
