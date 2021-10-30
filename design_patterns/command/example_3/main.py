"""
Command Design Pattern

Intent: Turns a request into a stand-alone object that contains all information
about the request. This transformation lets you parameterize methods with
different requests, delay or queue a request's execution, and support undoable
operations.
"""

from invoker import Invoker
from commands import SimpleCommand, ComplexCommand
from receiver import Receiver


def main():
    """
    The client code can parameterize an invoker with any commands.
    """
    invoker = Invoker()
    receiver = Receiver()

    simple_command = SimpleCommand("Say Hi!")
    complex_command = ComplexCommand(receiver, "Send email", "Save report")

    invoker.set_on_start(simple_command)
    invoker.set_on_finish(complex_command)

    invoker.do_something_important()


if __name__ == "__main__":
    main()
