
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\_impl\include\frc\motorcontrol\PWMSparkMax.h>

#include <wpi/sendable/SendableBuilder.h>



#include <rpygen/frc__PWMMotorController.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__PWMSparkMax =
    PyTrampolineCfg_frc__PWMMotorController<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__PWMSparkMax :
    PyTrampolineCfgBase_frc__PWMSparkMax< CfgBase>
{
    using Base = frc::PWMSparkMax;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__PWMSparkMax =
    PyTrampoline_frc__PWMMotorController<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__PWMSparkMax : PyTrampolineBase_frc__PWMSparkMax<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__PWMSparkMax<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__PWMSparkMax;






};

}; // namespace rpygen
