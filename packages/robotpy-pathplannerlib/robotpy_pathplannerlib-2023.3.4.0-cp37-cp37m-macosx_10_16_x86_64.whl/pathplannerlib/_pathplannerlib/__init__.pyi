from __future__ import annotations
import pathplannerlib._pathplannerlib
import typing
import wpimath._controls._controls.trajectory
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics

__all__ = [
    "GeometryUtil",
    "PathConstraints",
    "PathPlanner",
    "PathPlannerTrajectory",
    "PathPoint",
    "controllers"
]


class PathConstraints():
    def __init__(self, maxVel: meters_per_second, maxAccel: meters_per_second_squared) -> None: ...
    @property
    def maxAcceleration(self) -> meters_per_second_squared:
        """
        :type: meters_per_second_squared
        """
    @property
    def maxVelocity(self) -> meters_per_second:
        """
        :type: meters_per_second
        """
    pass
class PathPlanner():
    def __init__(self) -> None: ...
    @staticmethod
    @typing.overload
    def generatePath(constraints: PathConstraints, points: typing.List[PathPoint]) -> PathPlannerTrajectory: 
        """
        Generate a path on-the-fly from a list of points
        As you can't see the path in the GUI when using this method, make sure you have a good idea
        of what works well and what doesn't before you use this method in competition. Points positioned in weird
        configurations such as being too close together can lead to really janky paths.

        :param constraints: The max velocity and max acceleration of the path
        :param reversed:    Should the robot follow this path reversed
        :param points:      Points in the path

        :returns: The generated path

        Generate a path on-the-fly from a list of points
        As you can't see the path in the GUI when using this method, make sure you have a good idea
        of what works well and what doesn't before you use this method in competition. Points positioned in weird
        configurations such as being too close together can lead to really janky paths.

        :param constraints: The max velocity and max acceleration of the path
        :param reversed:    Should the robot follow this path reversed
        :param points:      Points in the path

        :returns: The generated path
        """
    @staticmethod
    @typing.overload
    def generatePath(constraints: PathConstraints, reversed: bool, points: typing.List[PathPoint]) -> PathPlannerTrajectory: ...
    @staticmethod
    def getConstraintsFromPath(name: str) -> PathConstraints: 
        """
        Load path constraints from a path file in storage. This can be used to change path max vel/accel in the
        GUI instead of updating and rebuilding code. This requires that max velocity and max acceleration have been
        explicitly set in the GUI.

        Throws a runtime error if constraints are not present in the file

        :param name: The name of the path to load constraints from

        :returns: The constraints from the path file
        """
    @staticmethod
    @typing.overload
    def loadPath(name: str, constraints: PathConstraints, reversed: bool = False) -> PathPlannerTrajectory: 
        """
        Load a path file from storage

        :param name:        The name of the path to load
        :param constraints: The max velocity and acceleration of the path
        :param reversed:    Should the robot follow the path reversed

        :returns: The generated path

        Load a path file from storage

        :param name:     The name of the path to load
        :param maxVel:   Max velocity of the path
        :param maxAccel: Max acceleration of the path
        :param reversed: Should the robot follow the path reversed

        :returns: The generated path
        """
    @staticmethod
    @typing.overload
    def loadPath(name: str, maxVel: meters_per_second, maxAccel: meters_per_second_squared, reversed: bool = False) -> PathPlannerTrajectory: ...
    @staticmethod
    @typing.overload
    def loadPathGroup(name: str, constraints: typing.List[PathConstraints], reversed: bool = False) -> typing.List[PathPlannerTrajectory]: 
        """
        Load a path file from storage as a path group. This will separate the path into multiple paths based on the waypoints marked as "stop points"

        :param name:        The name of the path group to load
        :param constraints: Vector of path constraints for each path in the group. This requires at least one path constraint. If less constraints than paths are provided, the last constraint will be used for the rest of the paths.
        :param reversed:    Should the robot follow the path group reversed

        :returns: Vector of all generated paths in the group

        Load a path file from storage as a path group. This will separate the path into multiple paths based on the waypoints marked as "stop points"

        :param name:     The name of the path group to load
        :param maxVel:   Max velocity of every path in the group
        :param maxAccel: Max acceleration of every path in the group
        :param reversed: Should the robot follow the path group reversed

        :returns: Vector of all generated paths in the group
        """
    @staticmethod
    @typing.overload
    def loadPathGroup(name: str, maxVel: meters_per_second, maxAccel: meters_per_second_squared, reversed: bool = False) -> typing.List[PathPlannerTrajectory]: ...
    resolution = 0.004
    pass
