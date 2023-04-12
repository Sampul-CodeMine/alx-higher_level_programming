#!/usr/bin/python3
"""A python script that adds arguments passed from the CLI
during program execution and save them to a file."""


if __name__ == "__main__":
    import sys as s
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

    try:
        vargs = load_from_json_file("add_item.json")
    except FileNotFoundError:
        vargs = []
    vargs.extend(s.argv[1:])
    save_to_json_file(vargs, "add_item.json")
