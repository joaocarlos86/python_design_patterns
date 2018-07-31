import types
from ForwardStrategy import ForwardStrategy
from BackwardStrategy import BackwardStrategy
import argparse
import sys

class StrategyExecutor:
    def __init__(self, strategy=None):
        if strategy is not None:
            self.execute = types.MethodType(strategy, self)

    def execute(self, to_be_processed):
        print("Strategy not implemented")


if __name__ == '__main__':
    available_strategies = []
    available_strategies.append(BackwardStrategy())
    available_strategies.append(ForwardStrategy())

    to_be_processed = sys.argv[1]

    executor = StrategyExecutor()

    for strategy in available_strategies:
        if strategy.supports(to_be_processed):
            executor = StrategyExecutor(strategy.execute)
            break
	
    executor.execute(to_be_processed)
