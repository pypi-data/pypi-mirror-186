import yaml

from yaml.loader import SafeLoader

def get_yml_to_dic(yml_path):
    with open(yml_path, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data