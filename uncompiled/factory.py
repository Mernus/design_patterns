from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """
    Some abstract product with abstract method

    """

    @abstractmethod
    def some_logic_implementation(self) -> str:
        pass


class FirstProduct(AbstractProduct):
    """
    Some concrete product that realize one of various implementation of business logic

    """

    def some_logic_implementation(self) -> str:
        return "Some result of FirstProduct"


class SecondProduct(AbstractProduct):
    """
    Some concrete product that realize one of various implementation of business logic

    """

    def some_logic_implementation(self) -> str:
        return "Some result of SecondProduct"


class AbstractCreator(ABC):
    """
    Abstract Creator that contain factory method that is supposed to return object of a Concrete Product

    """

    @abstractmethod
    def factory(self):
        pass

    def some_logic_implementation(self) -> str:
        """
        Contains some core business logic that relies on Product objects, returned by the factory method.

        :return: result of work with product
        """
        product = self.factory()

        result = f"Creator: Worked with {product.some_logic_implementation()}"
        return result


class FirstCreator(AbstractCreator):
    """
    Some concrete creator that realize one of various implementation of factory method

    """

    def factory(self) -> AbstractProduct:
        return FirstProduct()


class SecondCreator(AbstractCreator):
    """
    Some concrete creator that realize one of various implementation of factory method

    """

    def factory(self) -> AbstractProduct:
        return SecondProduct()


class Client:
    """
    Client implementation

    """

    @staticmethod
    def some_client_code(creator: AbstractCreator):
        """
        Shows that Factory method correctly configured

        :param creator:
        """

        print(creator.some_logic_implementation())


def main():
    client = Client()

    client.some_client_code(FirstCreator())
    client.some_client_code(SecondCreator())


if __name__ == "__main__":
    main()
