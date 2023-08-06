"""
_This package can ultimately be extracted from this program to act as an external library._

This package contains an EventDispatcher class within an event_dispatcher module.
EventDispatcher implements a full-featured observer pattern:

- `EventDispatcher` can register multiple `EventSubscriber` implementations.
`EventDispatcher` do not prevent the same `EventSubscriber` object to be registered twice or more.
This allows the same code to be run at different point in time.

- Any `EventSubscriber` implementation must advertise its order (default to `500`).
The `EventDispatcher` will run registered `EventSubscriber` implementations according to this order, lower values first.
When two `EventSubscriber` implementations or more share the same order value,
the order of registration is used to determine which will run first.
Because of the previous behavior, be careful in situation when you ignore the default order value. E.g:
    ```
    [...]
    event_dispatcher.register(subscriber1Order500()) # Run: 1st
    event_dispatcher.register(subscriber2Order500()) # Run: 2nd
    event_dispatcher.register(subscriber3Order500()) # Run: 3rd
    event_dispatcher.register(subscriberOrder501()) # Run: 4th (501 will always run after all 500)

    # Below is a better practice:

    [...]
    event_dispatcher.register(subscriber1Order500()) # Run: 1st
    event_dispatcher.register(subscriber2Order510()) # Run: 3rd
    event_dispatcher.register(subscriber3Order520()) # Run: 4th
    event_dispatcher.register(subscriberOrder501()) # Run: 2nd
    ```

- Any `EventSubscriber` implementation can stop the propagation of events after its run.
If set, this toggle will prevent any subsequent `EventSubscriber` to run, for any events.

- Any `EventSubscriber` implementation must advertise what events it listens to.
  When `EventDispatcher` dispatches a list of events, if any events intersect with an `EventSubscriber` subscribed events,
    it will run.
  The expected data type for events needs some explanations.
  They should be an Enum pointing to a specific value of type `tuple[str, type, Optional[bool]]`:
      1. `str` should ne a humanly readable label for the event.
      2. `type` should be the expected data object type for the specific event.
          Note that no `EventSubscriber` implementation can listen to a list of events requiring *different* data types,
          otherwise the `EventSubscriber` implementation will be permanently ignored and a warning will be raised.
      3. `Optional[bool]`, if set to `True`, will allow the data to be mutated by any `EventSubscriber`.
          Within dispatched events list, if any event is immutable (meaning: if this value is absent or `False`):
          any data mutation by all `EventSubscribers` will be ignored.
          It means you should be extra careful that during a single `dispatch`, *all* events are mutable: `True` for
          the data mutation to work.

- Any `EventSubscriber` implementation can advertise whether it should run.
  All `EventSubscriber` implementations are run by default, if `should_run` is left untouched.

- When `run`, any `EventSubscriber` implementation can raise a special `SubscriberGracefulError`.
  Contrary to any other exception, this error will not abort the entire program.
  Instead, it will be caught by the `EventDispatcher` and a warning will be logged.


Basic Usages:

```
class MyEvents(str, Enum):
    # An event named "test", expecting a mutable MyData type.
    TEST = tuple('test', MyData, True)
    # An event named "test2", expecting a immutable MyOtherData type.
    TEST2 = tuple('test2', MyOtherData)

class MyEventSubscriber(EventSubscriber):
    def get_subscribed_events(self) -> list[Enum]:
        # All the events this subscriber should react to
        return [MyEvent.TEST]

    def run(self, data: MyData) -> MyData:
        # Perform anything you want as a reaction to an event
        if MyData.field == 'wrong value':
            # Avoid this if possible. Prefer to implement `should_run`.
            raise SubscriberGracefulError('This error will be caught and program will continue.')
        if MyData.field == 'fatal':
            raise RuntimeError('This error will end the program immediately.')

        # Because the event "MyEvent.TEST" allows MyData to be mutated, we can change its content.
        MyData.field = 'new value'
        return MyData

    def should_run(self, data: MyData) -> bool:
        # This subscriber will only run if this method returns True.
        return 'specific_value' == data.field
```

Examples:

#### A sandwich EventSubscriber that can run early and late

```
[...]

class Event(Enum):
SANDWICH = tuple('sandwich', BaseModel)

class SandwichEventSubscriber(EventSubscriber):
order: int = 1

def __init__(self, order: int = 1);
    self.order = order

def get_subscribed_events(self) -> list[Enum]:
    return [Event.SANDWICH]

def run(self, data: BaseModel) -> BaseModel:
    print('Running this sandwich event listener')
    return BaseModel

def get_order(self) -> int:
    return self.order

early_subscriber = SandwichEventSubscriber()
late_subscriber = SandwichEventSubscriber(99999)
```
"""
