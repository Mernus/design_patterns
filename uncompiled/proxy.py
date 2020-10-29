from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    """
    Abstract subject class for Proxy and RealSubject classes

    """

    @abstractmethod
    def some_logic_implementation(self) -> None:
        """
        This method is abstract
        """
        pass


class Subject(AbstractSubject):
    """
    Subject class with some logic implementation

    """

    def some_logic_implementation(self) -> None:
        """
        Does some business logic actions

        """
        print("Subject logic implementation")


class Proxy(AbstractSubject):
    """
    Proxy class that add some additional behaviors to an object
    of some existing class without changing the client code

    """

    def __init__(self, subject: Subject) -> None:
        self._subject = subject

    def some_logic_implementation(self) -> None:
        """
        Checked permissions and use functions of subject

        """

        if self._check_permissions():
            self._subject.some_logic_implementation()

    @staticmethod
    def _check_permissions() -> bool:
        """
        Check permissions for usage of business logic

        :return: is permitted or not
        """
        return True


class Client:
    """
    Client implementation

    """

    @staticmethod
    def some_client_code(subject: Proxy):
        """
        Does some code that uses subject functions across Proxy

        :param subject:
        """
        subject.some_logic_implementation()


def main():
    client = Client()
    subject = Subject()
    proxy = Proxy(subject)

    client.some_client_code(proxy)


if __name__ == "__main__":
    main()