class PathPlannerTrajectory():
    class EventMarker():
        @property
        def names(self) -> typing.List[str]:
            """
            :type: typing.List[str]
            """
        @property
        def position(self) -> wpimath.geometry._geometry.Translation2d:
            """
            :type: wpimath.geometry._geometry.Translation2d
            """
        @property
        def time(self) -> seconds:
            """
            :type: seconds
            """
        pass
    class PathPlannerState():
        def __init__(self) -> None: ...
        def asWPILibState(self) -> wpimath._controls._controls.trajectory.Trajectory.State: 
            """
            Get this state as a WPILib trajectory state

            :returns: The WPILib state
            """
        @property
        def acceleration(self) -> meters_per_second_squared:
            """
            :type: meters_per_second_squared
            """
        @property
        def angularVelocity(self) -> radians_per_second:
            """
            :type: radians_per_second
            """
        @property
        def holonomicAngularVelocity(self) -> radians_per_second:
            """
            :type: radians_per_second
            """
        @property
        def holonomicRotation(self) -> wpimath.geometry._geometry.Rotation2d:
            """
            :type: wpimath.geometry._geometry.Rotation2d
            """
        @property
        def pose(self) -> wpimath.geometry._geometry.Pose2d:
            """
            :type: wpimath.geometry._geometry.Pose2d
            """
        @property
        def time(self) -> seconds:
            """
            :type: seconds
            """
        @property
        def velocity(self) -> meters_per_second:
            """
            :type: meters_per_second
            """
        pass
    class StopEvent():
        class ExecutionBehavior():
            """
            Members:

              PARALLEL

              SEQUENTIAL

              PARALLEL_DEADLINE
            """
            def __eq__(self, other: object) -> bool: ...
            def __getstate__(self) -> int: ...
            def __hash__(self) -> int: ...
            def __index__(self) -> int: ...
            def __init__(self, value: int) -> None: ...
            def __int__(self) -> int: ...
            def __ne__(self, other: object) -> bool: ...
            def __repr__(self) -> str: ...
            def __setstate__(self, state: int) -> None: ...
            @property
            def name(self) -> str:
                """
                :type: str
                """
            @property
            def value(self) -> int:
                """
                :type: int
                """
            PARALLEL: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.ExecutionBehavior # value = <ExecutionBehavior.PARALLEL: 0>
            PARALLEL_DEADLINE: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.ExecutionBehavior # value = <ExecutionBehavior.PARALLEL_DEADLINE: 2>
            SEQUENTIAL: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.ExecutionBehavior # value = <ExecutionBehavior.SEQUENTIAL: 1>
            __members__: dict # value = {'PARALLEL': <ExecutionBehavior.PARALLEL: 0>, 'SEQUENTIAL': <ExecutionBehavior.SEQUENTIAL: 1>, 'PARALLEL_DEADLINE': <ExecutionBehavior.PARALLEL_DEADLINE: 2>}
            pass
        class WaitBehavior():
            """
            Members:

              NONE

              BEFORE

              AFTER

              DEADLINE

              MINIMUM
            """
            def __eq__(self, other: object) -> bool: ...
            def __getstate__(self) -> int: ...
            def __hash__(self) -> int: ...
            def __index__(self) -> int: ...
            def __init__(self, value: int) -> None: ...
            def __int__(self) -> int: ...
            def __ne__(self, other: object) -> bool: ...
            def __repr__(self) -> str: ...
            def __setstate__(self, state: int) -> None: ...
            @property
            def name(self) -> str:
                """
                :type: str
                """
            @property
            def value(self) -> int:
                """
                :type: int
                """
            AFTER: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.WaitBehavior # value = <WaitBehavior.AFTER: 2>
            BEFORE: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.WaitBehavior # value = <WaitBehavior.BEFORE: 1>
            DEADLINE: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.WaitBehavior # value = <WaitBehavior.DEADLINE: 3>
            MINIMUM: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.WaitBehavior # value = <WaitBehavior.MINIMUM: 4>
            NONE: pathplannerlib._pathplannerlib.PathPlannerTrajectory.StopEvent.WaitBehavior # value = <WaitBehavior.NONE: 0>
            __members__: dict # value = {'NONE': <WaitBehavior.NONE: 0>, 'BEFORE': <WaitBehavior.BEFORE: 1>, 'AFTER': <WaitBehavior.AFTER: 2>, 'DEADLINE': <WaitBehavior.DEADLINE: 3>, 'MINIMUM': <WaitBehavior.MINIMUM: 4>}
            pass
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, names: typing.List[str], executionBehavior: PathPlannerTrajectory.StopEvent.ExecutionBehavior, waitBehavior: PathPlannerTrajectory.StopEvent.WaitBehavior, waitTime: seconds) -> None: ...
        @property
        def executionBehavior(self) -> PathPlannerTrajectory.StopEvent.ExecutionBehavior:
            """
            :type: PathPlannerTrajectory.StopEvent.ExecutionBehavior
            """
        @executionBehavior.setter
        def executionBehavior(self, arg0: PathPlannerTrajectory.StopEvent.ExecutionBehavior) -> None:
            pass
        @property
        def names(self) -> typing.List[str]:
            """
            :type: typing.List[str]
            """
        @property
        def waitBehavior(self) -> PathPlannerTrajectory.StopEvent.WaitBehavior:
            """
            :type: PathPlannerTrajectory.StopEvent.WaitBehavior
            """
        @waitBehavior.setter
        def waitBehavior(self, arg0: PathPlannerTrajectory.StopEvent.WaitBehavior) -> None:
            pass
        @property
        def waitTime(self) -> seconds:
            """
            :type: seconds
            """
        pass
    def __init__(self) -> None: ...
    def asWPILibTrajectory(self) -> wpimath._controls._controls.trajectory.Trajectory: 
        """
        Convert this path to a WPILib compatible trajectory

        :returns: The path as a WPILib trajectory
        """
    def getEndState(self) -> PathPlannerTrajectory.PathPlannerState: 
        """
        Get the end state of the path

        :returns: Reference to the last state in the path
        """
    def getEndStopEvent(self) -> PathPlannerTrajectory.StopEvent: 
        """
        Get the "stop event" for the end of the path

        :returns: The end stop event
        """
    def getInitialHolonomicPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Get the inital pose of a holonomic drive robot in the path

        :returns: The initial pose
        """
    def getInitialPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Get the inital pose of a differential drive robot in the path

        :returns: The initial pose
        """
    def getInitialState(self) -> PathPlannerTrajectory.PathPlannerState: 
        """
        Get the initial state of the path

        :returns: Reference to the first state of the path
        """
    def getMarkers(self) -> typing.List[PathPlannerTrajectory.EventMarker]: 
        """
        Get all of the markers in the path

        :returns: Reference to a vector of all markers
        """
    def getStartStopEvent(self) -> PathPlannerTrajectory.StopEvent: 
        """
        Get the "stop event" for the beginning of the path

        :returns: The start stop event
        """
    def getState(self, i: int) -> PathPlannerTrajectory.PathPlannerState: 
        """
        Get a state in the path based on its index. In most cases, using sample() is a better method.

        :param i: The index of the state

        :returns: Reference to the state at the given index
        """
    def getStates(self) -> typing.List[PathPlannerTrajectory.PathPlannerState]: 
        """
        Get all of the states in the path

        :returns: Reference to a vector of all states
        """
    def getTotalTime(self) -> seconds: 
        """
        Get the total runtime of the path

        :returns: The path runtime
        """
    def numStates(self) -> int: 
        """
        Get the total number of states in the path

        :returns: The number of states
        """
    def sample(self, time: seconds) -> PathPlannerTrajectory.PathPlannerState: 
        """
        Sample the path at a point in time

        :param time: The time to sample

        :returns: The state at the given point in time
        """
    @staticmethod
    def transformStateForAlliance(state: PathPlannerTrajectory.PathPlannerState, alliance: wpilib._wpilib.DriverStation.Alliance) -> PathPlannerTrajectory.PathPlannerState: ...
    @staticmethod
    def transformTrajectoryForAlliance(trajectory: PathPlannerTrajectory, alliance: wpilib._wpilib.DriverStation.Alliance) -> PathPlannerTrajectory: ...
    @property
    def fromGUI(self) -> bool:
        """
        :type: bool
        """
    @fromGUI.setter
    def fromGUI(self, arg0: bool) -> None:
        pass
    pass
