import yaml

with open(r'test.yaml') as file:
    the_list = yaml.load(file, Loader=yaml.fullLoader)
    print(the_list)