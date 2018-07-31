import abc

class Strategy:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports(self, to_be_processed):
        pass

    @abc.abstractmethod
    def execute(self, executor, to_be_processed):
        pass
