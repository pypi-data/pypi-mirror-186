from __future__ import annotations
import wpimath._controls._controls.controller
import typing
import wpimath._controls._controls.system
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics
import wpiutil._wpiutil

__all__ = [
    "ArmFeedforward",
    "BangBangController",
    "ControlAffinePlantInversionFeedforward_1_1",
    "ControlAffinePlantInversionFeedforward_2_1",
    "ControlAffinePlantInversionFeedforward_2_2",
    "DifferentialDriveAccelerationLimiter",
    "DifferentialDriveWheelVoltages",
    "ElevatorFeedforward",
    "HolonomicDriveController",
    "ImplicitModelFollower_1_1",
    "ImplicitModelFollower_2_1",
    "ImplicitModelFollower_2_2",
    "LTVDifferentialDriveController",
    "LTVUnicycleController",
    "LinearPlantInversionFeedforward_1_1",
    "LinearPlantInversionFeedforward_2_1",
    "LinearPlantInversionFeedforward_2_2",
    "LinearQuadraticRegulator_1_1",
    "LinearQuadraticRegulator_2_1",
    "LinearQuadraticRegulator_2_2",
    "PIDController",
    "ProfiledPIDController",
    "ProfiledPIDControllerRadians",
    "RamseteController",
    "SimpleMotorFeedforwardMeters"
]


class ArmFeedforward():
    """
    A helper class that computes feedforward outputs for a simple arm (modeled as
    a motor acting against the force of gravity on a beam suspended at an angle).
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new ArmFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kG: The gravity gain, in volts.
        :param kV: The velocity gain, in volt seconds per radian.
        :param kA: The acceleration gain, in volt seconds² per radian.
        """
    @typing.overload
    def __init__(self, kS: volts, kG: volts, kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian = 0.0) -> None: ...
    def calculate(self, angle: radians, velocity: radians_per_second, acceleration: radians_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param angle:        The angle setpoint, in radians. This angle should be
                             measured from the horizontal (i.e. if the provided
                             angle is 0, the arm should be parallel to the floor).
                             If your encoder does not follow this convention, an
                             offset should be added.
        :param velocity:     The velocity setpoint, in radians per second.
        :param acceleration: The acceleration setpoint, in radians per second².

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, angle: radians, velocity: radians_per_second) -> radians_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply, a position, and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the arm.
        :param angle:      The angle of the arm. This angle should be measured
                           from the horizontal (i.e. if the provided angle is 0,
                           the arm should be parallel to the floor). If your
                           encoder does not follow this convention, an offset
                           should be added.
        :param velocity:   The velocity of the arm.

        :returns: The maximum possible acceleration at the given velocity and angle.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, angle: radians, acceleration: radians_per_second_squared) -> radians_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply,
        a position, and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the arm.
        :param angle:        The angle of the arm. This angle should be measured
                             from the horizontal (i.e. if the provided angle is 0,
                             the arm should be parallel to the floor). If your
                             encoder does not follow this convention, an offset
                             should be added.
        :param acceleration: The acceleration of the arm.

        :returns: The maximum possible velocity at the given acceleration and angle.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, angle: radians, velocity: radians_per_second) -> radians_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply, a position, and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the arm.
        :param angle:      The angle of the arm. This angle should be measured
                           from the horizontal (i.e. if the provided angle is 0,
                           the arm should be parallel to the floor). If your
                           encoder does not follow this convention, an offset
                           should be added.
        :param velocity:   The velocity of the arm.

        :returns: The minimum possible acceleration at the given velocity and angle.
        """
    def minAchievableVelocity(self, maxVoltage: volts, angle: radians, acceleration: radians_per_second_squared) -> radians_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply,
        a position, and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the arm.
        :param angle:        The angle of the arm. This angle should be measured
                             from the horizontal (i.e. if the provided angle is 0,
                             the arm should be parallel to the floor). If your
                             encoder does not follow this convention, an offset
                             should be added.
        :param acceleration: The acceleration of the arm.

        :returns: The minimum possible velocity at the given acceleration and angle.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_radian:
        """
        :type: volt_seconds_squared_per_radian
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_radian) -> None:
        pass
    @property
    def kG(self) -> volts:
        """
        :type: volts
        """
    @kG.setter
    def kG(self, arg0: volts) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_radian:
        """
        :type: volt_seconds_per_radian
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_radian) -> None:
        pass
    pass
class BangBangController(wpiutil._wpiutil.Sendable):
    """
    Implements a bang-bang controller, which outputs either 0 or 1 depending on
    whether the measurement is less than the setpoint. This maximally-aggressive
    control approach works very well for velocity control of high-inertia
    mechanisms, and poorly on most other things.

    Note that this is an *asymmetric* bang-bang controller - it will not exert
    any control effort in the reverse direction (e.g. it won't try to slow down
    an over-speeding shooter wheel). This asymmetry is *extremely important.*
    Bang-bang control is extremely simple, but also potentially hazardous. Always
    ensure that your motor controllers are set to "coast" before attempting to
    control them with a bang-bang controller.
    """
    def __init__(self, tolerance: float = inf) -> None: 
        """
        Creates a new bang-bang controller.

        Always ensure that your motor controllers are set to "coast" before
        attempting to control them with a bang-bang controller.

        :param tolerance: Tolerance for atSetpoint.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the setpoint.

        :returns: Whether the error is within the acceptable bounds.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the calculated control output.

        Always ensure that your motor controllers are set to "coast" before
        attempting to control them with a bang-bang controller.

        :param measurement: The most recent measurement of the process variable.
        :param setpoint:    The setpoint for the process variable.

        :returns: The calculated motor output (0 or 1).

        Returns the calculated control output.

        :param measurement: The most recent measurement of the process variable.

        :returns: The calculated motor output (0 or 1).
        """
    @typing.overload
    def calculate(self, measurement: float, setpoint: float) -> float: ...
    def getError(self) -> float: 
        """
        Returns the current error.

        :returns: The current error.
        """
    def getMeasurement(self) -> float: 
        """
        Returns the current measurement of the process variable.

        :returns: The current measurement of the process variable.
        """
    def getSetpoint(self) -> float: 
        """
        Returns the current setpoint of the bang-bang controller.

        :returns: The current setpoint.
        """
    def getTolerance(self) -> float: 
        """
        Returns the current tolerance of the controller.

        :returns: The current tolerance.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def setSetpoint(self, setpoint: float) -> None: 
        """
        Sets the setpoint for the bang-bang controller.

        :param setpoint: The desired setpoint.
        """
    def setTolerance(self, tolerance: float) -> None: 
        """
        Sets the error within which AtSetpoint will return true.

        :param tolerance: Position error which is tolerable.
        """
    pass
