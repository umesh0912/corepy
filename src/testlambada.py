def main():
    print("Hi Welcome to lambada world")
    names = ["Umesh Jadhav", "Piyush Jadhav", "Puja wagh", "Umesh P", "Piyush U", "Puja J"]

    print(names)
    rs = sorted(names, key=lambda name: name.split()[-1])
    print(rs)


if __name__ == "__main__":
    main()
else:
    print("module imported successfully")
