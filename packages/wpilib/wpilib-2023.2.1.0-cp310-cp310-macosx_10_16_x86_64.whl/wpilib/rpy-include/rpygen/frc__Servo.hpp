
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <../_impl/include/frc/Servo.h>

#include <wpi/sendable/SendableBuilder.h>



#include <rpygen/frc__PWM.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__Servo =
    PyTrampolineCfg_frc__PWM<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__Servo :
    PyTrampolineCfgBase_frc__Servo< CfgBase>
{
    using Base = frc::Servo;

    using override_base_InitSendable_RTSendableBuilder = frc::Servo;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__Servo =
    PyTrampoline_frc__PWM<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__Servo : PyTrampolineBase_frc__Servo<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__Servo<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__Servo;



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