class ControlAffinePlantInversionFeedforward_1_1():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs the number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const StateVector&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ControlAffinePlantInversionFeedforward_2_1():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs the number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const StateVector&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ControlAffinePlantInversionFeedforward_2_2():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs the number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const StateVector&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class DifferentialDriveAccelerationLimiter():
    """
    Filters the provided voltages to limit a differential drive's linear and
    angular acceleration.

    The differential drive model can be created via the functions in
    LinearSystemId.
    """
    @typing.overload
    def __init__(self, system: wpimath._controls._controls.system.LinearSystem_2_2_2, trackwidth: meters, maxLinearAccel: meters_per_second_squared, maxAngularAccel: radians_per_second_squared) -> None: 
        """
        Constructs a DifferentialDriveAccelerationLimiter.

        :param system:          The differential drive dynamics.
        :param trackwidth:      The distance between the differential drive's left and
                                right wheels.
        :param maxLinearAccel:  The maximum linear acceleration.
        :param maxAngularAccel: The maximum angular acceleration.

        Constructs a DifferentialDriveAccelerationLimiter.

        :param system:          The differential drive dynamics.
        :param trackwidth:      The distance between the differential drive's left and
                                right wheels.
        :param minLinearAccel:  The minimum (most negative) linear acceleration.
        :param maxLinearAccel:  The maximum (most positive) linear acceleration.
        :param maxAngularAccel: The maximum angular acceleration.
                                @throws std::invalid_argument if minimum linear acceleration is greater
                                than maximum linear acceleration
        """
    @typing.overload
    def __init__(self, system: wpimath._controls._controls.system.LinearSystem_2_2_2, trackwidth: meters, minLinearAccel: meters_per_second_squared, maxLinearAccel: meters_per_second_squared, maxAngularAccel: radians_per_second_squared) -> None: ...
    def calculate(self, leftVelocity: meters_per_second, rightVelocity: meters_per_second, leftVoltage: volts, rightVoltage: volts) -> DifferentialDriveWheelVoltages: 
        """
        Returns the next voltage pair subject to acceleraiton constraints.

        :param leftVelocity:  The left wheel velocity.
        :param rightVelocity: The right wheel velocity.
        :param leftVoltage:   The unconstrained left motor voltage.
        :param rightVoltage:  The unconstrained right motor voltage.

        :returns: The constrained wheel voltages.
        """
    pass
class DifferentialDriveWheelVoltages():
    """
    Motor voltages for a differential drive.
    """
    def __init__(self, left: volts = 0, right: volts = 0) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def left(self) -> volts:
        """
        :type: volts
        """
    @left.setter
    def left(self, arg0: volts) -> None:
        pass
    @property
    def right(self) -> volts:
        """
        :type: volts
        """
    @right.setter
    def right(self, arg0: volts) -> None:
        pass
    pass
