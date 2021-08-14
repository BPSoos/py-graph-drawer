import yaml
import sys

def get_value_from_file(file, value):
    with open(file, 'r') as f:
        data = yaml.parse(f.read())
        print(str(data))


if __name__ == "__main__":
    exec(''.join(sys.argv[1:]))
