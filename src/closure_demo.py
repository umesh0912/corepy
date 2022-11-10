def raise_to(exp):
    def raised_to_power(x):
        return pow(x, exp)

    return raised_to_power


def main():
    square = raise_to(2);

    print("square of 8 --> " + str(square(8)))


if __name__ == '__main__':
    main()