class ElevatorFeedforward():
    """
    A helper class that computes feedforward outputs for a simple elevator
    (modeled as a motor acting against the force of gravity).
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new ElevatorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kG: The gravity gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds² per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kG: volts, kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter = 0.0) -> None: ...
    def calculate(self, velocity: meters_per_second, acceleration: meters_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second².

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the elevator.
        :param velocity:   The velocity of the elevator.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the elevator.
        :param acceleration: The acceleration of the elevator.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the elevator.
        :param velocity:   The velocity of the elevator.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the elevator.
        :param acceleration: The acceleration of the elevator.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_meter:
        """
        :type: volt_seconds_squared_per_meter
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_meter) -> None:
        pass
    @property
    def kG(self) -> volts:
        """
        :type: volts
        """
    @kG.setter
    def kG(self, arg0: volts) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_meter:
        """
        :type: volt_seconds_per_meter
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_meter) -> None:
        pass
    pass
class HolonomicDriveController():
    """
    This holonomic drive controller can be used to follow trajectories using a
    holonomic drivetrain (i.e. swerve or mecanum). Holonomic trajectory following
    is a much simpler problem to solve compared to skid-steer style drivetrains
    because it is possible to individually control forward, sideways, and angular
    velocity.

    The holonomic drive controller takes in one PID controller for each
    direction, forward and sideways, and one profiled PID controller for the
    angular direction. Because the heading dynamics are decoupled from
    translations, users can specify a custom heading that the drivetrain should
    point toward. This heading reference is profiled for smoothness.
    """
    def __init__(self, xController: PIDController, yController: PIDController, thetaController: ProfiledPIDControllerRadians) -> None: 
        """
        Constructs a holonomic drive controller.

        :param xController:     A PID Controller to respond to error in the
                                field-relative x direction.
        :param yController:     A PID Controller to respond to error in the
                                field-relative y direction.
        :param thetaController: A profiled PID controller to respond to error in
                                angle.
        """
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath._controls._controls.trajectory.Trajectory.State, desiredHeading: wpimath.geometry._geometry.Rotation2d) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the next output of the holonomic drive controller.

        :param currentPose:           The current pose, as measured by odometry or pose
                                      estimator.
        :param trajectoryPose:        The desired trajectory pose, as sampled for the
                                      current timestep.
        :param desiredLinearVelocity: The desired linear velocity.
        :param desiredHeading:        The desired heading.

        :returns: The next output of the holonomic drive controller.

        Returns the next output of the holonomic drive controller.

        :param currentPose:    The current pose, as measured by odometry or pose
                               estimator.
        :param desiredState:   The desired trajectory pose, as sampled for the current
                               timestep.
        :param desiredHeading: The desired heading.

        :returns: The next output of the holonomic drive controller.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, trajectoryPose: wpimath.geometry._geometry.Pose2d, desiredLinearVelocity: meters_per_second, desiredHeading: wpimath.geometry._geometry.Rotation2d) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes. When
        Calculate() is called on a disabled controller, only feedforward values
        are returned.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, tolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param tolerance: Pose error which is tolerable.
        """
    pass