class PathPoint():
    @typing.overload
    def __init__(self, position: wpimath.geometry._geometry.Translation2d, heading: wpimath.geometry._geometry.Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, position: wpimath.geometry._geometry.Translation2d, heading: wpimath.geometry._geometry.Rotation2d, holonomicRotation: wpimath.geometry._geometry.Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, position: wpimath.geometry._geometry.Translation2d, heading: wpimath.geometry._geometry.Rotation2d, holonomicRotation: wpimath.geometry._geometry.Rotation2d, velocityOverride: meters_per_second) -> None: ...
    @typing.overload
    def __init__(self, position: wpimath.geometry._geometry.Translation2d, heading: wpimath.geometry._geometry.Rotation2d, velocityOverride: meters_per_second) -> None: ...
    @staticmethod
    def fromCurrentDifferentialState(currentPose: wpimath.geometry._geometry.Pose2d, currentSpeeds: wpimath.kinematics._kinematics.ChassisSpeeds) -> PathPoint: ...
    @staticmethod
    def fromCurrentHolonomicState(currentPose: wpimath.geometry._geometry.Pose2d, currentSpeeds: wpimath.kinematics._kinematics.ChassisSpeeds) -> PathPoint: ...
    def withControlLengths(self, prevLength: meters, nextLength: meters) -> PathPoint: ...
    def withNextControlLength(self, length: meters) -> PathPoint: ...
    def withPrevControlLength(self, length: meters) -> PathPoint: ...
    @property
    def m_heading(self) -> wpimath.geometry._geometry.Rotation2d:
        """
        :type: wpimath.geometry._geometry.Rotation2d
        """
    @property
    def m_holonomicRotation(self) -> wpimath.geometry._geometry.Rotation2d:
        """
        :type: wpimath.geometry._geometry.Rotation2d
        """
    @property
    def m_nextControlLength(self) -> meters:
        """
        :type: meters
        """
    @property
    def m_position(self) -> wpimath.geometry._geometry.Translation2d:
        """
        :type: wpimath.geometry._geometry.Translation2d
        """
    @property
    def m_prevControlLength(self) -> meters:
        """
        :type: meters
        """
    @property
    def m_velocityOverride(self) -> meters_per_second:
        """
        :type: meters_per_second
        """
    pass
