from abc import ABC, abstractmethod


class AbstractImplementation(ABC):
    """
    Class that defines the interface for implementation

    """

    @abstractmethod
    def some_operation(self) -> str:
        pass


class Abstraction:
    """
    The Abstraction defines the interface and delegate work for implementation

    """

    def __init__(self, delegate: AbstractImplementation) -> None:
        self._delegate = delegate

    def delegate_operation(self) -> str:
        return f"Abstraction: With {self._delegate.some_operation()}"


class FirstImplementation(AbstractImplementation):
    """
    First variance of implementation

    """

    def some_operation(self) -> str:
        return "FirstImplementation"


class SecondImplementation(AbstractImplementation):
    """
    Second variance of implementation

    """

    def some_operation(self) -> str:
        return "SecondImplementation"


class Client:
    """
    Client implementation

    """

    @staticmethod
    def some_client_code(abstraction: Abstraction):
        """
        Links some abstraction and implementation

        :param abstraction:
        """

        pair = abstraction.delegate_operation()
        print(pair)


def main():
    client = Client()
    one_implementation = FirstImplementation()
    another_implementation = SecondImplementation()

    one_abstraction = Abstraction(one_implementation)
    another_abstraction = Abstraction(another_implementation)

    client.some_client_code(one_abstraction)
    client.some_client_code(another_abstraction)


if __name__ == "__main__":
    main()