class ImplicitModelFollower_1_1():
    """
    Contains the controller coefficients and logic for an implicit model
    follower.

    Implicit model following lets us design a feedback controller that erases the
    dynamics of our system and makes it behave like some other system. This can
    be used to make a drivetrain more controllable during teleop driving by
    making it behave like a slower or more benign drivetrain.

    For more on the underlying math, read appendix B.3 in
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def U(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the control input vector u.

        :returns: The control input.

        Returns an element of the control input vector u.

        :param i: Row of u.

        :returns: The row of the control input vector.
        """
    @typing.overload
    def U(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Aref: numpy.ndarray[numpy.float64, _Shape[1, 1]], Bref: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:    Continuous system matrix of the plant being controlled.
        :param B:    Continuous input matrix of the plant being controlled.
        :param Aref: Continuous system matrix whose dynamics should be followed.
        :param Bref: Continuous input matrix whose dynamics should be followed.
        """
    @typing.overload
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_1_1_1, plantRef: wpimath._controls._controls.system.LinearSystem_1_1_1) -> None: ...
    @typing.overload
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_1_1_2, plantRef: wpimath._controls._controls.system.LinearSystem_1_1_2) -> None: ...
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[1, 1]], u: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the next output of the controller.

        :param x: The current state x.
        :param u: The current input for the original model.
        """
    def reset(self) -> None: 
        """
        Resets the controller.
        """
    pass
class ImplicitModelFollower_2_1():
    """
    Contains the controller coefficients and logic for an implicit model
    follower.

    Implicit model following lets us design a feedback controller that erases the
    dynamics of our system and makes it behave like some other system. This can
    be used to make a drivetrain more controllable during teleop driving by
    making it behave like a slower or more benign drivetrain.

    For more on the underlying math, read appendix B.3 in
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def U(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the control input vector u.

        :returns: The control input.

        Returns an element of the control input vector u.

        :param i: Row of u.

        :returns: The row of the control input vector.
        """
    @typing.overload
    def U(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Aref: numpy.ndarray[numpy.float64, _Shape[2, 2]], Bref: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:    Continuous system matrix of the plant being controlled.
        :param B:    Continuous input matrix of the plant being controlled.
        :param Aref: Continuous system matrix whose dynamics should be followed.
        :param Bref: Continuous input matrix whose dynamics should be followed.
        """
    @typing.overload
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_1_1, plantRef: wpimath._controls._controls.system.LinearSystem_2_1_1) -> None: ...
    @typing.overload
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_1_2, plantRef: wpimath._controls._controls.system.LinearSystem_2_1_2) -> None: ...
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[2, 1]], u: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the next output of the controller.

        :param x: The current state x.
        :param u: The current input for the original model.
        """
    def reset(self) -> None: 
        """
        Resets the controller.
        """
    pass
class ImplicitModelFollower_2_2():
    """
    Contains the controller coefficients and logic for an implicit model
    follower.

    Implicit model following lets us design a feedback controller that erases the
    dynamics of our system and makes it behave like some other system. This can
    be used to make a drivetrain more controllable during teleop driving by
    making it behave like a slower or more benign drivetrain.

    For more on the underlying math, read appendix B.3 in
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def U(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the control input vector u.

        :returns: The control input.

        Returns an element of the control input vector u.

        :param i: Row of u.

        :returns: The row of the control input vector.
        """
    @typing.overload
    def U(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Aref: numpy.ndarray[numpy.float64, _Shape[2, 2]], Bref: numpy.ndarray[numpy.float64, _Shape[2, 2]]) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:    Continuous system matrix of the plant being controlled.
        :param B:    Continuous input matrix of the plant being controlled.
        :param Aref: Continuous system matrix whose dynamics should be followed.
        :param Bref: Continuous input matrix whose dynamics should be followed.
        """
    @typing.overload
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_2_1, plantRef: wpimath._controls._controls.system.LinearSystem_2_2_1) -> None: ...
    @typing.overload
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_2_2, plantRef: wpimath._controls._controls.system.LinearSystem_2_2_2) -> None: ...
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[2, 1]], u: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the next output of the controller.

        :param x: The current state x.
        :param u: The current input for the original model.
        """
    def reset(self) -> None: 
        """
        Resets the controller.
        """
    pass
class LTVDifferentialDriveController():
    """
    The linear time-varying differential drive controller has a similar form to
    the LQR, but the model used to compute the controller gain is the nonlinear
    model linearized around the drivetrain's current state. We precomputed gains
    for important places in our state-space, then interpolated between them with
    a LUT to save computational resources.

    See section 8.7 in Controls Engineering in FRC for a derivation of the
    control law we used shown in theorem 8.7.4.
    """
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_2_2, trackwidth: meters, Qelems: typing.Tuple[float, float, float, float, float], Relems: typing.Tuple[float, float], dt: seconds) -> None: 
        """
        Constructs a linear time-varying differential drive controller.

        :param plant:      The differential drive velocity plant.
        :param trackwidth: The distance between the differential drive's left and
                           right wheels.
        :param Qelems:     The maximum desired error tolerance for each state.
        :param Relems:     The maximum desired control effort for each input.
        :param dt:         Discretization timestep.
        """
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, leftVelocity: meters_per_second, rightVelocity: meters_per_second, desiredState: wpimath._controls._controls.trajectory.Trajectory.State) -> DifferentialDriveWheelVoltages: 
        """
        Returns the left and right output voltages of the LTV controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:      The current pose.
        :param leftVelocity:     The current left velocity.
        :param rightVelocity:    The current right velocity.
        :param poseRef:          The desired pose.
        :param leftVelocityRef:  The desired left velocity.
        :param rightVelocityRef: The desired right velocity.

        Returns the left and right output voltages of the LTV controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:   The current pose.
        :param leftVelocity:  The left velocity.
        :param rightVelocity: The right velocity.
        :param desiredState:  The desired pose, linear velocity, and angular velocity
                              from a trajectory.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, leftVelocity: meters_per_second, rightVelocity: meters_per_second, poseRef: wpimath.geometry._geometry.Pose2d, leftVelocityRef: meters_per_second, rightVelocityRef: meters_per_second) -> DifferentialDriveWheelVoltages: ...
    def setTolerance(self, poseTolerance: wpimath.geometry._geometry.Pose2d, leftVelocityTolerance: meters_per_second, rightVelocityTolerance: meters_per_second) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param poseTolerance:          Pose error which is tolerable.
        :param leftVelocityTolerance:  Left velocity error which is tolerable.
        :param rightVelocityTolerance: Right velocity error which is tolerable.
        """
    pass
