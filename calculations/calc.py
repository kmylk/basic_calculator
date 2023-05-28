from __future__ import annotations
from abc import ABC, abstractmethod
from kink import inject


class Context:
    """
    Context Interface
    """

    @inject
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Contain a strategy linked information
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Allow to change strategy.
        """

        self._strategy = strategy

    def calculate(self, a, b) -> None:
        """ Calculate according selected strategy logic """
        result = self._strategy.do_operation(a, b)
        return result


class Strategy(ABC):
    """ Base Interface for future inheritance with concrete implementations"""

    @abstractmethod
    def do_operation(self, a: int, b: int):
        pass


""" Concrete Strategies """


class SumStrategy(Strategy):
    def do_operation(self, a, b):
        return a + b


class SubStrategy(Strategy):
    def do_operation(self, a, b):
        return a - b


class MulStrategy(Strategy):
    def do_operation(self, a, b):
        return a * b


class DivStrategy(Strategy):
    def do_operation(self, a, b):
        if b != 0:
            result_number = a / b
            return result_number
        else:
            raise ValueError("Sorry, no numbers below zero")


def calculate(a, b, operand):
    """Switch logic for base calculation operation"""
    calc_context = Context(SumStrategy())
    match operand:
        case "sum":
            calc_context = Context(SumStrategy())
        case "sub":
            calc_context.strategy = SubStrategy()
        case "mul":
            calc_context.strategy = MulStrategy()
        case "div":
            calc_context.strategy = DivStrategy()
        case _:
            "No found matches"
    return calc_context.calculate(a, b)
