
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\..\_impl\include\frc\GenericHID.h>

#include <frc/DriverStation.h>
#include <frc/event/BooleanEvent.h>




namespace rpygen {

using namespace frc;



template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__GenericHID :
    CfgBase
{
    using Base = frc::GenericHID;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__GenericHID : PyTrampolineBase, virtual py::trampoline_self_life_support {
    using PyTrampolineBase::PyTrampolineBase;






};

}; // namespace rpygen
