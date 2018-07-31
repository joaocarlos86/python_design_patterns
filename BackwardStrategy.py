from Strategy import Strategy

class BackwardStrategy(Strategy):
    def supports(self, to_be_processed):
        if to_be_processed == "BackwardStrategy":
            return True
        else:
            return False

    def execute(self, executor, to_be_processed):
        print("Executing logic to process " + to_be_processed)
