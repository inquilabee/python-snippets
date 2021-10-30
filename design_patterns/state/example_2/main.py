"""
Adapted from book: Mastering Python Design Patterns

Use pip to install `state_machine` package before running the program.
"""

from enum import Enum
from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


class StateName(Enum):
    """Map of verb to state names"""
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'


class StateFunction:
    """Map of verb to state transition functions"""
    RUNNING = 'run'
    WAITING = 'wait'
    BLOCKED = 'block'
    TERMINATED = 'terminate'


@acts_as_state_machine
class Process:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}(state: {self.current_state})"

    # States
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    # transition rules
    wait = Event(
        from_states=(created, running, blocked, swapped_out_waiting),
        to_state=waiting
    )

    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked), to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    @after('wait')
    def wait_info(self):
        print(f'{self.name} entered waiting mode')

    @after('run')
    def run_info(self):
        print(f'{self.name} is running')

    @before('terminate')
    def terminate_info(self):
        print(f'{self.name} terminated')

    @after('block')
    def block_info(self):
        print(f'{self.name} is blocked')

    @after('swap_wait')
    def swap_wait_info(self):
        print(f'{self.name} is swapped out and waiting')

    @after('swap_block')
    def swap_block_info(self):
        print(f'{self.name} is swapped out and blocked')

    def transition(self, state: StateName):
        try:
            state_name = state.name
            event = getattr(StateFunction, state_name)
            event_function = getattr(self, event)
            event_function()
        except InvalidStateTransition as err:
            print(f'Error: transition of {self.name} from {self.current_state} to {state.value} failed')


def main():
    p1, p2 = Process('process_1'), Process('process_2')

    print(p1)
    print(p2)

    print("=" * 20, "\n")

    p1.transition(StateName.WAITING)
    p2.transition(StateName.TERMINATED)

    print("=" * 20, "\n")

    p1.transition(StateName.RUNNING)
    p2.transition(StateName.WAITING)

    print("=" * 20, "\n")

    print(p1)
    print(p2)

    print("=" * 20, "\n")

    p2.transition(StateName.RUNNING)

    print("=" * 20, "\n")

    print(p1)
    print(p2)

    print("=" * 20, "\n")

    [p.transition(StateName.BLOCKED) for p in (p1, p2)]

    print(p1)
    print(p2)

    print("=" * 20, "\n")

    [p.transition(StateName.TERMINATED) for p in (p1, p2)]

    print(p1)
    print(p2)

    print("=" * 20, "\n")


if __name__ == '__main__':
    main()
