
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\_impl\include\frc\TimesliceRobot.h>




#include <rpygen/frc__TimedRobot.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__TimesliceRobot =
    PyTrampolineCfg_frc__TimedRobot<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__TimesliceRobot :
    PyTrampolineCfgBase_frc__TimesliceRobot< CfgBase>
{
    using Base = frc::TimesliceRobot;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__TimesliceRobot =
    PyTrampoline_frc__TimedRobot<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__TimesliceRobot : PyTrampolineBase_frc__TimesliceRobot<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__TimesliceRobot<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__TimesliceRobot;






};

}; // namespace rpygen
