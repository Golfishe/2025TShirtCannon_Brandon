import constants

import commands2
import commands2.button

import wpilib

# from subsystems.drivetrain import arcadeDrive
# from commands.arcadedrive import ArcadeDrive

from subsystems.limelight import limelightSystem
from commands.limelightdisplay import limelightDisplay
from subsystems.drivetrain import arcadeDrive

class RobotContainer:
    def __init__(self) -> None:
        self.limelight = limelightSystem()
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)
        self.configureButtonBindings()
        validTarget = self.limelight.

    def configureButtonBindings(self) -> None:
        self.limelight.setDefaultCommand(limelightDisplay(self.limelight))
    
    def teleopPeriodic(self) -> None:
        if limelightSystem.get_results().tagId % 2 == 0:
            self.arcadeDrive.arcadeDrive(1.0, 1.0)

        if limelightSystem.get_results().tagId % 2 == 1:
            self.arcadeDrive.arcadeDrive(-1.0, 1.0)
