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


if __name__ == "__main__":
    print('loaded from command line')
    main1()
else:
    print('loaded using module import')
