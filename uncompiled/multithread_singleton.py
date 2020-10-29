from threading import Lock, Thread
from queue import Queue
import datetime


class SingletonMeta(type):
    """
    Metaclass for multithreading realisation of Singleton class

    """

    _instances = {}
    _lock: Lock = Lock()  # blocking object to synchronize threads

    def __call__(cls, *args, **kwargs):
        """
        Call self as function and add new instances with locking

        :param args:
        :param kwargs:
        :return: instances
        """
        with cls._lock:
            if cls not in cls._instances:
                new_instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = new_instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Singleton main class realization

    """

    def __init__(self) -> None:
        self._cur_datetime = datetime.datetime.now()

    def some_logic_implementation(self) -> datetime:
        """
        Realizes some logic(print datetime of instance initialization)

        :return: current datetime
        """

        return self._cur_datetime


def singleton_usage() -> datetime:
    """
    Shows that Singleton was realized successfully

    :return: current datetime
    """
    singleton = Singleton()
    return singleton.some_logic_implementation()


if __name__ == "__main__":
    results = Queue(maxsize=2)  # Results of functions in threads

    # Initialize threads
    process1 = Thread(target=lambda queue: queue.put(singleton_usage()), args=(results,))
    process2 = Thread(target=lambda queue: queue.put(singleton_usage()), args=(results,))

    # Threads start
    process1.start()
    process2.start()

    # Join threads
    process1.join()
    process2.join()

    # Check for singleton was realized successfully
    if results.qsize() == 2:
        first, second = results.get(), results.get()
        assert first == second, "Error: Multiple singletons were created"
    else:
        print("Error: Bad implementation of Singleton")
