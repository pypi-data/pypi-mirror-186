from __future__ import annotations
import commands2._impl.cmd
import typing
import commands2._impl

__all__ = [
    "deadline",
    "either",
    "nothing",
    "parallel",
    "print",
    "race",
    "repeatingSequence",
    "run",
    "runEnd",
    "runOnce",
    "select",
    "sequence",
    "startEnd",
    "wait",
    "waitUntil"
]


def deadline(deadline: commands2._impl.Command, others: typing.List[commands2._impl.Command]) -> commands2._impl.Command:
    """
    Runs a group of commands at the same time. Ends once a specific command
    finishes, and cancels the others.
    """
def either(onTrue: commands2._impl.Command, onFalse: commands2._impl.Command, selector: typing.Callable[[], bool]) -> commands2._impl.Command:
    """
    Runs one of two commands, based on the boolean selector function.

    :param onTrue:   the command to run if the selector function returns true
    :param onFalse:  the command to run if the selector function returns false
    :param selector: the selector function
    """
def nothing() -> commands2._impl.Command:
    """
    Constructs a command that does nothing, finishing immediately.
    """
@typing.overload
def parallel(*args) -> commands2._impl.Command:
    """
    Runs a group of commands at the same time. Ends once all commands in the
    group finish.
    """
@typing.overload
def parallel(commands: typing.List[commands2._impl.Command]) -> commands2._impl.Command:
    pass
def print(msg: str) -> commands2._impl.Command:
    """
    Constructs a command that prints a message and finishes.

    :param msg: the message to print
    """
@typing.overload
def race(*args) -> commands2._impl.Command:
    """
    Runs a group of commands at the same time. Ends once any command in the group
    finishes, and cancels the others.
    """
@typing.overload
def race(commands: typing.List[commands2._impl.Command]) -> commands2._impl.Command:
    pass
@typing.overload
def repeatingSequence(*args) -> commands2._impl.Command:
    """
    Runs a group of commands in series, one after the other. Once the last
    command ends, the group is restarted.
    """
@typing.overload
def repeatingSequence(commands: typing.List[commands2._impl.Command]) -> commands2._impl.Command:
    pass
def run(action: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> commands2._impl.Command:
    """
    Constructs a command that runs an action every iteration until interrupted.

    :param action:       the action to run
    :param requirements: subsystems the action requires
    """
def runEnd(run: typing.Callable[[], None], end: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> commands2._impl.Command:
    """
    Constructs a command that runs an action every iteration until interrupted,
    and then runs a second action.

    :param run:          the action to run every iteration
    :param end:          the action to run on interrupt
    :param requirements: subsystems the action requires
    """
def runOnce(action: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> commands2._impl.Command:
    """
    Constructs a command that runs an action once and finishes.

    :param action:       the action to run
    :param requirements: subsystems the action requires
    """
def select(selector: typing.Callable[[], object], commands: typing.List[typing.Tuple[object, commands2._impl.Command]]) -> commands2._impl.Command:
    pass
@typing.overload
def sequence(*args) -> commands2._impl.Command:
    """
    Runs a group of commands in series, one after the other.
    """
@typing.overload
def sequence(commands: typing.List[commands2._impl.Command]) -> commands2._impl.Command:
    pass
def startEnd(start: typing.Callable[[], None], end: typing.Callable[[], None], requirements: typing.List[commands2._impl.Subsystem] = []) -> commands2._impl.Command:
    """
    Constructs a command that runs an action once and another action when the
    command is interrupted.

    :param start:        the action to run on start
    :param end:          the action to run on interrupt
    :param requirements: subsystems the action requires
    """
def wait(duration: seconds) -> commands2._impl.Command:
    """
    Constructs a command that does nothing, finishing after a specified duration.

    :param duration: after how long the command finishes
    """
def waitUntil(condition: typing.Callable[[], bool]) -> commands2._impl.Command:
    """
    Constructs a command that does nothing, finishing once a condition becomes
    true.

    :param condition: the condition
    """
