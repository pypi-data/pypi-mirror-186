
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <../_impl/include/frc/ADIS16470_IMU.h>

#include <networktables/NTSendableBuilder.h>



#include <rpygen/nt__NTSendable.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__ADIS16470_IMU =
    PyTrampolineCfg_nt__NTSendable<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__ADIS16470_IMU :
    PyTrampolineCfgBase_frc__ADIS16470_IMU< CfgBase>
{
    using Base = frc::ADIS16470_IMU;

    using override_base_InitSendable_RTNTSendableBuilder = frc::ADIS16470_IMU;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__ADIS16470_IMU =
    PyTrampoline_nt__NTSendable<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__ADIS16470_IMU : PyTrampolineBase_frc__ADIS16470_IMU<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__ADIS16470_IMU<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__ADIS16470_IMU;



#ifndef RPYGEN_DISABLE_InitSendable_RTNTSendableBuilder
    void InitSendable(nt::NTSendableBuilder& builder) override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_InitSendable_RTNTSendableBuilder;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "initSendable", builder);
        return CxxCallBase::InitSendable(std::forward<decltype(builder)>(builder));
    }
#endif




};

}; // namespace rpygen
