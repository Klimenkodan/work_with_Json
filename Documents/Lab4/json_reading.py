import json


def json_reading(file_name, key=None):
    """
    This function make the dictionary from the information in json format
    """
    f = open(file_name, 'r', encoding = "utf-8")
    file = json.load(f)
    keys_json = file.keys()
    if not isinstance(key, str):
        return keys_json
    else:
        return file[key]


def user_quest():
    """
    This function gets the name of the key that user want to see
    """
    key = input("There are keys, that this dictionary includes.\nPlease enter name of key, that you want to see\n")
    return key


if __name__ == "__main__":
    print(json_reading('user_friends.json'))
    print(json_reading('user_friends.json', user_quest()))