class LTVUnicycleController():
    """
    The linear time-varying unicycle controller has a similar form to the LQR,
    but the model used to compute the controller gain is the nonlinear model
    linearized around the drivetrain's current state.

    See section 8.9 in Controls Engineering in FRC for a derivation of the
    control law we used shown in theorem 8.9.1.
    """
    @typing.overload
    def __init__(self, Qelems: typing.Tuple[float, float, float], Relems: typing.Tuple[float, float], dt: seconds, maxVelocity: meters_per_second = 9.0) -> None: 
        """
        Constructs a linear time-varying unicycle controller with default maximum
        desired error tolerances of (0.0625 m, 0.125 m, 2 rad) and default maximum
        desired control effort of (1 m/s, 2 rad/s).

        :param dt:          Discretization timestep.
        :param maxVelocity: The maximum velocity for the controller gain lookup
                            table.

        Constructs a linear time-varying unicycle controller.

        :param Qelems:      The maximum desired error tolerance for each state.
        :param Relems:      The maximum desired control effort for each input.
        :param dt:          Discretization timestep.
        :param maxVelocity: The maximum velocity for the controller gain lookup
                            table.
        """
    @typing.overload
    def __init__(self, dt: seconds, maxVelocity: meters_per_second = 9.0) -> None: ...
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath._controls._controls.trajectory.Trajectory.State) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the linear and angular velocity outputs of the LTV controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:        The current pose.
        :param poseRef:            The desired pose.
        :param linearVelocityRef:  The desired linear velocity.
        :param angularVelocityRef: The desired angular velocity.

        Returns the linear and angular velocity outputs of the LTV controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:  The current pose.
        :param desiredState: The desired pose, linear velocity, and angular velocity
                             from a trajectory.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, poseRef: wpimath.geometry._geometry.Pose2d, linearVelocityRef: meters_per_second, angularVelocityRef: radians_per_second) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, poseTolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param poseTolerance: Pose error which is tolerable.
        """
    pass
class LinearPlantInversionFeedforward_1_1():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const StateVector&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearPlantInversionFeedforward_2_1():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const StateVector&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearPlantInversionFeedforward_2_2():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const StateVector&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearQuadraticRegulator_1_1():
    """
    Contains the controller coefficients and logic for a linear-quadratic
    regulator (LQR).
    LQRs use the control law u = K(r - x).

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States Number of states.
    @tparam Inputs Number of inputs.
    """
    @typing.overload
    def K(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the controller matrix K.

        Returns an element of the controller matrix K.

        :param i: Row of K.
        :param j: Column of K.
        """
    @typing.overload
    def K(self, i: int, j: int) -> float: ...
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the reference vector r.

        :returns: The reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def U(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the control input vector u.

        :returns: The control input.

        Returns an element of the control input vector u.

        :param i: Row of u.

        :returns: The row of the control input vector.
        """
    @typing.overload
    def U(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Q: numpy.ndarray[numpy.float64, _Shape[1, 1]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], N: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.
                       @throws std::invalid_argument If the system is uncontrollable.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.
                   @throws std::invalid_argument If the system is uncontrollable.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param N:  The state-input cross-term cost matrix.
        :param dt: Discretization timestep.
                   @throws std::invalid_argument If the system is uncontrollable.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Q: numpy.ndarray[numpy.float64, _Shape[1, 1]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Qelems: typing.Tuple[float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_1, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_2, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the next output of the controller.

        :param x: The current state x.

        Returns the next output of the controller.

        :param x:     The current state x.
        :param nextR: The next reference vector r.
        """
    @typing.overload
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def latencyCompensate(self, plant: wpimath._controls._controls.system.LinearSystem_1_1_1, dt: seconds, inputDelay: seconds) -> None: 
        """
        Adjusts LQR controller gain to compensate for a pure time delay in the
        input.

        Linear-Quadratic regulator controller gains tend to be aggressive. If
        sensor measurements are time-delayed too long, the LQR may be unstable.
        However, if we know the amount of delay, we can compute the control based
        on where the system will be after the time delay.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf
        appendix C.4 for a derivation.

        :param plant:      The plant being controlled.
        :param dt:         Discretization timestep.
        :param inputDelay: Input time delay.

        Adjusts LQR controller gain to compensate for a pure time delay in the
        input.

        Linear-Quadratic regulator controller gains tend to be aggressive. If
        sensor measurements are time-delayed too long, the LQR may be unstable.
        However, if we know the amount of delay, we can compute the control based
        on where the system will be after the time delay.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf
        appendix C.4 for a derivation.

        :param plant:      The plant being controlled.
        :param dt:         Discretization timestep.
        :param inputDelay: Input time delay.
        """
    @typing.overload
    def latencyCompensate(self, plant: wpimath._controls._controls.system.LinearSystem_1_1_2, dt: seconds, inputDelay: seconds) -> None: ...
    def reset(self) -> None: 
        """
        Resets the controller.
        """
    pass
class LinearQuadraticRegulator_2_1():
    """
    Contains the controller coefficients and logic for a linear-quadratic
    regulator (LQR).
    LQRs use the control law u = K(r - x).

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States Number of states.
    @tparam Inputs Number of inputs.
    """
    @typing.overload
    def K(self) -> numpy.ndarray[numpy.float64, _Shape[1, 2]]: 
        """
        Returns the controller matrix K.

        Returns an element of the controller matrix K.

        :param i: Row of K.
        :param j: Column of K.
        """
    @typing.overload
    def K(self, i: int, j: int) -> float: ...
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the reference vector r.

        :returns: The reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def U(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the control input vector u.

        :returns: The control input.

        Returns an element of the control input vector u.

        :param i: Row of u.

        :returns: The row of the control input vector.
        """
    @typing.overload
    def U(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], N: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.
                       @throws std::invalid_argument If the system is uncontrollable.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.
                   @throws std::invalid_argument If the system is uncontrollable.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param N:  The state-input cross-term cost matrix.
        :param dt: Discretization timestep.
                   @throws std::invalid_argument If the system is uncontrollable.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Qelems: typing.Tuple[float, float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_1, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_2, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the next output of the controller.

        :param x: The current state x.

        Returns the next output of the controller.

        :param x:     The current state x.
        :param nextR: The next reference vector r.
        """
    @typing.overload
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def latencyCompensate(self, plant: wpimath._controls._controls.system.LinearSystem_2_1_1, dt: seconds, inputDelay: seconds) -> None: 
        """
        Adjusts LQR controller gain to compensate for a pure time delay in the
        input.

        Linear-Quadratic regulator controller gains tend to be aggressive. If
        sensor measurements are time-delayed too long, the LQR may be unstable.
        However, if we know the amount of delay, we can compute the control based
        on where the system will be after the time delay.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf
        appendix C.4 for a derivation.

        :param plant:      The plant being controlled.
        :param dt:         Discretization timestep.
        :param inputDelay: Input time delay.

        Adjusts LQR controller gain to compensate for a pure time delay in the
        input.

        Linear-Quadratic regulator controller gains tend to be aggressive. If
        sensor measurements are time-delayed too long, the LQR may be unstable.
        However, if we know the amount of delay, we can compute the control based
        on where the system will be after the time delay.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf
        appendix C.4 for a derivation.

        :param plant:      The plant being controlled.
        :param dt:         Discretization timestep.
        :param inputDelay: Input time delay.
        """
    @typing.overload
    def latencyCompensate(self, plant: wpimath._controls._controls.system.LinearSystem_2_1_2, dt: seconds, inputDelay: seconds) -> None: ...
    def reset(self) -> None: 
        """
        Resets the controller.
        """
    pass
class LinearQuadraticRegulator_2_2():
    """
    Contains the controller coefficients and logic for a linear-quadratic
    regulator (LQR).
    LQRs use the control law u = K(r - x).

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States Number of states.
    @tparam Inputs Number of inputs.
    """
    @typing.overload
    def K(self) -> numpy.ndarray[numpy.float64, _Shape[2, 2]]: 
        """
        Returns the controller matrix K.

        Returns an element of the controller matrix K.

        :param i: Row of K.
        :param j: Column of K.
        """
    @typing.overload
    def K(self, i: int, j: int) -> float: ...
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the reference vector r.

        :returns: The reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def U(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the control input vector u.

        :returns: The control input.

        Returns an element of the control input vector u.

        :param i: Row of u.

        :returns: The row of the control input vector.
        """
    @typing.overload
    def U(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[2, 2]], N: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.
                       @throws std::invalid_argument If the system is uncontrollable.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.
                   @throws std::invalid_argument If the system is uncontrollable.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param N:  The state-input cross-term cost matrix.
        :param dt: Discretization timestep.
                   @throws std::invalid_argument If the system is uncontrollable.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Qelems: typing.Tuple[float, float], Relems: typing.Tuple[float, float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_1, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float, float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_2, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float, float], arg3: seconds) -> None: ...
    @typing.overload
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the next output of the controller.

        :param x: The current state x.

        Returns the next output of the controller.

        :param x:     The current state x.
        :param nextR: The next reference vector r.
        """
    @typing.overload
    def calculate(self, x: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def latencyCompensate(self, plant: wpimath._controls._controls.system.LinearSystem_2_2_1, dt: seconds, inputDelay: seconds) -> None: 
        """
        Adjusts LQR controller gain to compensate for a pure time delay in the
        input.

        Linear-Quadratic regulator controller gains tend to be aggressive. If
        sensor measurements are time-delayed too long, the LQR may be unstable.
        However, if we know the amount of delay, we can compute the control based
        on where the system will be after the time delay.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf
        appendix C.4 for a derivation.

        :param plant:      The plant being controlled.
        :param dt:         Discretization timestep.
        :param inputDelay: Input time delay.

        Adjusts LQR controller gain to compensate for a pure time delay in the
        input.

        Linear-Quadratic regulator controller gains tend to be aggressive. If
        sensor measurements are time-delayed too long, the LQR may be unstable.
        However, if we know the amount of delay, we can compute the control based
        on where the system will be after the time delay.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf
        appendix C.4 for a derivation.

        :param plant:      The plant being controlled.
        :param dt:         Discretization timestep.
        :param inputDelay: Input time delay.
        """
    @typing.overload
    def latencyCompensate(self, plant: wpimath._controls._controls.system.LinearSystem_2_2_2, dt: seconds, inputDelay: seconds) -> None: ...
    def reset(self) -> None: 
        """
        Resets the controller.
        """
    pass
class PIDController(wpiutil._wpiutil.Sendable):
    """
    Implements a PID control loop.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, period: seconds = 0.02) -> None: 
        """
        Allocates a PIDController with the given constants for Kp, Ki, and Kd.

        :param Kp:     The proportional coefficient.
        :param Ki:     The integral coefficient.
        :param Kd:     The derivative coefficient.
        :param period: The period between controller updates in seconds. The
                       default is 20 milliseconds. Must be non-zero and positive.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the setpoint.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param setpoint:    The new setpoint of the controller.
        """
    @typing.overload
    def calculate(self, measurement: float, setpoint: float) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: float, maximumInput: float) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> float: 
        """
        Returns the difference between the setpoint and the measurement.
        """
    def getPositionTolerance(self) -> float: 
        """
        Gets the position tolerance of this controller.

        :returns: The position tolerance of the controller.
        """
    def getSetpoint(self) -> float: 
        """
        Returns the current setpoint of the PIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> float: 
        """
        Returns the velocity error.
        """
    def getVelocityTolerance(self) -> float: 
        """
        Gets the velocity tolerance of this controller.

        :returns: The velocity tolerance of the controller.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def isContinuousInputEnabled(self) -> bool: 
        """
        Returns true if continuous input is enabled.
        """
    def reset(self) -> None: 
        """
        Reset the previous error, the integral term, and disable the controller.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setSetpoint(self, setpoint: float) -> None: 
        """
        Sets the setpoint for the PIDController.

        :param setpoint: The desired setpoint.
        """
    def setTolerance(self, positionTolerance: float, velocityTolerance: float = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class ProfiledPIDController(wpiutil._wpiutil.Sendable):
    """
    Implements a PID control loop whose setpoint is constrained by a trapezoid
    profile.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, constraints: wpimath._controls._controls.trajectory.TrapezoidProfile.Constraints, period: seconds = 0.02) -> None: 
        """
        Allocates a ProfiledPIDController with the given constants for Kp, Ki, and
        Kd. Users should call reset() when they first start running the controller
        to avoid unwanted behavior.

        :param Kp:          The proportional coefficient.
        :param Ki:          The integral coefficient.
        :param Kd:          The derivative coefficient.
        :param constraints: Velocity and acceleration constraints for goal.
        :param period:      The period between controller updates in seconds. The
                            default is 20 milliseconds.
        """
    def atGoal(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        Currently this just reports on target as the actual value passes through
        the setpoint. Ideally it should be based on being within the tolerance for
        some period of time.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.
        :param constraints: Velocity and acceleration constraints for goal.
        """
    @typing.overload
    def calculate(self, measurement: float, goal: float) -> float: ...
    @typing.overload
    def calculate(self, measurement: float, goal: float, constraints: wpimath._controls._controls.trajectory.TrapezoidProfile.Constraints) -> float: ...
    @typing.overload
    def calculate(self, measurement: float, goal: wpimath._controls._controls.trajectory.TrapezoidProfile.State) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: float, maximumInput: float) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getGoal(self) -> wpimath._controls._controls.trajectory.TrapezoidProfile.State: 
        """
        Gets the goal for the ProfiledPIDController.
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> float: 
        """
        Returns the difference between the setpoint and the measurement.

        :returns: The error.
        """
    def getPositionTolerance(self) -> float: 
        """
        Gets the position tolerance of this controller.

        :returns: The position tolerance of the controller.
        """
    def getSetpoint(self) -> wpimath._controls._controls.trajectory.TrapezoidProfile.State: 
        """
        Returns the current setpoint of the ProfiledPIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> units_per_second: 
        """
        Returns the change in error per second.
        """
    def getVelocityTolerance(self) -> float: 
        """
        Gets the velocity tolerance of this controller.

        :returns: The velocity tolerance of the controller.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    @typing.overload
    def reset(self, measuredPosition: float) -> None: 
        """
        Reset the previous error and the integral term.

        :param measurement: The current measured State of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system.
        :param measuredVelocity: The current measured velocity of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system. The
                                 velocity is assumed to be zero.
        """
    @typing.overload
    def reset(self, measuredPosition: float, measuredVelocity: units_per_second) -> None: ...
    @typing.overload
    def reset(self, measurement: wpimath._controls._controls.trajectory.TrapezoidProfile.State) -> None: ...
    def setConstraints(self, constraints: wpimath._controls._controls.trajectory.TrapezoidProfile.Constraints) -> None: 
        """
        Set velocity and acceleration constraints for goal.

        :param constraints: Velocity and acceleration constraints for goal.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    @typing.overload
    def setGoal(self, goal: float) -> None: 
        """
        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.

        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.
        """
    @typing.overload
    def setGoal(self, goal: wpimath._controls._controls.trajectory.TrapezoidProfile.State) -> None: ...
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setTolerance(self, positionTolerance: float, velocityTolerance: units_per_second = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with
        AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class ProfiledPIDControllerRadians(wpiutil._wpiutil.Sendable):
    """
    Implements a PID control loop whose setpoint is constrained by a trapezoid
    profile.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, constraints: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.Constraints, period: seconds = 0.02) -> None: 
        """
        Allocates a ProfiledPIDController with the given constants for Kp, Ki, and
        Kd. Users should call reset() when they first start running the controller
        to avoid unwanted behavior.

        :param Kp:          The proportional coefficient.
        :param Ki:          The integral coefficient.
        :param Kd:          The derivative coefficient.
        :param constraints: Velocity and acceleration constraints for goal.
        :param period:      The period between controller updates in seconds. The
                            default is 20 milliseconds.
        """
    def atGoal(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        Currently this just reports on target as the actual value passes through
        the setpoint. Ideally it should be based on being within the tolerance for
        some period of time.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: radians) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.
        :param constraints: Velocity and acceleration constraints for goal.
        """
    @typing.overload
    def calculate(self, measurement: radians, goal: radians) -> float: ...
    @typing.overload
    def calculate(self, measurement: radians, goal: radians, constraints: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.Constraints) -> float: ...
    @typing.overload
    def calculate(self, measurement: radians, goal: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: radians, maximumInput: radians) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getGoal(self) -> wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State: 
        """
        Gets the goal for the ProfiledPIDController.
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> radians: 
        """
        Returns the difference between the setpoint and the measurement.

        :returns: The error.
        """
    def getPositionTolerance(self) -> float: 
        """
        Gets the position tolerance of this controller.

        :returns: The position tolerance of the controller.
        """
    def getSetpoint(self) -> wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State: 
        """
        Returns the current setpoint of the ProfiledPIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> radians_per_second: 
        """
        Returns the change in error per second.
        """
    def getVelocityTolerance(self) -> float: 
        """
        Gets the velocity tolerance of this controller.

        :returns: The velocity tolerance of the controller.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    @typing.overload
    def reset(self, measuredPosition: radians) -> None: 
        """
        Reset the previous error and the integral term.

        :param measurement: The current measured State of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system.
        :param measuredVelocity: The current measured velocity of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system. The
                                 velocity is assumed to be zero.
        """
    @typing.overload
    def reset(self, measuredPosition: radians, measuredVelocity: radians_per_second) -> None: ...
    @typing.overload
    def reset(self, measurement: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State) -> None: ...
    def setConstraints(self, constraints: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.Constraints) -> None: 
        """
        Set velocity and acceleration constraints for goal.

        :param constraints: Velocity and acceleration constraints for goal.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    @typing.overload
    def setGoal(self, goal: radians) -> None: 
        """
        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.

        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.
        """
    @typing.overload
    def setGoal(self, goal: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State) -> None: ...
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setTolerance(self, positionTolerance: radians, velocityTolerance: radians_per_second = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with
        AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class RamseteController():
    """
    Ramsete is a nonlinear time-varying feedback controller for unicycle models
    that drives the model to a desired pose along a two-dimensional trajectory.
    Why would we need a nonlinear control law in addition to the linear ones we
    have used so far like PID? If we use the original approach with PID
    controllers for left and right position and velocity states, the controllers
    only deal with the local pose. If the robot deviates from the path, there is
    no way for the controllers to correct and the robot may not reach the desired
    global pose. This is due to multiple endpoints existing for the robot which
    have the same encoder path arc lengths.

    Instead of using wheel path arc lengths (which are in the robot's local
    coordinate frame), nonlinear controllers like pure pursuit and Ramsete use
    global pose. The controller uses this extra information to guide a linear
    reference tracker like the PID controllers back in by adjusting the
    references of the PID controllers.

    The paper "Control of Wheeled Mobile Robots: An Experimental Overview"
    describes a nonlinear controller for a wheeled vehicle with unicycle-like
    kinematics; a global pose consisting of x, y, and theta; and a desired pose
    consisting of x_d, y_d, and theta_d. We call it Ramsete because that's the
    acronym for the title of the book it came from in Italian ("Robotica
    Articolata e Mobile per i SErvizi e le TEcnologie").

    See <https://file.tavsys.net/control/controls-engineering-in-frc.pdf> section
    on Ramsete unicycle controller for a derivation and analysis.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a Ramsete unicycle controller.

        :param b:    Tuning parameter (b > 0 rad²/m²) for which larger values make
                     convergence more aggressive like a proportional term.
        :param zeta: Tuning parameter (0 rad⁻¹ < zeta < 1 rad⁻¹) for which larger
                     values provide more damping in response.

        Construct a Ramsete unicycle controller. The default arguments for
        b and zeta of 2.0 rad²/m² and 0.7 rad⁻¹ have been well-tested to produce
        desirable results.
        """
    @typing.overload
    def __init__(self, b: float, zeta: float) -> None: ...
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath._controls._controls.trajectory.Trajectory.State) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the next output of the Ramsete controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:        The current pose.
        :param poseRef:            The desired pose.
        :param linearVelocityRef:  The desired linear velocity.
        :param angularVelocityRef: The desired angular velocity.

        Returns the next output of the Ramsete controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:  The current pose.
        :param desiredState: The desired pose, linear velocity, and angular velocity
                             from a trajectory.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, poseRef: wpimath.geometry._geometry.Pose2d, linearVelocityRef: meters_per_second, angularVelocityRef: radians_per_second) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, poseTolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param poseTolerance: Pose error which is tolerable.
        """
    pass
class SimpleMotorFeedforwardMeters():
    """
    A helper class that computes feedforward voltages for a simple
    permanent-magnet DC motor.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new SimpleMotorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds² per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter = 0.0) -> None: ...
    @typing.overload
    def calculate(self, currentVelocity: meters_per_second, nextVelocity: meters_per_second, dt: seconds) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second².

        :returns: The computed feedforward, in volts.

        Calculates the feedforward from the gains and setpoints.

        :param currentVelocity: The current velocity setpoint, in distance per
                                second.
        :param nextVelocity:    The next velocity setpoint, in distance per second.
        :param dt:              Time between velocity setpoints in seconds.

        :returns: The computed feedforward, in volts.
        """
    @typing.overload
    def calculate(self, velocity: meters_per_second, acceleration: meters_per_second_squared = 0.0) -> volts: ...
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_meter:
        """
        :type: volt_seconds_squared_per_meter
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_meter) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_meter:
        """
        :type: volt_seconds_per_meter
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_meter) -> None:
        pass
    pass
