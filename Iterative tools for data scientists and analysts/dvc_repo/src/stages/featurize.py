import argparse

import yaml
#from src.stages.data_load import data_load for jupyter notebook
from data_load import data_load


def featurize(config_path):
    dataset=data_load(config_path)
    dataset['sepal_length_to_sepal_width'] = dataset['sepal_length'] / \
        dataset['sepal_width']


    dataset['petal_length_to_petal_width'] = dataset['petal_length'] / \
        dataset['petal_width']

    dataset = dataset[[
        'sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        #     'sepal_length_in_square', 'sepal_width_in_square', 'petal_length_in_square', 'petal_width_in_square',
        'sepal_length_to_sepal_width', 'petal_length_to_petal_width',
        'target'
    ]]
    with open(config_path, "r") as f:
        param = yaml.safe_load(f)
    dataset.to_csv(param['data']['features_path'], index=False)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', dest='param',
                        default='params.yaml')
    args = parser.parse_args()
    featurize(config_path=args.param)
