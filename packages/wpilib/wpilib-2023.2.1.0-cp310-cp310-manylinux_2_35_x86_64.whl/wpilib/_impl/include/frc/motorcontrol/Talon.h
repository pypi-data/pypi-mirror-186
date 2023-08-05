// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#pragma once

#include "frc/motorcontrol/PWMMotorController.h"

namespace frc {

/**
 * Cross the Road Electronics (CTRE) %Talon and %Talon SR Motor %Controller.
 *
 * Note that the %Talon uses the following bounds for PWM values. These values
 * should work reasonably well for most controllers, but if users experience
 * issues such as asymmetric behavior around the deadband or inability to
 * saturate the controller in either direction, calibration is recommended.
 * The calibration procedure can be found in the %Talon User Manual available
 * from CTRE.
 *
 * \li 2.037ms = full "forward"
 * \li 1.539ms = the "high end" of the deadband range
 * \li 1.513ms = center of the deadband range (off)
 * \li 1.487ms = the "low end" of the deadband range
 * \li 0.989ms = full "reverse"
 */
class Talon : public PWMMotorController {
 public:
  /**
   * Constructor for a %Talon (original or %Talon SR).
   *
   * @param channel The PWM channel number that the %Talon is attached to. 0-9
   *                are on-board, 10-19 are on the MXP port
   */
  explicit Talon(int channel);

  Talon(Talon&&) = default;
  Talon& operator=(Talon&&) = default;
};

}  // namespace frc
