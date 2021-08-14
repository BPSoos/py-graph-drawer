import yaml
import sys

def get_value_from_file(file, value):
    with open(file, 'r') as f:
        parsed_file = yaml.load(f, Loader=yaml.FullLoader)
        print(parsed_file[value])

def get_graph_drawer_data(file, value):
    with open(file, 'r') as f:
        parsed_file = yaml.load(f, Loader=yaml.FullLoader)
        print(parsed_file['graph-drawer'][value])



if __name__ == "__main__":
    exec(''.join(sys.argv[1:]))
