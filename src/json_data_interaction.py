import json


def get_data(filename):
    with open(filename, "r") as read_file:
        return json.load(read_file)