from Strategy import Strategy
import sys

class ForwardStrategy(Strategy):
    def supports(self, to_be_processed):
            if to_be_processed == "ForwardStrategy":
                return True
            else:
                return False

    def execute(self, executor, to_be_processed):
        print("Executing logic to process ForwardStrategy")
