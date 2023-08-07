from __future__ import annotations
import pathplannerlib._pathplannerlib.controllers
import typing
import wpimath._controls._controls.controller
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics

__all__ = [
    "PPHolonomicDriveController"
]


class PPHolonomicDriveController():
    def __init__(self, xController: wpimath._controls._controls.controller.PIDController, yController: wpimath._controls._controls.controller.PIDController, rotationController: wpimath._controls._controls.controller.PIDController) -> None: 
        """
        Constructs a PPHolonomicDriveController

        :param xController:        A PID controller to respond to error in the field-relative X direction
        :param yController:        A PID controller to respond to error in the field-relative Y direction
        :param rotationController: A PID controller to respond to error in rotation
        """
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.

        :returns: True if the pose error is within tolerance of the reference.
        """
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, referenceState: pathplannerlib._pathplannerlib.PathPlannerTrajectory.PathPlannerState) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Calculates the next output of the holonomic drive controller

        :param currentPose:    The current pose
        :param referenceState: The desired trajectory state

        :returns: The next output of the holonomic drive controller
        """
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting. When calculate() is called on a disabled
        controller, only feedforward values are returned.

        :param enabled: If the controller is enabled or not
        """
    def setTolerance(self, tolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error whic is considered tolerance for use with atReference()

        :param tolerance: The pose error which is tolerable
        """
    pass
