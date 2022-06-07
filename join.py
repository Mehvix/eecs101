import os
import yaml

fdata = 'data.yaml'
data_dir = os.getcwd() + '/data/'

with open(fdata, 'r+') as fout:
    data = {}
    for i, fname in enumerate(os.listdir(data_dir)):
        print(i)
        with open(os.path.join(data_dir, fname), 'r') as stream:
            fin = yaml.safe_load(stream)
            nr = fin['nr']
            data[nr] = [fin]
    print('writing...')
    yaml.dump(data, fout, sort_keys=True)
