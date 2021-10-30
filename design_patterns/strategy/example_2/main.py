from strategies import AddStrategy, SubtractStrategy, MultiplyStrategy
from context import Context


def perform(a, b, action):
    context = Context()

    action_strategy = {
        "add": AddStrategy,
        "subtract": SubtractStrategy,
        "multiply": MultiplyStrategy,
    }

    strategy = action_strategy[action]()

    # User supplies context with the strategy
    context.strategy = strategy

    result = context.execute_strategy(a, b)

    return result


if __name__ == '__main__':
    print(perform(3, 4, "add"))
    print(perform(3, 4, "subtract"))
    print(perform(3, 4, "multiply"))
