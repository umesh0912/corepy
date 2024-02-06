import hashlib


def main():
    data = b"example_data_to_hash_dfd"
    hash_object = hashlib.sha256(data)
    full_hash = hash_object.hexdigest()

    # Truncate to 234 characters
    truncated_hash = full_hash[:234]

    print(truncated_hash)


if __name__ == "__main__":
    main()