from __future__ import annotations
import wpilib.event._event
import typing
import ntcore._ntcore

__all__ = [
    "BooleanEvent",
    "EventLoop",
    "NetworkBooleanEvent"
]


class BooleanEvent():
    """
    This class provides an easy way to link actions to inputs. Each object
    represents a boolean condition to which callback actions can be bound using
    :meth:`.IfHigh`.

    These events can easily be composed using factories such as {@link
    #operator!},
    :class:`.operator`, :class:`.operator` etc.

    To get an event that activates only when this one changes, see {@link
    #Falling()} and :meth:`.Rising`.
    """
    def __init__(self, loop: EventLoop, condition: typing.Callable[[], bool]) -> None: 
        """
        Creates a new event with the given condition determining whether it is
        active.

        :param loop:      the loop that polls this event
        :param condition: returns whether or not the event should be active
        """
    def castTo(self, arg0: function) -> object: 
        """
        A method to "downcast" a BooleanEvent instance to a subclass (for example,
        to a command-based version of this class).

        :param ctor: a method reference to the constructor of the subclass that
                     accepts the loop as the first parameter and the condition/signal as the
                     second.

        :returns: an instance of the subclass.
        """
    def debounce(self, debounceTime: seconds, type: wpimath.filter._filter.Debouncer.DebounceType = DebounceType.kRising) -> BooleanEvent: 
        """
        Creates a new debounced event from this event - it will become active when
        this event has been active for longer than the specified period.

        :param debounceTime: The debounce period.
        :param type:         The debounce type.

        :returns: The debounced event.
        """
    def falling(self) -> BooleanEvent: 
        """
        Get a new event that triggers only when this one newly changes to false.

        :returns: a new event representing when this one newly changes to false.
        """
    def getAsBoolean(self) -> bool: 
        """
        Check whether this event is active or not.

        :returns: true if active.
        """
    def ifHigh(self, action: typing.Callable[[], None]) -> None: 
        """
        Bind an action to this event.

        :param action: the action to run if this event is active.
        """
    def rising(self) -> BooleanEvent: 
        """
        Get a new event that events only when this one newly changes to true.

        :returns: a new event representing when this one newly changes to true.
        """
    pass
class EventLoop():
    """
    The loop polling BooleanEvent objects and executing the actions bound to
    them.
    """
    def __init__(self) -> None: ...
    def bind(self, action: typing.Callable[[], None]) -> None: 
        """
        Bind a new action to run.

        :param action: the action to run.
        """
    def clear(self) -> None: 
        """
        Clear all bindings.
        """
    def poll(self) -> None: 
        """
        Poll all bindings.
        """
    pass
class NetworkBooleanEvent(BooleanEvent):
    """
    A Button that uses a NetworkTable boolean field.

    This class is provided by the NewCommands VendorDep
    """
    @typing.overload
    def __init__(self, loop: EventLoop, inst: ntcore._ntcore.NetworkTableInstance, tableName: str, topicName: str) -> None: 
        """
        Creates a new event with the given boolean topic determining whether it is
        active.

        :param loop:  the loop that polls this event
        :param topic: The boolean topic that contains the value

        Creates a new event with the given boolean subscriber determining whether
        it is active.

        :param loop: the loop that polls this event
        :param sub:  The boolean subscriber that provides the value

        Creates a new event with the given boolean topic determining whether it is
        active.

        :param loop:      the loop that polls this event
        :param table:     The NetworkTable that contains the topic
        :param topicName: The topic name within the table that contains the value

        Creates a new event with the given boolean topic determining whether it is
        active.

        :param loop:      the loop that polls this event
        :param tableName: The NetworkTable name that contains the topic
        :param topicName: The topic name within the table that contains the value

        Creates a new event with the given boolean topic determining whether it is
        active.

        :param loop:      the loop that polls this event
        :param inst:      The NetworkTable instance to use
        :param tableName: The NetworkTable that contains the topic
        :param topicName: The topic name within the table that contains the value
        """
    @typing.overload
    def __init__(self, loop: EventLoop, sub: ntcore._ntcore.BooleanSubscriber) -> None: ...
    @typing.overload
    def __init__(self, loop: EventLoop, table: ntcore._ntcore.NetworkTable, topicName: str) -> None: ...
    @typing.overload
    def __init__(self, loop: EventLoop, tableName: str, topicName: str) -> None: ...
    @typing.overload
    def __init__(self, loop: EventLoop, topic: ntcore._ntcore.BooleanTopic) -> None: ...
    pass
