from __future__ import annotations
import commands2._impl.button
import typing
import commands2._impl
import ntcore._ntcore
import wpilib._wpilib
import wpilib.event._event
import wpilib.interfaces._interfaces

__all__ = [
    "Button",
    "CommandGenericHID",
    "CommandJoystick",
    "CommandPS4Controller",
    "CommandXboxController",
    "JoystickButton",
    "NetworkButton",
    "POVButton"
]


class Button(commands2._impl.Trigger):
    """
    A class used to bind command scheduling to button presses.  Can be composed
    with other buttons with the operators in Trigger.

    @see Trigger
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Create a new button that is pressed when the given condition is true.

        :deprecated: Replace with Trigger

        :param isPressed: Whether the button is pressed.

        Create a new button that is pressed active (default constructor) - activity
        can be further determined by subclass code.

        :deprecated: Replace with Trigger
        """
    @typing.overload
    def __init__(self, isPressed: typing.Callable[[], bool]) -> None: ...
    def cancelWhenPressed(self, command: commands2._impl.Command) -> Button: 
        """
        Binds a command to be canceled when the button is pressed.  Takes a
        raw pointer, and so is non-owning; users are responsible for the lifespan
        and scheduling of the command.

        :deprecated: Pass this as a command end condition with Until() instead.

        :param command: The command to bind.

        :returns: The button, for chained calls.
        """
    def toggleWhenPressed(self, command: commands2._impl.Command) -> Button: 
        """
        Binds a command to start when the button is pressed, and be canceled when
        it is pressed again.  Takes a raw pointer, and so is non-owning; users are
        responsible for the lifespan of the command.

        :deprecated: Replace with Trigger::ToggleOnTrue()

        :param command: The command to bind.

        :returns: The button, for chained calls.
        """
    def whenHeld(self, command: commands2._impl.Command) -> Button: 
        """
        Binds a command to be started when the button is pressed, and canceled
        when it is released.  Takes a raw pointer, and so is non-owning; users are
        responsible for the lifespan of the command.

        :deprecated: Replace with Trigger::WhileTrue()

        :param command: The command to bind.

        :returns: The button, for chained calls.
        """
    @typing.overload
    def whenPressed(self, command: commands2._impl.Command) -> Button: 
        """
        Binds a command to start when the button is pressed.  Takes a
        raw pointer, and so is non-owning; users are responsible for the lifespan
        of the command.

        :deprecated: Replace with Trigger::OnTrue()

        :param command: The command to bind.

        :returns: The trigger, for chained calls.

        Binds a runnable to execute when the button is pressed.

        :deprecated: Replace with Trigger::OnTrue(cmd::RunOnce())

        :param toRun:        the runnable to execute.
        :param requirements: the required subsystems.
        """
    @typing.overload
    def whenPressed(self, toRun: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> Button: ...
    @typing.overload
    def whenReleased(self, command: commands2._impl.Command) -> Button: 
        """
        Binds a command to start when the button is released.  Takes a
        raw pointer, and so is non-owning; users are responsible for the lifespan
        of the command.

        :deprecated: Replace with Trigger::OnFalse()

        :param command: The command to bind.

        :returns: The button, for chained calls.

        Binds a runnable to execute when the button is released.

        :deprecated: Replace with Trigger::OnFalse(cmd::RunOnce())

        :param toRun:        the runnable to execute.
        :param requirements: the required subsystems.
        """
    @typing.overload
    def whenReleased(self, toRun: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> Button: ...
    @typing.overload
    def whileHeld(self, command: commands2._impl.Command) -> Button: 
        """
        Binds a command to be started repeatedly while the button is pressed, and
        canceled when it is released.  Takes a raw pointer, and so is non-owning;
        users are responsible for the lifespan of the command.

        :deprecated: Replace with Trigger::WhileTrue(command.Repeatedly())

        :param command: The command to bind.

        :returns: The button, for chained calls.

        Binds a runnable to execute repeatedly while the button is pressed.

        :deprecated: Replace with Trigger::WhileTrue(cmd::Run())

        :param toRun:        the runnable to execute.
        :param requirements: the required subsystems.
        """
    @typing.overload
    def whileHeld(self, toRun: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> Button: ...
    pass
class CommandGenericHID(wpilib.interfaces._interfaces.GenericHID):
    """
    A subclass of {@link GenericHID} with {@link Trigger} factories for
    command-based.

    @see GenericHID
    """
    @typing.overload
    def POV(self, angle: int, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around this angle of a POV on the HID.

        The POV angles start at 0 in the up direction, and increase clockwise
        (eg right is 90, upper-left is 315).

        :param loop:  the event loop instance to attach the event to. Defaults to
                      {@link CommandScheduler::GetDefaultButtonLoop() the default command
                      scheduler button loop}.
        :param angle: POV angle in degrees, or -1 for the center / not pressed.

        :returns: a Trigger instance based around this angle of a POV on the HID.

        Constructs a Trigger instance based around this angle of a POV on the HID.

        The POV angles start at 0 in the up direction, and increase clockwise
        (eg right is 90, upper-left is 315).

        :param loop:  the event loop instance to attach the event to. Defaults to
                      {@link CommandScheduler::GetDefaultButtonLoop() the default command
                      scheduler button loop}.
        :param pov:   index of the POV to read (starting at 0). Defaults to 0.
        :param angle: POV angle in degrees, or -1 for the center / not pressed.

        :returns: a Trigger instance based around this angle of a POV on the HID.
        """
    @typing.overload
    def POV(self, pov: int, angle: int, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: ...
    def POVCenter(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the center (not pressed)
        position of the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the center position of a POV on the
                  HID.
        """
    def POVDown(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 180 degree angle (down) of
        the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 180 degree angle of a POV on
                  the HID.
        """
    def POVDownLeft(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 225 degree angle (down left)
        of the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 225 degree angle of a POV on
                  the HID.
        """
    def POVDownRight(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 135 degree angle (right
        down) of the default (index 0) POV on the HID.

        :returns: a Trigger instance based around the 135 degree angle of a POV on
                  the HID.
        """
    def POVLeft(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 270 degree angle (left) of
        the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 270 degree angle of a POV on
                  the HID.
        """
    def POVRight(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 90 degree angle (right) of
        the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 90 degree angle of a POV on the
                  HID.
        """
    def POVUp(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 0 degree angle (up) of the
        default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 0 degree angle of a POV on the
                  HID.
        """
    def POVUpLeft(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 315 degree angle (left up)
        of the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 315 degree angle of a POV on
                  the HID.
        """
    def POVUpRight(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance based around the 45 degree angle (right up)
        of the default (index 0) POV on the HID.

        :param loop: the event loop instance to attach the event to. Defaults to
                     {@link CommandScheduler::GetDefaultButtonLoop() the default command
                     scheduler button loop}.

        :returns: a Trigger instance based around the 45 degree angle of a POV on the
                  HID.
        """
    def __init__(self, arg0: int) -> None: ...
    def axisGreaterThan(self, axis: int, threshold: float, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance that is true when the axis value is greater
        than ``threshold``, attached to {@link
        CommandScheduler::GetDefaultButtonLoop() the default command scheduler
        button loop}.

        :param axis:      The axis to read, starting at 0.
        :param threshold: The value below which this trigger should return true.
        :param loop:      the event loop instance to attach the event to. Defaults to
                          {@link CommandScheduler::GetDefaultButtonLoop() the default command
                          scheduler button loop}.

        :returns: a Trigger instance that is true when the axis value is greater than
                  the provided threshold.
        """
    def axisLessThan(self, axis: int, threshold: float, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance that is true when the axis value is less than
        ``threshold``, attached to {@link
        CommandScheduler::GetDefaultButtonLoop() the default command scheduler
        button loop}.

        :param axis:      The axis to read, starting at 0.
        :param threshold: The value below which this trigger should return true.
        :param loop:      the event loop instance to attach the event to. Defaults to
                          {@link CommandScheduler::GetDefaultButtonLoop() the default command
                          scheduler button loop}.

        :returns: a Trigger instance that is true when the axis value is less than
                  the provided threshold.
        """
    def button(self, button: int, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around this button's digital signal.

        :param button: the button index
        :param loop:   the event loop instance to attach the event to. Defaults to the
                       CommandScheduler's default loop.

        :returns: an event instance representing the button's digital signal attached
                  to the given loop.
        """
    pass
class CommandJoystick(wpilib._wpilib.Joystick, wpilib.interfaces._interfaces.GenericHID):
    """
    A subclass of {@link Joystick} with {@link Trigger} factories for
    command-based.

    @see Joystick
    """
    def __init__(self, arg0: int) -> None: ...
    def button(self, button: int, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around this button's digital signal.

        :param button: the button index
        :param loop:   the event loop instance to attach the event to. Defaults to the
                       CommandScheduler's default loop.

        :returns: an event instance representing the button's digital signal attached
                  to the given loop.
        """
    def top(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the top button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the top button's digital signal
                  attached to the given loop.
        """
    def trigger(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the trigger button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the trigger button's digital signal
                  attached to the given loop.
        """
    pass
class CommandPS4Controller(wpilib._wpilib.PS4Controller, wpilib.interfaces._interfaces.GenericHID):
    """
    A subclass of {@link PS4Controller} with {@link Trigger} factories for
    command-based.

    @see PS4Controller
    """
    def L1(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the L1 button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the L1 button's digital signal
                  attached to the given loop.
        """
    def L2(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the L2 button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the L2 button's digital signal
                  attached to the given loop.
        """
    def L3(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the L3 button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the L3 button's digital signal
                  attached to the given loop.
        """
    def PS(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the PS button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the PS button's digital signal
                  attached to the given loop.
        """
    def R1(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the R1 button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the R1 button's digital signal
                  attached to the given loop.
        """
    def R2(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the R2 button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the R2 button's digital signal
                  attached to the given loop.
        """
    def R3(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the R3 button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the R3 button's digital signal
                  attached to the given loop.
        """
    def __init__(self, arg0: int) -> None: ...
    def button(self, button: int, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around this button's digital signal.

        :param button: the button index
        :param loop:   the event loop instance to attach the event to. Defaults to the
                       CommandScheduler's default loop.

        :returns: an event instance representing the button's digital signal attached
                  to the given loop.
        """
    def circle(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the circle button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the circle button's digital signal
                  attached to the given loop.
        """
    def cross(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the cross button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the cross button's digital signal
                  attached to the given loop.
        """
    def options(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the options button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the options button's digital signal
                  attached to the given loop.
        """
    def square(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the square button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the square button's digital signal
                  attached to the given loop.
        """
    def touchpad(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the touchpad's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the touchpad's digital signal
                  attached to the given loop.
        """
    def triangle(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the triangle button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the triangle button's digital signal
                  attached to the given loop.
        """
    pass
class CommandXboxController(wpilib._wpilib.XboxController, wpilib.interfaces._interfaces.GenericHID):
    """
    A subclass of {@link XboxController} with {@link Trigger} factories for
    command-based.

    @see XboxController
    """
    def A(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the A button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the A button's digital signal
                  attached to the given loop.
        """
    def B(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the B button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the B button's digital signal
                  attached to the given loop.
        """
    def X(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the X button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the X button's digital signal
                  attached to the given loop.
        """
    def Y(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the Y button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the Y button's digital signal
                  attached to the given loop.
        """
    def __init__(self, arg0: int) -> None: ...
    def back(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the back button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the back button's digital signal
                  attached to the given loop.
        """
    def button(self, button: int, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around this button's digital signal.

        :param button: the button index
        :param loop:   the event loop instance to attach the event to. Defaults to the
                       CommandScheduler's default loop.

        :returns: an event instance representing the button's digital signal attached
                  to the given loop.
        """
    def leftBumper(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the left bumper's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the left bumper's digital signal
                  attached to the given loop.
        """
    def leftStick(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the left stick's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the left stick's digital signal
                  attached to the given loop.
        """
    def leftTrigger(self, threshold: float = 0.5, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance around the axis value of the left trigger.
        The returned Trigger will be true when the axis value is greater than
        ``threshold``.

        :param threshold: the minimum axis value for the returned Trigger to be
                          true. This value should be in the range [0, 1] where 0 is the unpressed
                          state of the axis. Defaults to 0.5.
        :param loop:      the event loop instance to attach the Trigger to. Defaults to
                          the CommandScheduler's default loop.

        :returns: a Trigger instance that is true when the left trigger's axis
                  exceeds the provided threshold, attached to the given loop
        """
    def rightBumper(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the right bumper's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the right bumper's digital signal
                  attached to the given loop.
        """
    def rightStick(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the right stick's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the right stick's digital signal
                  attached to the given loop.
        """
    def rightTrigger(self, threshold: float = 0.5, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs a Trigger instance around the axis value of the right trigger.
        The returned Trigger will be true when the axis value is greater than
        ``threshold``.

        :param threshold: the minimum axis value for the returned Trigger to be
                          true. This value should be in the range [0, 1] where 0 is the unpressed
                          state of the axis. Defaults to 0.5.
        :param loop:      the event loop instance to attach the Trigger to. Defaults to
                          the CommandScheduler's default loop.

        :returns: a Trigger instance that is true when the right trigger's axis
                  exceeds the provided threshold, attached to the given loop
        """
    def start(self, loop: typing.Optional[wpilib.event._event.EventLoop] = None) -> commands2._impl.Trigger: 
        """
        Constructs an event instance around the start button's digital signal.

        :param loop: the event loop instance to attach the event to. Defaults to the
                     CommandScheduler's default loop.

        :returns: an event instance representing the start button's digital signal
                  attached to the given loop.
        """
    pass
class JoystickButton(Button, commands2._impl.Trigger):
    """
    A class used to bind command scheduling to joystick button presses.  Can be
    composed with other buttons with the operators in Trigger.

    @see Trigger
    """
    def __init__(self, joystick: wpilib.interfaces._interfaces.GenericHID, buttonNumber: int) -> None: 
        """
        Creates a JoystickButton that commands can be bound to.

        :param joystick:     The joystick on which the button is located.
        :param buttonNumber: The number of the button on the joystick.
        """
    pass
class NetworkButton(Button, commands2._impl.Trigger):
    """
    A Button that uses a NetworkTable boolean field.
    """
    @typing.overload
    def __init__(self, inst: ntcore._ntcore.NetworkTableInstance, table: str, field: str) -> None: 
        """
        Creates a NetworkButton that commands can be bound to.

        :param table: The table where the networktable value is located.
        :param field: The field that is the value.

        Creates a NetworkButton that commands can be bound to.

        :param table: The table where the networktable value is located.
        :param field: The field that is the value.

        Creates a NetworkButton that commands can be bound to.

        :param inst:  The NetworkTable instance to use
        :param table: The table where the networktable value is located.
        :param field: The field that is the value.
        """
    @typing.overload
    def __init__(self, table: ntcore._ntcore.NetworkTable, field: str) -> None: ...
    @typing.overload
    def __init__(self, table: str, field: str) -> None: ...
    pass
class POVButton(Button, commands2._impl.Trigger):
    """
    A class used to bind command scheduling to joystick POV presses.  Can be
    composed with other buttons with the operators in Trigger.

    @see Trigger
    """
    def __init__(self, joystick: wpilib.interfaces._interfaces.GenericHID, angle: int, povNumber: int = 0) -> None: 
        """
        Creates a POVButton that commands can be bound to.

        :param joystick:  The joystick on which the button is located.
        :param angle:     The angle of the POV corresponding to a button press.
        :param povNumber: The number of the POV on the joystick.
        """
    pass
