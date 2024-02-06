def main():
    list_item = [{1: "test1"}, {2: "test2"}]

    list_of_list_items = [[{3: "test3"}, {4: "test4"}]]

    for item in list_of_list_items:
        list_item.extend(item)

    print(list_item)


if __name__ == "__main__":
    main()
