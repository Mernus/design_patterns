import json


class Adaptable:
    """
    Adaptable class which cannot be used by Client directly

    """

    def __init__(self, some_dict: dict) -> None:
        """
        Initialize adaptee object with some dictionary

        :param some_dict: some initial dict
        """
        self._dict = some_dict

    @property
    def some_dict(self) -> dict:
        """
        Property that returns adaptee dict

        :return: initial dict
        """
        return self._dict


class Target:
    """
    Target class

    """

    @staticmethod
    def unpack_json(json_obj: str) -> object:
        """
        Method which takes some json object and prints it as dict

        :param json_obj:
        :return:
        """
        dict_obj = json.loads(json_obj)

        return dict_obj.values()


class Adapter(Target, Adaptable):
    """
    Makes interface of Adaptable compatible with Target interface

    """

    def convert(self) -> str:
        """
        Convert dict object to json

        :return:
        """
        json_obj = json.dumps(self.some_dict)
        return json_obj


class Client:
    """
    Client implementation

    """

    @staticmethod
    def some_client_code(adapter: Adapter):
        """
        Shows that Adapter correctly configured

        :param adapter:
        """
        json_obj = adapter.convert()

        target = Target()
        print("Target:\t" + str(target.unpack_json(json_obj)))


if __name__ == "__main__":
    temp_dict = {
        "name": "John",
        "age": 30
    }

    adaptable = Adaptable(temp_dict)
    print("Adaptable:\t" + str(adaptable.some_dict))

    adapter = Adapter(temp_dict)
    print("Adapter:\t" + adapter.convert())
    client = Client()
    client.some_client_code(adapter)
