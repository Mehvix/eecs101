import os
import yaml

data = 'data.yaml'
data_dir = os.getcwd() + '/data/'
processed = 'processed.txt'

for fname in os.listdir(data_dir):
    if fname not in open(processed).read():
        with open(os.path.join(data_dir, fname), 'r') as stream:
            fin = yaml.safe_load(stream)
            nr = fin['nr']
            with open(data, 'a') as fout:
                yaml.dump({nr: fin}, fout, sort_keys=True)
            with open(processed, 'a') as fout:
                fout.write(fname)
