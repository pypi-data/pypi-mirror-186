
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\_impl\include\frc\motorcontrol\DMC60.h>

#include <wpi/sendable/SendableBuilder.h>



#include <rpygen/frc__PWMMotorController.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__DMC60 =
    PyTrampolineCfg_frc__PWMMotorController<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__DMC60 :
    PyTrampolineCfgBase_frc__DMC60< CfgBase>
{
    using Base = frc::DMC60;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__DMC60 =
    PyTrampoline_frc__PWMMotorController<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__DMC60 : PyTrampolineBase_frc__DMC60<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__DMC60<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__DMC60;






};

}; // namespace rpygen
