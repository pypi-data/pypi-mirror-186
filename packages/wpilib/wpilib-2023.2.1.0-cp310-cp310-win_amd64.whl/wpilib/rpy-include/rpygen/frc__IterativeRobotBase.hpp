
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\_impl\include\frc\IterativeRobotBase.h>




#include <rpygen/frc__RobotBase.hpp>

namespace rpygen {

using namespace frc;


template <typename CfgBase>
using PyTrampolineCfgBase_frc__IterativeRobotBase =
    PyTrampolineCfg_frc__RobotBase<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc__IterativeRobotBase :
    PyTrampolineCfgBase_frc__IterativeRobotBase< CfgBase>
{
    using Base = frc::IterativeRobotBase;

    using override_base_RobotInit_v = frc::IterativeRobotBase;
    using override_base_SimulationInit_v = frc::IterativeRobotBase;
    using override_base_DisabledInit_v = frc::IterativeRobotBase;
    using override_base_AutonomousInit_v = frc::IterativeRobotBase;
    using override_base_TeleopInit_v = frc::IterativeRobotBase;
    using override_base_TestInit_v = frc::IterativeRobotBase;
    using override_base_RobotPeriodic_v = frc::IterativeRobotBase;
    using override_base_SimulationPeriodic_v = frc::IterativeRobotBase;
    using override_base_DisabledPeriodic_v = frc::IterativeRobotBase;
    using override_base_AutonomousPeriodic_v = frc::IterativeRobotBase;
    using override_base_TeleopPeriodic_v = frc::IterativeRobotBase;
    using override_base_TestPeriodic_v = frc::IterativeRobotBase;
    using override_base_DisabledExit_v = frc::IterativeRobotBase;
    using override_base_AutonomousExit_v = frc::IterativeRobotBase;
    using override_base_TeleopExit_v = frc::IterativeRobotBase;
    using override_base_TestExit_v = frc::IterativeRobotBase;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc__IterativeRobotBase =
    PyTrampoline_frc__RobotBase<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc__IterativeRobotBase : PyTrampolineBase_frc__IterativeRobotBase<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc__IterativeRobotBase<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc__IterativeRobotBase;



#ifndef RPYGEN_DISABLE_RobotInit_v
    void RobotInit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_RobotInit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "robotInit", );
        return CxxCallBase::RobotInit();
    }
#endif

#ifndef RPYGEN_DISABLE_SimulationInit_v
    void SimulationInit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_SimulationInit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "_simulationInit", );
        return CxxCallBase::SimulationInit();
    }
#endif

#ifndef RPYGEN_DISABLE_DisabledInit_v
    void DisabledInit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_DisabledInit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "disabledInit", );
        return CxxCallBase::DisabledInit();
    }
#endif

#ifndef RPYGEN_DISABLE_AutonomousInit_v
    void AutonomousInit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_AutonomousInit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "autonomousInit", );
        return CxxCallBase::AutonomousInit();
    }
#endif

#ifndef RPYGEN_DISABLE_TeleopInit_v
    void TeleopInit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_TeleopInit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "teleopInit", );
        return CxxCallBase::TeleopInit();
    }
#endif

#ifndef RPYGEN_DISABLE_TestInit_v
    void TestInit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_TestInit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "testInit", );
        return CxxCallBase::TestInit();
    }
#endif

#ifndef RPYGEN_DISABLE_RobotPeriodic_v
    void RobotPeriodic() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_RobotPeriodic_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "robotPeriodic", );
        return CxxCallBase::RobotPeriodic();
    }
#endif

#ifndef RPYGEN_DISABLE_SimulationPeriodic_v
    void SimulationPeriodic() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_SimulationPeriodic_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "_simulationPeriodic", );
        return CxxCallBase::SimulationPeriodic();
    }
#endif

#ifndef RPYGEN_DISABLE_DisabledPeriodic_v
    void DisabledPeriodic() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_DisabledPeriodic_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "disabledPeriodic", );
        return CxxCallBase::DisabledPeriodic();
    }
#endif

#ifndef RPYGEN_DISABLE_AutonomousPeriodic_v
    void AutonomousPeriodic() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_AutonomousPeriodic_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "autonomousPeriodic", );
        return CxxCallBase::AutonomousPeriodic();
    }
#endif

#ifndef RPYGEN_DISABLE_TeleopPeriodic_v
    void TeleopPeriodic() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_TeleopPeriodic_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "teleopPeriodic", );
        return CxxCallBase::TeleopPeriodic();
    }
#endif

#ifndef RPYGEN_DISABLE_TestPeriodic_v
    void TestPeriodic() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_TestPeriodic_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "testPeriodic", );
        return CxxCallBase::TestPeriodic();
    }
#endif

#ifndef RPYGEN_DISABLE_DisabledExit_v
    void DisabledExit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_DisabledExit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "disabledExit", );
        return CxxCallBase::DisabledExit();
    }
#endif

#ifndef RPYGEN_DISABLE_AutonomousExit_v
    void AutonomousExit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_AutonomousExit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "autonomousExit", );
        return CxxCallBase::AutonomousExit();
    }
#endif

#ifndef RPYGEN_DISABLE_TeleopExit_v
    void TeleopExit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_TeleopExit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "teleopExit", );
        return CxxCallBase::TeleopExit();
    }
#endif

#ifndef RPYGEN_DISABLE_TestExit_v
    void TestExit() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_TestExit_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "testExit", );
        return CxxCallBase::TestExit();
    }
#endif


#ifndef RPYBLD_DISABLE_LoopFunc_v
  #ifndef RPYBLD_UDISABLE_frc__IterativeRobotBase_LoopFunc
    using frc::IterativeRobotBase::LoopFunc;
    #define RPYBLD_UDISABLE_frc__IterativeRobotBase_LoopFunc
  #endif
#endif


};

}; // namespace rpygen
