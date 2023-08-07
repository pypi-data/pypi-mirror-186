from __future__ import annotations
import pathplannerlib._pathplannerlib.GeometryUtil
import typing
import wpimath.geometry._geometry

__all__ = [
    "cosineInterpolate",
    "cubicLerp",
    "isFinite",
    "isNaN",
    "modulo",
    "quadraticLerp",
    "rotationLerp",
    "translationLerp",
    "unitLerp"
]


def cosineInterpolate(y1: wpimath.geometry._geometry.Rotation2d, y2: wpimath.geometry._geometry.Rotation2d, mu: float) -> wpimath.geometry._geometry.Rotation2d:
    pass
def cubicLerp(a: wpimath.geometry._geometry.Translation2d, b: wpimath.geometry._geometry.Translation2d, c: wpimath.geometry._geometry.Translation2d, d: wpimath.geometry._geometry.Translation2d, t: float) -> wpimath.geometry._geometry.Translation2d:
    pass
def isFinite(u: meters) -> bool:
    pass
def isNaN(u: meters) -> bool:
    pass
def modulo(a: degrees, b: degrees) -> degrees:
    pass
def quadraticLerp(a: wpimath.geometry._geometry.Translation2d, b: wpimath.geometry._geometry.Translation2d, c: wpimath.geometry._geometry.Translation2d, t: float) -> wpimath.geometry._geometry.Translation2d:
    pass
def rotationLerp(startVal: wpimath.geometry._geometry.Rotation2d, endVal: wpimath.geometry._geometry.Rotation2d, t: float) -> wpimath.geometry._geometry.Rotation2d:
    pass
def translationLerp(startVal: wpimath.geometry._geometry.Translation2d, endVal: wpimath.geometry._geometry.Translation2d, t: float) -> wpimath.geometry._geometry.Translation2d:
    pass
@typing.overload
def unitLerp(startVal: meters, endVal: meters, t: float) -> meters:
    pass
@typing.overload
def unitLerp(startVal: meters_per_second, endVal: meters_per_second, t: float) -> meters_per_second:
    pass
@typing.overload
def unitLerp(startVal: meters_per_second_squared, endVal: meters_per_second_squared, t: float) -> meters_per_second_squared:
    pass
@typing.overload
def unitLerp(startVal: radians_per_meter, endVal: radians_per_meter, t: float) -> radians_per_meter:
    pass
@typing.overload
def unitLerp(startVal: radians_per_second, endVal: radians_per_second, t: float) -> radians_per_second:
    pass
@typing.overload
def unitLerp(startVal: radians_per_second_squared, endVal: radians_per_second_squared, t: float) -> radians_per_second_squared:
    pass
@typing.overload
def unitLerp(startVal: seconds, endVal: seconds, t: float) -> seconds:
    pass
