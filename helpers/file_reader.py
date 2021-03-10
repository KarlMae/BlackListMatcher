def remove_whitespaces(names):
    return [name.strip() for name in names]


def read_file_to_list(file_name):
    with open(file_name) as file:
        content = file.readlines()

    return remove_whitespaces(content)
