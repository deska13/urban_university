from pprint import pprint


class IntrospectionObj:
    _test = "test"
    __test_value = "test_value"

    def __init__(self) -> None:
        self.test = 42

    def test_method(self):
        pass


def introspection_info(obj):
    introspect_data = {
        "type": type(obj),
        "methods": [],
        "attributes": [],
        "module": obj.__class__.__module__,
    }
    for value in dir(obj):
        if callable(getattr(obj, value)):
            introspect_data["methods"].append(value)
        else:
            introspect_data["attributes"].append(value)
    return introspect_data


number_info = introspection_info(42)
pprint(number_info)

pprint(introspection_info(IntrospectionObj()))
