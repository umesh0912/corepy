def testDecorator(f):
    def wrap(*args, **kwargs):
        print('calling function name ' + f.__name__)
        return f(*args, **kwargs)

    return wrap


class Person:
    def __init__(self, name):
        self._name = name

    @testDecorator
    def name(self):
        return self._name


@testDecorator
def main1():
    print("main method")
    p = Person("Umesh")
    p.name()
    list_p = []
    list_string1 = list(["abc", "pqr", "uj"])
    list_string2 = list(["xyz", "pqr", "tt"])
    list_p.append(list_string1)
    list_p.append(list_string2)
    list_2 = lambda list_3: (
        _data = []
        for l in list_3:
            _data.apeend(l)
         _data
    )
    print(list_p)


if __name__ == "__main__":
    print('loaded from command line')
    main1()
else:
    print('loaded using module import')
