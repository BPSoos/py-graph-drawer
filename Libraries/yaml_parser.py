import ast
import os
import sys


def get_value_from_file(file, value):
    with open(os.path.normpath(file), 'r') as f:
        parsed_file = ast.literal_eval(f.read().replace('\n', '').replace(' ', ''))
        print(parsed_file[value])


def get_graph_drawer_data(file, value):
    with open(os.path.normpath(file), 'r') as f:
        parsed_file = ast.literal_eval(f.read().replace('\n', '').replace(' ', ''))
        print(parsed_file['graph-drawer'][value])


if __name__ == "__main__":
    exec(''.join(sys.argv[1:]))
