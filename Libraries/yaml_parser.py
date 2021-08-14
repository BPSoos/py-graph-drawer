import yaml
import sys

def get_value_from_file(file, value):
    with open(file, 'r') as f:
        parsed_file = yaml.load(f, Loader=yaml.FullLoader)
        for key in parsed_file.keys():
            print(parsed_file[key])


if __name__ == "__main__":
    exec(''.join(sys.argv[1:]))
