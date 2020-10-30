from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import itertools


class AbstractSubject(ABC):

    @abstractmethod
    def attach_to_observer(self, observer: AbstractObserver) -> None:
        """
        Attach an observer to the subject.

        """
        pass

    @abstractmethod
    def detach_from_observer(self, observer: AbstractObserver) -> None:
        """
        Detach an observer from the subject.

        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Notify all observers about some event.

        """
        pass

    @property
    @abstractmethod
    def state(self):
        """
        Some state which change will be notified

        """
        pass

    @abstractmethod
    def some_logic_implementation(self):
        """
        Some business logic implementation

        """
        pass


class Subject(AbstractSubject):
    """
    The Subject class has some state and notifies observers when the state changes.

    """

    _state: int = 0
    _observers: List[AbstractObserver] = []

    @property
    def state(self):
        """
        Getter for _state

        :return: state of this subject
        """
        return self._state

    def attach_to_observer(self, observer: AbstractObserver) -> None:
        self._observers.append(observer)

    def detach_from_observer(self, observer: AbstractObserver) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_logic_implementation(self) -> None:
        self._state += 1
        print(f"\nState has changed to: {self._state}")

        self.notify_observers()


class AbstractObserver(ABC):
    """
    Abstract observer with update method that called by subject
    """

    @abstractmethod
    def update(self, subject: AbstractSubject) -> None:
        """
        Called when subject updates

        :param subject: concrete subject
        """
        pass


class Observer(AbstractObserver):
    """
    Concrete Observer with concrete update method
    """

    def update(self, subject: AbstractSubject) -> None:
        if subject.state != 2:
            print("Observer: Reacted to the event")


class Client:
    """
    Client implementation

    """

    @staticmethod
    def some_client_code(subject: AbstractSubject):
        """
        Shows that Observer correctly configured

        :param subject: some subject
        """

        subject.some_logic_implementation()


def main():
    subject = Subject()
    observer = Observer()

    subject.attach_to_observer(observer)

    client = Client()

    for _ in itertools.repeat(None, 3):
        client.some_client_code(subject)

    subject.detach_from_observer(observer)

    client.some_client_code(subject)


if __name__ == "__main__":
    main()
